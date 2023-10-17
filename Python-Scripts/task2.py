import sys
import os
import numpy
import datetime
import tarfile

# Backup
#   Archive as a “tarball” (*.tar.gz file) all the files in your home directory tree (/home/your-name) that have been modified in the last 24 hours. Hint: use find.

pathoffiles=sys.argv[1]

now = datetime.datetime.now()

hours24mod = now - datetime.timedelta(hours=24)

modfilenames = []

for root, dirs, files in os.walk(pathoffiles):
    for file in files:

        file_path = os.path.join(root, file)
        
        modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        
        if modification_time >= hours24mod:
            modfilenames.append(file_path)

with tarfile.open("hours24mod.tar", 'w') as tar:
    for file in modfilenames:
        # Add each file to the archive with its name
        tar.add(file, arcname=file.split('/')[-1])

print(f'hours24mod.tar archive created for the files editied in last 24 hours')
