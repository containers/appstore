# Zerotier One

> This Quadlet requires root privileges to run.

[ZeroTier](https://www.zerotier.com/) is a smart programmable Ethernet switch for planet Earth. It allows all networked devices, VMs, containers, and applications to communicate as if they all reside in the same physical data center or cloud region.

## Usage

Unfortunately, networks cannot be supplied through environment variables. You will need to join nertworks using the following command as root, or with sudo:

`podman exec zerotier-one zerotier-cli join YOUR_NETWORK_ID`

If you are using this in an immutable distro such as silverblue, you can also create a script in `/usr/local/bin` called `zerotier-cli` with the following contents:

```bash
#!/bin/bash
podman exec -it zerotier-one zerotier-cli $@
```

This will "forward" any zerotier-cli commands you run to the container. This script still needs to be ran as root, or with sudo.
