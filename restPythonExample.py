#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests

xml = """<ScriptBean>
		<script>
			def querySrv = server.get("QueryService");


objectType="Object"

name="test osama"
description="test description"
scheduleName="Always"

serviceName="my"
msg = new StringBuilder();



queryStr="FSMService where name = \'"+serviceName+"\'"
service = querySrv.queryTopologyObjects(queryStr)
objects=service[0].definition

		</script>
	</ScriptBean>"""

    
headers = {'Content-Type': 'application/xml','Access-Token':'gl57ru0u4rhgaq3pdcj04ef9so',} # set what your server accepts
print requests.post('http://199.204.218.63:8080/api/v1/script/runScript', data=xml, headers=headers).text