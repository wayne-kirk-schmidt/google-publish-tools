#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

This script is a general publisher of content to a Google Drive.
Designed to work with an Oauth token, please refer to documents
on how to set up a token and use specific SCOPES

Usage:
    $ python  gmkdir [ options ]

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           gmkdir
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import argparse
import datetime
import sys
import os
import apiclient
from httplib2 import Http
from oauth2client import file, client, tools

sys.dont_write_bytecode = 1

PARSER = argparse.ArgumentParser(description="""

This is a general publisher for documents to a Google drive.
By default this uploads content, exports it to a Google 
format, and then exports file contents to a PDF file.

""")

PARSER.add_argument('-c', metavar='<creds>', dest='creds', help='specify secret file')
PARSER.add_argument('-t', metavar='<token>', dest='token', help='specify token file')
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
    os.environ['TOKENFILE'] = ARGS.token
if ARGS.dir:
    os.environ['TARGETDIR'] = ARGS.dir

try:
    CREDENTIALS = os.environ['CREDENTIALS']
    TOKENFILE = os.environ['TOKENFILE']
    TARGETDIR = os.environ['TARGETDIR']
except KeyError as myerror:
    print('Environment Variable Not Set :: {} '.format(myerror.args[0]))

SCOPES = ('https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets')

def move_target_file(service, id_, folder_id):
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
        print('Moved FolderID: %s' % folder_id)
        print('To ParentID: %s' % id_)

def create_target_dir(service, targetname, parent_id):
    """
    Create the target directory to store the files
    """
    dir_metadata = {'name': targetname, 'mimeType': 'application/vnd.google-apps.folder'}
    directory_result = service.files().create(body=dir_metadata, fields='id').execute()
    folder_id = directory_result.get('id')
    if ARGS.verbose:
        print('Created FolderID: %s' % folder_id)
    if parent_id != "undefined":
        move_target_file(service, parent_id, folder_id)
    return folder_id

def create_auth():
    """
    Fetch or create the credentials used to create the service
    """
    store = file.Storage(TOKENFILE)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(CREDENTIALS, SCOPES)
        creds = tools.run_flow(flow, store)
        service = apiclient.discovery.build('drive', 'v3', http=creds.authorize(Http()))
    service = apiclient.discovery.build('drive', 'v3', credentials=creds)
    return service

def split_target_path(targetpath):
    """
    This subroutine splits an array into component parts, this returns an array
    """
    path_element_array = []
    while 1:
        path_elements = os.path.split(targetpath)
        if path_elements[0] == targetpath:  # sentinel for absolute paths
            path_element_array.insert(0, path_elements[0])
            break
        elif path_elements[1] == targetpath: # sentinel for relative paths
            path_element_array.insert(0, path_elements[1])
            break
        else:
            targetpath = path_elements[0]
            path_element_array.insert(0, path_elements[1])
    return path_element_array

def main():
    """
    This is the main lodule for authentication, and file operations
    """
    (service) = create_auth()
    path_element_array = split_target_path(TARGETDIR)
    parent_id = "undefined"
    for direlement in reversed(path_element_array):
        if ARGS.verbose:
            print('Creating: %s' % direlement)
        parent_id = create_target_dir(service, direlement, parent_id)

if __name__ == '__main__':
    main()
