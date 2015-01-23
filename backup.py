import tarfile
import configparser
import os
import sys

def check_files(file_names):
    failed = []
    for name in file_names:
        if not os.path.exists(name):
           failed.append(name)
    
    for failure in failed:
        print('%s - failed' % failure)
    return failed
          
def backup(file_names, out_file):
    tar = tarfile.open(out_file, 'w:gz')
    for name in file_names:
       tar.add(name, name.split('/').pop())
    tar.close()
    
config = configparser.ConfigParser()
config.read('backup.config')
paths = config.items('paths')
names = []

for key, path in paths:
    names.append(path)
    
failed = check_files(names)
if len(failed) == 0:
    backup(names, sys.argv[1])
else:
    print("Please fix config file")
