
Google Specific Information
===========================

There are several steps to building a Google Application

1. Create a specific Google Project

2. Enable the Google Drive API for that project

3. Configure an Application that will run in the Project to use the API

4. Provide a consent screen for the Application

5. Assign a credential to the Applicatin and Consent Screen

6. Create Oauth credentials that can be used to authenticate

7. Authorize the credentials with your account using the consent screen

8. The credentials are given a token stored in a pickle file

9. This pickle is refreshed, and needs to be rerun if credentials, projects, applicatioons, or SCOPES change


Google Specific Preparatory Work
================================

*First visit this link*
[Getting Started](https://support.google.com/googleapi/answer/6158841?hl=en)

| *Step Descrription or Picture*                                                               |
|:---------------------------------------------------------------------------------------------|
|                                                                                              |
| Step-001:  Next visit this view API status. https://console.developers.google.com/           |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.001.png) |
|                                                                                              |
| Step-002:  Click on the three dots to the right of "Google APIS"                             |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.002.png) |
|                                                                                              |
| Step-003:  You should see all projects with your organization. Click "Create Project"        |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.003.png) |
|                                                                                              |
| Step-004: Now specify a name for the project "gPublisher". specify a location. hit create.   |                                             |
|            After a short time you should see the creation event and other recent events.     |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.004.png) |
|                                                                                              |
| Step-005: Click on the project in the finish, click on the project and API View              |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.005.png) |
|                                                                                              |
| Step-006: Click on view and on click on "Enable APIS and Services"                           |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.006.png) |
|                                                                                              |
| Step-007: Confirm you can see all of the API listed                                          |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.007.png) |
|                                                                                              |
| Step-008: Filter and select the Google Drive API                                             |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.008.png) |
|                                                                                              |
| Step-009: Click on Enable the API                                                            |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.009.png) |
|                                                                                              |
| Step-010: After the API is enabled, then click on "Create Credentials" on the right          |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.010.png) |
|                                                                                              |
| Step-011: Fill out the data requested in the creation screen                                 |
|           Choose "Google Drive API", select "Other UI", and then select "User Data"          |
|           Finally click on "What credentials do I need?"                                     |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.011.png) |
|                                                                                              |
| Step-012: This will bring up a "Configure Consent" screen. Select this"                      |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.012.png) |
|                                                                                              |
| Step-013:  Choose internal application, and then click on create.                            |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.013.png) |
|                                                                                              |
| Step-014: After done the screen goes back to the project. Select Credentials                 |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.014.png) |
|                                                                                              |
| Step-015: Select on "Create Credentials" in the middle of the screen                         |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.015.png) |
|                                                                                              |
| Step-016: Choose "Oauth ID" as the authentication credentials to build                       |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.016.png) |
|                                                                                              |
| Step-017: Choose Desktop Application, and then put in the name of the app "gPublisher"       |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.017.png) |
|                                                                                              |
| Step-018: The next screen allows you to copy the key and secret. This is not necessary.      |
|           Close this to download the oauth file instead.                                     |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.018.png) |
|                                                                                              |
| Step-019: Look for the Oauth credentials created, and then click on the download icon        |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.019.png) |
|                                                                                              |
| Copy the downloaded secret file to a directory of your choosing. An example is shown below:  |
| prompt> cp ../client_secret_XXX.apps.googleusercontent.com.json /tmp/credentials.json        |
|                                                                                              |
| Run the quickstart.py script to authorize the credentials. An example is show below:         |
| prompt> ./quickstart.py /tmp/credentials.json /tmp/token.pickle                              |
|                                                                                              |
| Step-20: This will launch the authorization window. Choose the Google account to use this    |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.020.png) |
|                                                                                              |
| Step-021: Then consent to the permissions being granted this google application              |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.021.png) |
|                                                                                              |
| Step-022: This is complete now. You can use the script in the project                        |
|                                                                                              |
| ![](https://github.com/wayne-kirk-schmidt/google-publish-tools/blob/master/doc/pictures/gsetup.step.022.png) |
|                                                                                              |

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

Feel free to e-mail me with issues to: 

wayne.kirk.schmidt@gmail.com
wschmidt@sumologic.com

I will provide "best effort" fixes and extend the scripts.
