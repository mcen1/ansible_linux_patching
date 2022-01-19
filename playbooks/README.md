# playbooks - overview
This playbook is modularly designed leveraging roles heavily. The playbook itself is actually quite short and make use of include_role and import_role often. The majority of includes are driven by facts, either gathered from Facter, ansible, or set as part of the playbooks "gather info" tasks.

# playbooks - sections
The playbook is broken into 4 sections:
1. The gather info prepatching steps - get vcenter password, OS level and type, etc
2. The pre-patching steps for a server - take a VM snapshot for rollback in case of a failed patch, turn off services, etc
3. The actual patching of the OS - this section always restarts the server
4. The post-patching steps for a server - turn services back on, verify no open alerts from patching, notification of patch completion, etc

# playbooks - error handling
The playbook includes an error handler that if invoked will generally rollback to a prepatching snapshot and inform appropriate parties of the failure and at what step the server failed.

# playbooks - role inclusion
Above we mentioned that roles do the heavy lifting of the patching playbook which is what allows it to patch many different kinds of servers using the same code. Role inclusion happens 2 different ways - A server has a Facter fact for the role inclusion like custom_admin_ansible_prestep_role (pre-pended in ansible with 'facter_' to denote that it is a Facter generated fact), or as a variable defined in one or more of the group_vars/xxx/main.yml files. These variables do not need to be prepended with facter_ or ansible_, but should only be used with static inventories. The 'All' group_var applies to all servers regardless of static or dynamic inventory and whether they have any other facts.