# Minio + Prometheus

Use this example to provision a [Minio](https://min.io/) container with [Prometheus](https://prometheus.io/) metrics enabled.

Minio is an open source S3 compatible object storage server which allows you to store objects on your filesystem and interact with them as if they were stored on S3.


## Usage

This example expects to be ran as a non-root user without the need for any special privileges.  It is not designed to be used in a production environment as credentials are hard-coded and stored in plain text, without any sort of encryption.  Please refer to the [Minio documentation](https://min.io/docs/minio/container/index.html) for more information on how to properly secure your Minio server.

To run this example, you can move the files in this directory to your `~/.config/containers/systemd` directory, and run the following commands:

```bash
$ systemctl --user daemon-reload
$ systemctl --user start prometheus.service
$ systemctl --user start minio.service
$ xdg-open http://localhost:9001
```

The default credentials are `admin:password` and all data is stored in `$HOME/.local/share/minio-data`.

To interact with the Minio server using the [AWS CLI](https://aws.amazon.com/cli/), you must first login to the site and create an access key.  After you have created the access key, run the following command to configure the AWS CLI with your generated credentials:

```bash
$ aws configure --profile minio
AWS Access Key ID [None]: XL2HKL1bkDxeIEXAMPLE
AWS Secret Access Key [None]: MCQNis0YSeFnQ0qgEZEheuqFeYJLJpxBSEXAMPLE
Default region name [None]: 
Default output format [None]:
```

Finally, you can interact with the Minio server using the AWS CLI:

```bash
$ export AWS_PROFILE=minio
$ aws --endpoint-url http://localhost:9000 s3 ls
$ aws --endpoint-url http://localhost:9000 s3 mb s3://test-bucket
$ aws --endpoint-url http://localhost:9000 s3 cp /etc/os-release s3://test-bucket
$ aws --endpoint-url http://localhost:9000 s3 ls s3://test-bucket
```
