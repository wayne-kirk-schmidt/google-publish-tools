
Google Publisher and Converter
==============================

This is a collection of tools to demonstrate how to use the Google Drive via the API.

The first tool starts with download, upload, and conversion, as well as moving files.

As this repository grows, we will make more DevOps friendly tools handle single tasks.

Installing the Project
======================

The scripts are command line based, designed to be used within a batch script or DevOPs tool.
All are python3 scripts. The complete list of the python modules are listed in a Pipfile for install.

You will need to use Python 3.6 or higher and the modules listed in the dependency section.  

The steps are as follows: 

    1. Download and install python 3.6 or higher from python.org. Append python3 to the LIB and PATH env.

    2. Download and install git for your platform if you don't already have it installed.
       It can be downloaded from https://git-scm.com/downloads
    
    3. Open a new shell/command prompt. It must be new since only a new shell will include the new python 
       path that was created in step 1. Cd to the folder where you want to install the scripts.
    
    4. Execute the following command to install pipenv, which will manage all of the library dependencies:
    
        sudo -H pip3 install pipenv 
 
    5. Clone this repo using the following command:
    
       git clone git@github.com:wayne-kirk-schmidt/google-publish-tools.git

    This will create a new folder google-publish-tools
    
    6. Change into the folder. Type the following to install all the package dependencies 
       (this may take a while as this will download all of the libraries that it uses):

        pipenv install
        
Getting this set up
===================

    1. The first thing to do is to enable the Google Drive API

[Enable-Google-Drive-API](https://developers.google.com/drive/api/v3/enable-drive-api)


    2. The next thing to do is to configure the quickstart for the Google Drive API

[Google-Drive-Quickstart](https://developers.google.com/drive/api/v3/quickstart/python)


Dependencies
============

See the contents of "pipfile"

Script Names and Purposes
=========================

Scripts and Functions:

    1. gpublish - this is the first script combining upload, download, and file conversion

                   
To Do List:
===========

* Extend more scripts to include discrete functions

* Extend the mime type support

* Build the tools into a subject verb object format

License
=======

Copyright 2020 Wayne Kirk Schmidt

Licensed under the GNU GPL License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    license-name   GNU GPL
    license-url    http://www.gnu.org/licenses/gpl.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
=======

Feel free to e-mail me with issues to: wayne.kirk.schmidt@gmail.com
I will provide "best effort" fixes and extend the scripts.
