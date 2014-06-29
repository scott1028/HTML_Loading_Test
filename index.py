#!/usr/bin/python
# System Command CGI

import os, cgi, sys
import commands
from subprocess import Popen, STDOUT, PIPE

print '''Content-type: text/html\r\n

<html>
<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
</head>
<body>
	<div id="container">
	loading
	</div>
	<script>
		$.get('store.py', function(r, i ,a){
			console.log(r);

			$('#container').text(r.a);
		});

		function imgError(image) {
			image.onerror = "";
			image.src = "loading.gif";
			return true;
		}
	</script>
	<img src="image.py" style="width: 200px; height: 300px;" onerror="imgError(this);" />
</body>
<script>
	$('body').ready(function(e){
		console.log(e);
	});
</script>
<style>
	/* Make Ajax Loading Image and fit it's container. */
	img {
		background: url('loading.gif');
		background-size: 100% 100%;
		background-repeat: no-repeat;
	}
</style>
</html>'''