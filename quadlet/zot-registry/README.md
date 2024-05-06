# Zot Registry

[Zot Registry](https://zotregistry.dev/) is an open-source CNCF sandbox project which allows you to store and retrieve OCI images. It is a lightweight, but powerful alternative to the Docker registry which has built-in features such as pull-through cache, image scanning and signing.

This quadlet runs Zot Registry as a rootless container, and mounts a volume to store the OCI images. It does not contain any authentication, so is not recommended for production use.

## Installation

To install the Zot Registry quadlet to your user's systemd services, copy the `zot-registry.container`, `zot-registry.volume` and `config.yaml` files to either of the following directories:

- `$HOME/.config/containers/systemd/`
- `/etc/containers/systemd/users/`

Once the files are in place, you can generate the systemd service files and execute the service:

```bash
$ systemctl --user daemon-reload
$ systemctl --user start zot-registry

# Optional: enable the service to start on boot
$ systemctl --user enable zot-registry
```

## Usage

The configuration file `config.yaml` contains all the necessary configuration for the registry.  This includes pull-through cache for all containers with the `ghcr.io/containers/` prefix.  This can be updated to include other prefixes as required.

Since this registry does not use HTTPS, you will need to add a configuration file to `/etc/containers/registries.conf.d/zot-registry.conf`.  Otherwise you will receive an error when trying to pull or push images:

```bash
[[registry]]
location = "localhost:5000"
insecure = true
```

Once you have added that, you are able to push images to the registry using the `podman` command:

```bash
$ podman pull quay.io/fedora/fedora:latest
$ podman tag quay.io/fedora/fedora:latest localhost:5000/my-library/fedora:latest
$ podman push localhost:5000/my-library/fedora:latest
```

You can then pull the image from the registry or use it as part of a `Containerfile` (`Dockerfile`):

```bash
$ podman pull localhost:5000/my-library/fedora:latest
$ cat <<EOF > Containerfile
FROM localhost:5000/my-library/fedora:latest
CMD echo "Hello, World!"
EOF
```
