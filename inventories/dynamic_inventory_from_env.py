#!/usr/bin/env python3

# Gets list of servers from environment variable ANSSERVERS and puts it into a format
# Ansible understands.

import os
import sys

try:
  myhosts=str(os.environ['ANSSERVERS']).split()
except Exception as e:
  print ("ERROR retrieving environment variable! ANSSERVERS is unset. ")
  sys.exit(66)
mymeta={"hostvars":{}}
# metadata for special port connections and anything else you can imagine
mymetatmp = eval(open("ansible_resources/inventories/dynamic_inventory_meta.dict").read())
for hosta in myhosts:
  if hosta in mymetatmp["hostvars"]:
    mymeta["hostvars"][hosta]=mymetatmp["hostvars"][hosta]
    continue
mystuff={"servers":{"hosts":myhosts},"_meta":mymeta}
print(mystuff)
