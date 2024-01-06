# Syncthing
Inspired by the following guide: <https://github.com/MMarco94/linux-guides/blob/main/immutable-os/syncthing.md>

# Items to take note of:

## Container Privileges
- This container is expected to run as **non-root**
- When initialising the systemd service, use `systemctl --usee`

## Volumes
- Config Volume: As mentioned in the guide above, you can use ~/.config/syncthing
- Data Volumes: For every folder you want to add in Syncthing you must create a new volume and add the volume to the `.container` file:
For ~/Sync add it as `Volume=%h/Sync:/var/syncthing/sync:Z`

**Please create the above folders in your system before initialising the container, if not the service will error out**

