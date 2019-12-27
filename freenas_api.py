import requests
import re
import json
import os
import io
import urllib


class FreeNASAPI:
    def __init__(self, method, host, port, user, password):
        self.method = method
        self.host = host
        self.user = user
        self.password = password
        self.port = port

    def requests(self, type, url, *payload):
        if type == 'GET':
            req = requests.get(
                '' + self.method + '://' + self.host + ':' + self.port + '/api/v2.0/' + url + '/',
                headers={'Content-Type': 'application/json'},
                auth=( self.user, self.password ),
                verify=False,
                params='limit=100000',
            )

        if type == 'POST':
            req = requests.post(
            '' + self.method + '://' + self.host + ':' + self.port + '/api/v2.0/'+ url + '/',
            headers={'Content-Type': 'application/json'},
            auth=( self.user, self.password ),
            verify=False,
            data=payload[0],
            )

        if type == 'DELETE':
            req = requests.delete(
            '' + self.method + '://' + self.host + ':' + self.port + '/api/v2.0/'+ url + '/',
            headers={'Content-Type': 'application/json'},
            auth=( self.user, self.password ),
            verify=False,
            params='limit=100000',
            )

        return req.status_code, req.text

    def listnetworkconfig(self):
        status, content = self.requests('GET', 'network/configuration')

        data = {}
        data['status'] = str(status)
        data['networkconfig'] = json.loads(content)
        
        return json.dumps(data)

    def listnetworksummary(self):
        status, content = self.requests('GET', 'network/general/summary')

        data = {}
        data['status'] = str(status)
        data['networksummary'] = json.loads(content)
        
        return json.dumps(data)

    def listsystemready(self):
        status, content = self.requests('GET', 'system/ready')

        data = {}
        data['status'] = str(status)
        data['systemready'] = json.loads(content)
        
        return json.dumps(data)

    def listalerts(self):
        status, content = self.requests('GET', 'alert/list')

        data = {}
        data['status'] = str(status)
        data['alerts'] = json.loads(content)
        
        return json.dumps(data)

    def listjails(self):
        status, content = self.requests('GET', 'jail')

        data = {}
        data['status'] = str(status)
        data['jails'] = json.loads(content)
        
        return json.dumps(data)
