#!/usr/bin/env python3
import requests
import json
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def getCMDBField(servername,myfield):
  go=True
  cmdburl='https://cmdb.company.com/rest/'
  json_data = {
                  "operation": "core/get",
                  "class": "VirtualMachine",
                  "key": "SELECT VirtualMachine WHERE status != 'decommissioned' AND name = '"+servername+"'",
                   "output_fields": myfield
                }
  encoded_data = json.dumps(json_data)
  r = requests.post(cmdburl, verify=False, data={'auth_user': USERNAME, 'auth_pwd': PASSWORD, 'json_data': encoded_data})
  result = json.loads(r.text)
  try:
    for res in result["objects"]:
      myid=result["objects"][res]["fields"][myfield]
  except Exception as e:
    print(e)
    print(result)
    go=False
    sys.exit(68)
  if len(myid)<2:
    sys.exit(66)
  return myid


myserver=str(sys.argv[1])
myfield=str(sys.argv[2])

print(getCMDBField(myserver,myfield))
