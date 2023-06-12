#!/bin/sh
# Example script to figure out all containers running on your system

# This script looks for all `conmon` (container monitor) processes running on
# the host. It then runs a shell executing `podman ps $ARG` in each one of the
# user sessions listing the containers that are currently running.

logins() {
    ps --no-heading -C conmon -o user | sort -u
}

podman_ps_user() {
    name=$1
    shift
    args="$@"
    machinectl shell --quiet $name@ /bin/sh -c "/usr/bin/echo User: $name; /usr/bin/podman ps $args"
}

if [ "$EUID" -ne 0 ];then
    echo "The $0 script must be executaed as root"
    exit 1
fi

for name in $(logins); do podman_ps_user $name "$@"; done
