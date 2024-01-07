# Syncthing
Inspired by the following guide: <https://github.com/MMarco94/linux-guides/blob/main/immutable-os/syncthing.md>

# Items to take note of:

## Networking
You can achieve networking for the container in the following 2 ways

1. Setting Network=Host (Line 33)
My preferred method as it works faster when my devices are on a local network

2. Setting Published Ports (Lines 17-20)
Performance is poorer but achieves network isolation from host

## Container Privileges
- This container is expected to run as **non-root**
- When initialising the systemd service, use `systemctl --user`

## Volumes
- Config Volume: As mentioned in the guide above, you can use ~/.config/syncthing
- Data Volumes: For every folder you want to add in Syncthing you must create a new volume and add the volume to the `.container` file:
For ~/Sync add it as `Volume=%h/Sync:/var/syncthing/sync:Z`

**Please create the above folders in your system before initialising the container, if not the service will error out**

