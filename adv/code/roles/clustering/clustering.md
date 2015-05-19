# Summary
Clustering with pacemaker and corosync. This will enable communication between servers through SSH automatically and will create a group of `n` nodes. Where `n` will be your `hosts` definition in the main playbook.

# Explanation
I've previously generated a SSH-RSA key and copied both private and public in `certs.yml` file which is encrypted. This very same key will be copied among your defined `hosts` so that they will see to each other.

There is also a `config` ssh file to load the key automatically since differs from default `id_rsa`.

After required software is installed, playbook will start copying our cluster configuration files.

Most interesting file would be `cluster.conf` which states each hostname and its id by using Jinja2 filters and some Python plugins.

It will create a cluster configuration file with only running hosts in the current group

We also set `no_quorum` only if the cluster is less than 5 nodes since we actually want to run at least 1 server given the small amount of this cluster - webpage always up!

# Hints
If you only want to run `clustering` role and skip certain other roles you can help yourself using tags. This will not run any `glusterfs` task

After that, `httpd` role is installing Apache and setting up Apache and a failover IP as resources.

`$ ansible-playbook` -i enviro/vagrant/hosts lamp.yml --vault-password-file=secret.txt -vv --skip-tags=glusterfs`

You can bring up more machines and run again this playbook. Nodes will be appended to cluster with Apache
