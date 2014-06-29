#!/usr/bin/python
# System Command CGI

import os, cgi, sys
import commands
import json, time
from subprocess import Popen, STDOUT, PIPE

print "Content-type: application/json\r\n"

data = {
	'a': 1
}

time.sleep(3)

print json.dumps(data)