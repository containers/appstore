# Splunk

Use this example to provision a Splunk Enterprise container.

For further details see the Splunk [Documentation](https://splunk.github.io/docker-splunk/)

## Prerequisites

The service gets the admin password from an already existing podman secret named `splunk-admin-password`.

To create it run:
```
printf <Admin Password> | podman secret create splunk-admin-password -
```

## Usage

The Quadlet is configured to publish a high order port. So, it can also be used as a user Quadlet

- Copy the files [splunk.container](./splunk.container) and [splunk.volume](./splunk.volume) to the Quadlet directory
- Reload the systemd daemon
- Start the splunk service
- Browse to http://localhost:8000
