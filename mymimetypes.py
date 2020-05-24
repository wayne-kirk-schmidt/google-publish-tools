#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Explanation:

    This is a datastructure file for mimetypes

Usage:
    $ python mimtypes.py

Style:
    Google Python Style Guide:
    http://google.github.io/styleguide/pyguide.html

    @name           mimtypes
    @version        1.0.0
    @author-name    Wayne Schmidt
    @author-email   wayne.kirk.schmidt@gmail.com
    @license-name   GNU GPL
    @license-url    http://www.gnu.org/licenses/gpl.html
"""

__version__ = '1.0.0'
__author__ = "Wayne Schmidt (wayne.kirk.schmidt@gmail.com)"

import sys
sys.dont_write_bytecode = 1

MIMETYPES = dict()
MIMETYPES["pdf"] = "application/pdf"
MIMETYPES["html"] = "text/html"
MIMETYPES["htm"] = "text/html"
MIMETYPES["ics"] = "text/calendar"
MIMETYPES["gif"] = "image/gif"
MIMETYPES["bmp"] = "image/bmp"
MIMETYPES["jpg"] = "image/jpeg"
MIMETYPES["jpeg"] = "image/jpeg"
MIMETYPES["gif"] = "image/gif"
MIMETYPES["png"] = "image/png"
MIMETYPES["json"] = "application/json"
MIMETYPES["gaudio"] = "application/vnd.google-apps.audio"
MIMETYPES["gdoc"] = "application/vnd.google-apps.document"
MIMETYPES["gdrive"] = "application/vnd.google-apps.drive-sdk"
MIMETYPES["gdraw"] = "application/vnd.google-apps.drawing"
MIMETYPES["gfile"] = "application/vnd.google-apps.file"
MIMETYPES["gdir"] = "application/vnd.google-apps.folder"
MIMETYPES["gform"] = "application/vnd.google-apps.form"
MIMETYPES["gtable"] = "application/vnd.google-apps.fusiontable"
MIMETYPES["gmap"] = "application/vnd.google-apps.map"
MIMETYPES["gphoto"] = "application/vnd.google-apps.photo   "
MIMETYPES["gslide"] = "application/vnd.google-apps.presentation"
MIMETYPES["gscript"] = "application/vnd.google-apps.script"
MIMETYPES["glink"] = "application/vnd.google-apps.shortcut"
MIMETYPES["gsite"] = "application/vnd.google-apps.site"
MIMETYPES["gsheet"] = "application/vnd.google-apps.spreadsheet"
MIMETYPES["gunknown"] = "application/vnd.google-apps.unknown "
MIMETYPES["gvideo"] = "application/vnd.google-apps.video"
MIMETYPES["doc"] = "application/msword"
MIMETYPES["dot"] = "application/msword"
MIMETYPES["docx"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
MIMETYPES["dotx"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.template"
MIMETYPES["docm"] = "application/vnd.ms-word.document.macroEnabled.12"
MIMETYPES["dotm"] = "application/vnd.ms-word.template.macroEnabled.12"
MIMETYPES["xls"] = "application/vnd.ms-excel"
MIMETYPES["xlt"] = "application/vnd.ms-excel"
MIMETYPES["xla"] = "application/vnd.ms-excel"
MIMETYPES["xlsx"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
MIMETYPES["xltx"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.template"
MIMETYPES["xlsm"] = "application/vnd.ms-excel.sheet.macroEnabled.12"
MIMETYPES["xltm"] = "application/vnd.ms-excel.template.macroEnabled.12"
MIMETYPES["xlam"] = "application/vnd.ms-excel.addin.macroEnabled.12"
MIMETYPES["xlsb"] = "application/vnd.ms-excel.sheet.binary.macroEnabled.12"
MIMETYPES["ppt"] = "application/vnd.ms-powerpoint"
MIMETYPES["pot"] = "application/vnd.ms-powerpoint"
MIMETYPES["pps"] = "application/vnd.ms-powerpoint"
MIMETYPES["ppa"] = "application/vnd.ms-powerpoint"
MIMETYPES["pptx"] = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
MIMETYPES["potx"] = "application/vnd.openxmlformats-officedocument.presentationml.template"
MIMETYPES["ppsx"] = "application/vnd.openxmlformats-officedocument.presentationml.slideshow"
MIMETYPES["ppam"] = "application/vnd.ms-powerpoint.addin.macroEnabled.12"
MIMETYPES["pptm"] = "application/vnd.ms-powerpoint.presentation.macroEnabled.12"
MIMETYPES["potm"] = "application/vnd.ms-powerpoint.template.macroEnabled.12"
MIMETYPES["ppsm"] = "application/vnd.ms-powerpoint.slideshow.macroEnabled.12"

MAPPINGS = dict()
MAPPINGS["doc"] = "gdoc"
MAPPINGS["docx"] = "gdoc"
MAPPINGS["xls"] = "gsheet"
MAPPINGS["xlsx"] = "gsheet"
MAPPINGS["ppt"] = "gslide"
MAPPINGS["pptx"] = "gslide"
MAPPINGS["gdoc"] = "docx"
MAPPINGS["gsheet"] = "xlsx"
MAPPINGS["gslide"] = "pptx"
