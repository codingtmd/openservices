#!/usr/bin/python
# Filename: compile.py
# Example:
#   python compile.py -s ~/openservices/services/csvparser/csvparser.thrift -l php:server -c csharp


import os,sys, getopt,subprocess, contextmanager

input_source = "";
client_languages = "";
server_language = "";
opts, args = getopt.getopt(sys.argv[1:], "s:c:l:")
for op, value in opts:
    if op == "-s":
        input_source = value
    elif op == "-c":
        client_languages = value
    elif op == "-l":
        server_language = value

if (input_source == "") or (client_languages == "") or (server_language =="") :
    print "error parameter"
    sys.exit()


print "start to process services:", input_source
print "server_language:", server_language
print "client_languages", client_languages

# compile thrift code for server side
thrift_path, thrift_name = os.path.split(input_source)
print "delete old code "
   # enter the directory like this:
with contextmanager.cd(thrift_path):
   # we are in ~/Library
   command = "rm -rf gen-*"
   print "execute:", command
   subprocess.call(command, shell=True)

# outside the context manager we are back wherever we started.


# compile thrift code for server side
thrift_path, thrift_name = os.path.split(input_source)
print "start to compile server side ", thrift_name, "under", thrift_path
   # enter the directory like this:
with contextmanager.cd(thrift_path):
   # we are in ~/Library
   command = "thrift --gen " + server_language + " " + thrift_name
   print "execute:", command
   subprocess.call(command, shell=True)

# outside the context manager we are back wherever we started.

# compile thrift code for client side

clients = client_languages.split(',');

for client in clients:
    print 'compile ', client
    with contextmanager.cd(thrift_path):
       # we are in ~/Library
       command = "thrift --gen " + client + " " + thrift_name
       print "execute:", command
       subprocess.call(command, shell=True)

# copy server host class to the package
if (server_language == "php:server") :
    # we are in ~/Library
    command = "cp ./phptemplate/* " + thrift_path
    print "execute:", command
    subprocess.call(command, shell=True)


print "done"
