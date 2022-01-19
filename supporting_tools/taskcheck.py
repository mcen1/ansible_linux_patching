#!/usr/bin/env python3

import signal
import atexit
import argparse
import sys
import time
import ssl
import os
import datetime
import json
from pyVmomi import vim, vmodl
from pyVim import connect, task
from pyVim.connect import Disconnect, SmartConnect, GetSi
import time
import socket

socket.setdefaulttimeout(15)

inputs = {
          'vcenter_password': sys.argv[3],
          'vcenter_user': VMWAREUSER,
          }

def get_obj(content, vimtype, name):
    """
     Get the vsphere object associated with a given text name
    """    
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj

'''
This will pull all tasks on the "first page" of the vm tasks, and brings back lastest task.
'''
def checkTask(vmn,content):
    taskManager = content.taskManager
    specByuser = vim.TaskFilterSpec()
    specByuser.entity = vim.TaskFilterSpec.ByEntity(entity=vmn,recursion='all')
    #print (specByuser.entity)
    tasks = taskManager.CreateCollectorForTasks(specByuser)
    
    #print(tasks)
    tasks.ResetCollector()
    alltasks = tasks.ReadNextTasks(10)[0]
    
    #print (alltasks.completeTime)
    #print(alltasks)
    
    if alltasks.completeTime != None:
        print("This server is not busy.")
        busybee = False
    else:
        #print("This server is busy.")
        busybee = True
        
    return busybee
        
'''
Main connector to vsphere and continuously checks task status for 5 minutes every 10 seconds.
'''
def main(vcenter, servername):

    si = None
    busycheck = True
    try:
        #print ("Trying to connect to VCENTER SERVER . . .")
        
        context = None
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.verify_mode = ssl.CERT_NONE
        
        si = connect.Connect(vcenter, 443, inputs['vcenter_user'], inputs['vcenter_password'],sslContext=context)

    except IOError as e:
        pass
        atexit.register(Disconnect, si)

    #print ("Connected to VCENTER SERVER !")
    
    content = si.RetrieveContent()
    vmn = get_obj(content, [vim.VirtualMachine], servername)
    
    # check for 5 minutes
    t_end = time.time() + 60 * 5
    
    while time.time() < t_end:
        if busycheck == True:
            #print("checking status of last task...")
            busycheck = checkTask(vmn, content)
            if busycheck == False:
                break
            time.sleep(10)
        else:
            break
    
    if busycheck == True:
        print("Busy. doing CIA tasks.")
        sys.exit(1)


vcenter = sys.argv[1]
servername = sys.argv[2]

main(vcenter, servername)

