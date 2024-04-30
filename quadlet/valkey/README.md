# Valkey

> This Quadlet can be ran in a rootless container.

[Valkey](https://valkey.io/) is an open source (BSD) high-performance key/value datastore that supports a variety workloads such as caching, message queues, and can act as a primary database. Valkey can run as either a standalone daemon or in a cluster, with options for replication and high availability.

Since this Quadlet is a single container, it is not recommended for production use. For production use, you should run Valkey in a cluster by following the [Valkey documentation](https://valkey.io/docs/).

Valkey does not currently publish a `:latest` or `:stable` tag, so the quadlet contains the hard-coded version `7.2`. If you would like to use a different version, you can modify the image tag inside the `valkey.container` file.

## Usage

This Quadlet requires no special permissions to run.

To setup the Valkey Quadlet, you can paste the `valkey.container` and `valkey.volume` files into any of the following directories:

- `$HOME/.config/containers/systemd/`
- `/etc/containers/systemd/users/`

You can start the Valkey server with the following command, as a regular user:

```bash
$ systemctl --user daemon-reload
$ systemctl --user start valkey.service
```

You are now ready to connect your application to the Valkey server at localhost:6379.
