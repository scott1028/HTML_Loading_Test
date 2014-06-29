#!/usr/bin/python
# System Command CGI
# Blocking Server

import os, cgi, sys
import commands
from subprocess import Popen, STDOUT, PIPE

print "Content-type: image/jpeg\r\n"
import time
time.sleep(3)

print open('./loaded.jpg').read()
