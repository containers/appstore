# PostgreSQL

Use this example to provision a PostgreSQL container

## Jinja Templated Quadlet file
Please note that the provided Quadlet file is a Jinja Template that uses the following variables:

### Mandatory Variables
- image_tag - The tag for the [PostgreSQL container](https://hub.docker.com/_/postgres)

### Optional Variables
- host_port - The host port to bind the container port to (default 5432)
- postgresql_uid - UID for the PostgreSQL user used for UID and GID mapping
- wanted_by - WantedBy target for the systemd `Install` section

## Prerequisites
To create the `postgresql.container` file from the [postgresql.container.j2](./postgresql.container.j2) jinja template you will need to install `j2`

```bash
dnf install -y jq
```

## Usage

### Generate the `.container` file
You may choose the provided [example.json](./example.json) file or create your own

```bash
j2 postgresql.container.j2 example.json  > postgresql.container
```

### Set Environment Variables
You may add PostgreSQL environment variables using the [postgresql.env](./postgresql.env)

### Generate the Secret for the PostgreSQL admin
On the target machine make sure to create the secret holding the admin password

```bash
cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-20} | head -n 1 > pass.file
podman secret create postgresql_admin_password_secret pass.file
```
