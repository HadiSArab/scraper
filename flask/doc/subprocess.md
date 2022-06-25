
import subprocess

# just do command and show output in terminal
subprocess.run('ls')

# store result in variable "a" but not output, just args and faults
a = subprocess.run('ls')

# store output of command in variable "b" . this command return full detail of output and can be usely
b = subprocess.run('ls',capture_output=True)

# convert output to string from binary 
c= subprocess.run('ls',capture_output=True, text=True)

# print just output without result code 
print ('c: ',c.stdout)

# subprocess.call()
>>>>print(subprocess.call('ls'))
ali.json  doc  first.json  Pipfile  Pipfile.lock  __pycache__  req.py  salam  second.json  subpros.py  templates  third.json  web.py
0
# subprocess.run()
>>>>print(subprocess.run('ls'))
ali.json  doc  first.json  Pipfile  Pipfile.lock  __pycache__  req.py  salam  second.json  subpros.py  templates  third.json  web.py
CompletedProcess(args='ls', returncode=0)

# subprocess.getoutput()
>>>>print(subprocess.getoutput('ls'))
ali.json
doc
first.json
Pipfile
Pipfile.lock
__pycache__
req.py
salam
second.json
subpros.py
templates
third.json
web.py
python@ubuntu:~/projects/flask$ 

# check_call() return full errors text if exists
>>>>subprocess.check_call()

# check_output can store full errors text in variables for more uses
>>>>subprocess.check_output()

# 
>>>>subprocess.popen()

#
>>>>subprocess.communicate()


