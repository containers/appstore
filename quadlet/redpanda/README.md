# Redpanda Data Streaming Development Cluster

Use this example to provision a [Redpanda](https://redpanda.com/) single-node cluster with the [Redpanda Console](https://redpanda.com/redpanda-console-kafka-ui) container configured to manage the cluster.

Redpanda is an open source streaming platform built with Go.  It is designed to be a Kafka API compatible alternative to Kafka, with the goal of being faster and more efficient.


## Usage

This example expects to be ran as a non-root user without the need for any special privileges.  It is not designed to be used in a production environment as there is no access control, high availability or any sort of encryption.  Please refer to the [Redpanda documentation](https://docs.redpanda.com/current/home/) for more information on how to properly secure your cluster.

To run this example, you can move the files in this directory to your `~/.config/containers/systemd` directory, and run the following commands:

```bash
$ systemctl --user daemon-reload
$ systemctl --user start redpanda-console.service
$ xdg-open http://localhost:8080
```

There are no credentials, and all data is stored in `redpanda-data` Podman volume owned by your user.
Since running the console isn't a requirement for the cluster, these have been split into separate units without an explicit dependency from the cluster to the console.  When starting the console however, it will bring the cluster up if it is not already running.

To connect to the Redpanda cluster, you can run the following commands with Python 3.11 installed:

```bash
$ cd sample-app
$ pip install -r requirements.txt
```

And start the app in two separate terminals:

```bash
$ python app.py
```
