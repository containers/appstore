# podman_ps
Example script to list all containers running on your system, by any user.

This script looks for all `conmon` (container monitor) processes running on
the host. It then runs a shell executing `podman ps $ARG` in each one of the
user sessions listing the containers that are currently running.

* NOTE: This script is not a security mechanism. It only gathers containers at the time of execution. Monitoring what users are doing on your system you is better accomplished via the audit subsystem. This script can easily be thwarted by hostile users. Simply running a container with `podman --root ~/myroot ...` creates a container that this script does not list.

There could be potential side effects of this tool like:

 * Mounting NFS home directories
 * Create $HOME/.containers-or-config-or-something if there wasn't one.
 * Affect accounting: the machinectl session shows up under last.
 * Potentially side effects of accounts with different login shells, or strange environments
