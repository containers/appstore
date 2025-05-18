# Bluesky PDS

Use this example to provision a [Bluesky PDS](https://github.com/bluesky-social/pds) server.

[ATProtocol PDS (Personal Data Server)](https://atproto.com/guides/glossary#pds-personal-data-server):
> A PDS, or Personal Data Server, is a server that hosts a user. A PDS will always store the user's data repo and signing keys. It may also assign the user a handle and a DID. Many PDSes will host multiple users.

## Example Notes

- hosts pds server on a subdomain while users use root domain.
- secret environment variables stored in podman secrets
- rootless containers via automatic namespace
- selinux and chown relabeling
- No `pdsadmin`. See note below

For additional environment variable configurations, see [atproto sources](https://github.com/bluesky-social/atproto).

## Usage

- Configure DNS for your domain: see [configure-dns-for-your-domain](https://github.com/bluesky-social/pds/tree/main?tab=readme-ov-file#configure-dns-for-your-domain)
- Replace `example.com` with your domain in `pds.container` and `Caddyfile`
- Generate `pds_jwt`, `pds_admin`, and `pds_rotate` secrets
- Optionally setup SMTP environment variables `PDS_EMAIL_FROM_ADDRESS` and `PDS_EMAIL_SMTP_URL` in `pds.container`: see [setting-up-smtp](https://github.com/bluesky-social/pds/tree/main?tab=readme-ov-file#setting-up-smtp)
  - SMTP is required for the users take certain actions on their account such as verify it and reset passwords.

```sh
printf "$(openssl rand --hex 16)" | podman secret create pds_admin -
printf "$(openssl rand --hex 16)" | podman secret create pds_jwt -
printf "$(openssl ecparam --name secp256k1 --genkey --noout --outform DER | tail --bytes=+8 | head --bytes=32 | xxd --plain --cols 32)" | podman secret create pds_rotate -
```

## Missing pdsadmin?

`pdsadmin` tools are incompatible outside of [installer.sh](https://github.com/bluesky-social/pds/blob/main/installer.sh) based deployments. However they not needed as the PDS is controlled through AT protocol API calls

- See [goat](https://github.com/bluesky-social/indigo/tree/main/cmd/goat) for an AT protocol CLI tool
- See [pdsadmin subfolder](https://github.com/bluesky-social/pds/tree/f07a20e7e8e3b60eb40fbf735cabda8cd6a0e9d2/pdsadmin) for example curl commands

## Caddy Ports

The provided Caddyfile needs to the following ports:

- 80: HTTP-01 challenge and HTTP to HTTPS redirects
- 443: HTTPS
- 443/udp: HTTP/3 (optional if not using HTTP/3)
