#!/bin/bash

# Get a list of all volumes
volumes=$(podman volume ls -q)
#get timestamp for unique filename
timestamp=$(date +"%Y%m%d%H%M%S")

# Temp directory for tar vols
mkdir temp_podman_backup_${timestamp}

# Pause all running containers
echo "Pausing containers for backup"
podman pause --all

# Iterate over the volumes
for volume in $volumes
do
#backup the listed vols
    echo "Backing up ${volume}..."
    podman volume export ${volume} --output ./temp_podman_backup_${timestamp}/${volume}.tar
    # Check if the podman volume export was successful
    if [ $? -ne 0 ]; then
        echo "An error occurred while exporting podman volume ${volume}"
        exit 1
    fi
done

# Unpause all paused containers
echo "Resuming containers"
podman unpause --all

# Archive and compress all .tar files that do not match the pattern podmanbackup_*.tar.gz
echo "Combining volume archives into compressed tar..."
cd temp_podman_backup_${timestamp}
tar cvzf ../podmanbackup_${timestamp}.tar.gz --exclude='podmanbackup_*.tar.gz'  *.tar

# Check if the tar command was successful
if [ $? -eq 0 ]; then
    # If the tar command was successful, remove the .tar files that do not match the pattern podmanbackup_*.tar.gz
    echo "Archiving successful, removing individual .tar files..."
    cd ..
    rm -rf temp_podman_backup_${timestamp}
else
    # If the tar command failed, print an error message
    echo "An error occurred during archiving, no files have been deleted."
    exit 1
fi

# Remove .tar.gz files older than a month
echo "Removing .tar.gz files older than a month..."
find . -maxdepth 1 -type f -name "*.tar.gz" -mtime +30 -exec rm -f {} \;

# Check if the old files deletion was successful
if [ $? -ne 0 ]; then
    echo "An error occurred while deleting old .tar.gz files."
    exit 1
fi

echo "Backup Complete"
exit 0