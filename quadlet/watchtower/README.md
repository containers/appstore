# Watchtower

[Watchtower](https://github.com/containrrr/watchtower) provides a container that
monitors other containers for updates. From their GitHub
[README](https://github.com/containrrr/watchtower#readme):

> With watchtower you can update the running version of your containerized app simply by
> pushing a new image to the Docker Hub or your own image registry.

> Watchtower will pull down your new image, gracefully shut down your existing container
> and restart it with the same options that were used when it was deployed initially.
> Run the watchtower container with the following command:

There's also a [blog post](https://major.io/p/podman-quadlet-watchtower/) explaining how to run it as a quadlet with podman on Fedora CoreOS.