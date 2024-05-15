# Localstack

[Localstack](https://www.localstack.cloud/) is a service which allows you to emulate AWS services locally.  Some of the services are free and open-source, while others require a license. Some of the notable services which are open-source are S3, DynamoDB and Lambda.

This quadlet runs Localstack as a rootless container, and mounts a volume to store the data.  It also mounts the Podman socket to allow the container to start other containers.  This is a requirement for running Lambda functions.

## Installation

To install the Localstack quadlet to your user's systemd services, copy the `localstack.container` and `localstack.volume` files to any of the following directories:

- `$HOME/.config/containers/systemd/`
- `/etc/containers/systemd/users/`

Once the files are in place, you can generate the systemd service files and execute the service:

```bash
$ systemctl --user daemon-reload
$ systemctl --user start localstack
```

You are then able to call out to the local services using the AWS CLI or SDKs by pointing towards the localstack endpoint.

```bash
$ aws --endpoint-url=http://localhost:4566 s3 mb s3://mybucket
$ aws --endpoint-url=http://localhost:4566 s3 ls
```
