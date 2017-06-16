# -*- coding: latin-1 -*-

import urllib,urllib2
import base64
import json

class Ziron:

	def __init__(self,sid,authkey,baseurl="https://api.ziron.net/v1"):
		self.sid = sid
		self.authkey = authkey
		self.baseurl = baseurl

		if not self.sid:
			raise ValueError("sid must not be null")
		
		if not self.authkey:
			raise ValueError("authkey must not be null")
		

	def send_request(self, resource, parameters, method):
		req = urllib2.Request(url=self.baseurl+"/Accounts/"+self.sid+resource, data=urllib.urlencode( parameters, True ))
		req.get_method = lambda: method
		req.add_header("Accept","application/json; charset=utf-8")
		req.add_header("Content-Type","application/x-www-form-urlencoded")
		req.add_header("Authorization","Basic %s" %  base64.b64encode("%s:%s" % (self.sid,self.authkey)))

		f = urllib2.urlopen(req)
		response = json.loads( f.read() )
		return response 


	def message_send(self, parameters):
		return self.send_request( "/Messages", parameters, "POST" )


	def lookup(self,parameters):
		return self.send_request( "/Lookups", parameters, "POST" )


	def account_retrieve(self):
		return self.send_request( "", "", "GET" )






