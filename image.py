#!/usr/bin/python
# System Command CGI
# Blocking Server

import os, cgi, sys
import commands
from subprocess import Popen, STDOUT, PIPE

print "Content-type: image/gif\r\n"
import time
time.sleep(3)

print open('./1.gif').read()
