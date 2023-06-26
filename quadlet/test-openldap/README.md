# OpenLDAP for Testing

Use this example to provision an OpenLDAP container for testing.
See details [here](https://hub.docker.com/r/rroemhild/test-openldap)

## Jinja Templated Quadlet file
Please note that the provided Quadlet file is a Jinja Template that uses the following optional variables:

- ldap_host_port - The host port to bind the LDAP container port to (default 10389)
- ldaps_host_port - The host port to bind the LDAPS container port to (default 10636)
- wanted_by - WantedBy target for the systemd `Install` section

## Prerequisites
To create the `.container` file from the [test-openldap.container.j2](./test-openldap.container.j2) jinja template you will need to install `j2`

```bash
dnf install -y jq
```

## Usage

### Generate the `.container` file
You may choose the provided [example.json](./example.json) file or create your own

```bash
j2 test-openldap.container.j2 example.json  > test-openldap.container
```
