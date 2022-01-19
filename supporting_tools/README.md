# supporting_tools

The supporting tools are external scripts used to extend the patching process with mechanisms that are not built-in to Ansible or not easily achievable using Ansible tooling. This playbook strives to use native Ansible modules wherever possible, though.

- bootcheck.sh: This script checks for available space on the /boot partition of less than 90,000 KB. This information is used to resolve an issue with small boot partitions not having enough space to hold more than a single kernel and associated libraries.
- getcmdbinfo.py: This script contacts your companys CMDB (assuming one exists) and pulls variables used throughout this playbook. This script accepts a server name and field to query (like hostname or something). You must provide the username and password for the CMDB to the script as well. If you do not have a CMDB we suggest you get one, but the playbook will run without it.
- id_rsa: The public SSH key for the rancher user. Only used if patching a rancher cluster running ROS.
- lilboots.sh: This script handles removing old kernels in the case of a small /boot partition with less than 90,000 KB free space (there is a specific use case for this script that requires it be run before the next script in this list - the generic remove_old_kernels.sh script).
- remove_old_kernels.sh: Removes all kernels on the /boot partition older than the most recent.
- taskcheck.py: This script queries the vm provider (vmware, openstack, etc) and checks to see if the VM that is about to be patched is currently running any tasks like an HA failover, snapshot, etc. If one of these tasks are in the middle of running when the server is being patched, bad things can happen. This is a safety check. You'll need to provide the VM provider server address, and a valid username and password.
- kubeconfigs: For kubernetes cluster patching support. This allows kubernetes clusters to be patched using valid kubectl commands and user authentication.
