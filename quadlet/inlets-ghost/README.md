# GHost exposed using Inlets Client

Use this example, which was used in the [blog post](https://inlets.dev/blog/2023/10/03/client-quadlet.html),
to provision a [GHost](https://ghost.org/) server locally and expose it to the internet using [Inlets](https://inlets.dev/)

## Prerequisites

In order to generate the actual Kubernetes YAML files, you will need to install `j2`

```bash
dnf install -y jq
```

## Inlets License Secret

### Mandatory Variables
- inlets_license - Inlets license string

### Create the secret

Create a data file based on the provided [example-license.yml](./example-license.yml) file or create your own
and use the provided [inlets-license.yml.j2](./inlets-license.yml.j2) jinja template to generate the `inlets-license` secret

```bash
j2 inlets-license.yml.j2 example-license.yml  | podman kube play -
```

## Inlets Token Secret

### Mandatory Variables
- inlets_token - The client auth token to preset to the Inlets server

### Create the secret

Create a data file based on the provided [example-token.yml](./example-token.yml) file or create your own
and use the provided [inlets-token.yml.j2](./inlets-token.yml.j2) jinja template to generate the `inlets-token` secret

```bash
j2 inlets-token.yml.j2 example-token.yml  | podman kube play -
```

## Kubernetes Pod YAML file

### Mandatory Variables
- inlets_server_ip - IP address of the Inlets server
- inlets_server_domain - FQDN of the Inlets server

### Optional Variables
- inlets_version - Inlets container image version (default `0.9.21`)

### Create the Kubernetes YAML file

Create a data file based on the provided [example-pod.yml](./example-pod.yml) file or create your own
and use the provided [inlets-ghost.yml.j2](./inlets-ghost.yml.j2) jinja template to generate the `inlets-ghost.yml` file

```bash
j2 inlets-ghost.yml.j2 example-pod.yml  > inlets-ghost.yml
```

## Setup the service

Copy the generated Kubernetes YAML and the [inlets-ghost.kube](./inlets-ghost.kube) files to the Quadlet directory:
- For rootful service: `/etc/containers/systemd`
- For rootless service: `~/.config/containers/systemd/`

Reload the systemd daemon
- For rootful service: `sudo systemctl daemon-reload`
- For rootless service: `systemctl --user daemon-reload`

Start the service
- For rootful service: `sudo systemctl start inlets-ghost`
- For rootless service: `systemctl --user start inlets-ghost`
