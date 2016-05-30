#!/usr/bin/python
# Filename: deploy.py
# Example:
#   python deploy.py -p ~/openservices/services -d 100.100.100.100 -n csvparser


import os,sys, getopt,subprocess, contextmanager

dest = "";
source_path= "";
service = "";
opts, args = getopt.getopt(sys.argv[1:], "p:d:n:")
for op, value in opts:
    if op == "-d":
        dest = value
    elif op == "-p":
        source_path = value
    elif op == "-n" :
        service = value

if (dest == "") or (source_path=="") or (service == ""):
    print "error parameter"
    sys.exit()

print "delete the old code"

command = "ssh  " + dest  + " rm -rf /var/www/html/" + service
print "execute:", command
subprocess.call(command, shell=True)

print "start to deploy services:", dest

command = "scp -r " + source_path + "/" + service + "/ " + dest + ":/var/www/html"
print "execute:", command

subprocess.call(command, shell=True)

print "done"
