# Pihole and Unbound

[Pihole](https://github.com/pi-hole/pi-hole) is a locally hosted dns/url filter and provider.  It can be used for a variety of purposes, but it's main use case is for blocking ads on an entire network and for devices which do not have any in-built method for adblocking.

[Unbound](https://www.nlnetlabs.nl/projects/unbound/about/) is a validating, recursive, caching DNS resolver that allows your local system to identify the path to the intended location on the internet, without having to rely on outside hosted DNS providers like Google or Cloudflare, or your local ISP.

## Installation

To install the Pihole-unbound quadlet to your your root users' systemd services, copy the `pihole-unbound_home.network' 'pihole-unbound_pihole_dnsmasq.volume' 'pihole-unbound_pihole_volume.volume' and 'pihole.container' files to either of the following directories:

This service requires the use of privileged ports below 1024 to operate correctly.  It can either be installed via rootful podman, or you can port forward the necessary ports to a non-rootful version.  Here we are assuming the rootful version.

- /etc/containers/systemd/
- /usr/share/containers/systemd/


## Usage

To start the Ollama and Open WebUI services, you can generate the systemd service files and execute the services:

```bash
$ systemctl daemon-reload
$ systemctl start pihole
```

This will bring up the Pihole and the Unbound services.  You can then access the Pihole service by navigating to `http://192.168.7.8` in your web browser. #Replace this ip with whatever one you chose in your .container file if it differs.