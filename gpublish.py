#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

This script is a general publisher of content to a Google Drive.
Designed to work with an Oauth token, please refer to documents
on how to set up a token and use specific SCOPES

Usage:
    $ python  gpublish [ options ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           gpublish
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"


import sys
import os
import apiclient
import pickle
import google
import google_auth_oauthlib
import googleapiclient
import argparse
import datetime
import mymimetypes

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

This is a general publisher for documents to a Google drive.
By default this uploads content, exports it to a Google 
format, and then exports file contents to a PDF file.

""")

PARSER.add_argument('-c', metavar='<creds>', dest='creds', help='specify secret file')
PARSER.add_argument('-t', metavar='<token>', dest='token', help='specify token file')
PARSER.add_argument('-f', metavar='<file>', dest='file', help='specify source file')
PARSER.add_argument('-d', metavar='<dir>', dest='dir', help='specify target directory')
PARSER.add_argument('-v', '--verbose', help='verbose', action="store_true")

ARGS = PARSER.parse_args()

CURRENT = datetime.datetime.now()
DSTAMP = CURRENT.strftime("%Y%m%d")
TSTAMP = CURRENT.strftime("%H%M%S")
LSTAMP = DSTAMP + '.' + TSTAMP

if ARGS.creds:
    os.environ['CREDENTIALS'] = ARGS.creds
if ARGS.token:
    os.environ['TOKENPICKLE'] = ARGS.token
if ARGS.file:
    os.environ['TARGETFILE'] = ARGS.file
    os.environ['TARGETNAME'] = os.path.basename(ARGS.file)
if ARGS.dir:
    os.environ['TARGETDIR'] = ARGS.dir

try:
    CREDENTIALS = os.environ['CREDENTIALS']
    TOKENPICKLE = os.environ['TOKENPICKLE']
    TARGETFILE = os.environ['TARGETFILE']
    TARGETNAME = os.environ['TARGETNAME']
    TARGETDIR = os.environ['TARGETDIR']
except KeyError as myerror:
    print('Environment Variable Not Set :: {} '.format(myerror.args[0]))

SCOPES = ('https://www.googleapis.com/auth/drive')

def move_output_pdf(service, id_, folder_id):
    """
    Moving a file in Google Drive means assigning the correct parents
    """
    file_ = service.files().get(fileId=id_, fields='parents').execute()
    service.files().update(
        fileId=id_,
        addParents=folder_id,
        removeParents=file_['parents'][0],
        fields='id,parents').execute()
    if ARGS.verbose:
        print('Source_FileID: %s' % id_)
        print('Target_FolderID: %s' % folder_id)

def create_target_dir(service):
    """
    Create the target directory to store the files
    """
    dir_metadata = {'name': TARGETDIR, 'mimeType': 'application/vnd.google-apps.folder'}
    directory_result = service.files().create(body=dir_metadata, fields='id').execute()
    folder_id = directory_result.get('id')
    if ARGS.verbose:
        print('FolderID: %s' % folder_id)
    return folder_id


def create_auth():
    """
    Fetch or create the credentials used to create the service
    """

    if os.path.exists(TOKENPICKLE):
        with open(TOKENPICKLE, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKENPICKLE, 'wb') as token:
            pickle.dump(creds, token)

    service = googleapiclient.discovery.build('drive', 'v3', credentials=creds)
    return service

def define_mime_types():
    """
    assign the mime types based on the MAPPING and file extension
    """
    file_extension = os.path.splitext(TARGETFILE)[1][1:]
    src_mime = mymimetypes.MIMETYPES[file_extension]
    dst_mime = mymimetypes.MIMETYPES[mymimetypes.MAPPINGS[file_extension]]
    return src_mime, dst_mime

def upload_native_file(service, folder_id, src_mime):
    """
    Upload the native file to the parent directory
    """
    file_metadata = {'name': TARGETNAME, 'parents': [folder_id]}
    media = apiclient.http.MediaFileUpload(TARGETFILE, mimetype=src_mime)
    native_file_result = service.files().create(
        body=file_metadata, media_body=media, fields='id'
        ).execute()
    native_file_id = native_file_result.get('id')
    if ARGS.verbose:
        print('Native_FileID: %s' % native_file_id)

def upload_google_file(service, folder_id, src_mime, dst_mime):
    """
    Upload the google equivalent of the native file to the parent directory
    """
    file_metadata = {'name': TARGETNAME, 'mimeType': dst_mime, 'parents': [folder_id]}
    media = apiclient.http.MediaFileUpload(TARGETFILE, resumable=True, mimetype=src_mime)
    google_file_result = service.files().create(
        body=file_metadata, media_body=media, fields='id'
        ).execute()
    google_file_id = google_file_result.get('id')
    if ARGS.verbose:
        print('Google_FileID: %s' % google_file_id)
    return google_file_id

def convert_file_to_pdf(service, folder_id, google_file_id):
    """
    Create the PDF file and then move from the base directory to the target directory
    """
    file_name = os.path.splitext(TARGETNAME)[0]
    targetpdf = file_name + ".pdf"
    pdf_mime = mymimetypes.MIMETYPES["pdf"]
    data = service.files().export(fileId=google_file_id, mimeType=pdf_mime).execute()
    body = {'name':targetpdf, 'mimeType':pdf_mime}
    file_handle = apiclient.http.BytesIO(data)
    media_body = apiclient.http.MediaIoBaseUpload(file_handle, mimetype=pdf_mime)
    pdf_file_id = service.files().create(body=body, media_body=media_body).execute()['id']
    if ARGS.verbose:
        print('DstPDF_FileID: %s' % pdf_file_id)

    move_output_pdf(service, pdf_file_id, folder_id)

def main():
    """
    This is the main lodule for authentication, and file operations
    """
    (service) = create_auth()
    folder_id = create_target_dir(service)
    (src_mime, dst_mime) = define_mime_types()
    upload_native_file(service, folder_id, src_mime)
    google_file_id = upload_google_file(service, folder_id, src_mime, dst_mime)
    convert_file_to_pdf(service, folder_id, google_file_id)

if __name__ == '__main__':
    main()
