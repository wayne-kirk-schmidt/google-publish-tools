#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

This is a modified google quickstart.pyy to bootstrap/validate credentials.

Usage:
    $ python  quickstart.py credentials.json token.pickle

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import sys
import os
import pickle
import apiclient
import google
import google_auth_oauthlib

sys.dont_write_bytecode = 1

CREDENTIALS = sys.argv[1]
TOKENPICKLE = sys.argv[2]

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file TOKENPICKLE stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
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

    service = apiclient.discovery.build('drive', 'v3', credentials=creds)
    return service

if __name__ == '__main__':
    main()
