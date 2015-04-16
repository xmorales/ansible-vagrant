INSTRUCTIONS
============
Kindly get in touch with delivery_fc@tid.es in order to perform this task for you since `delivery` password should
only be kept by SEEN team. This playbook might also leave Ansible traces to the server logs and Nagios alarms will
be raised.

USAGE
=====
This will copy a public key to the user provided among the specified hosts in case it doesn't exist.

```
ap -i enviro/<enviro>/hosts pubkeys.yml -k --vault-password-file=secret.txt -e pub_file=<path/to/key.pub> -e user=foo
```

Use `--limit` to specify the hosts within the environment if you like.
The `--vault-password-file` parameter is required since Ansible loads its whole code in memory.
`-k` will prompt for `delivery` user password before triggering any task.

EXAMPLES
========
```
# Copy id_rsa.pub to all London staging servers for delivery user
ap -i enviro/ldst/hosts pubkeys.yml \
   -k \
   --vault-password-file=secret.txt \
   -e pub_file=/Users/oriolf/.ssh/id_rsa.pub \
   -e user=delivery
```

```
# Copy id_rsa.pub to only Miami production Orejas for foo user
ap -i enviro/mapr/hosts pubkeys.yml \
   -k \
   --vault-password-file=secret.txt \
   -e pub_file=/Users/oriolf/.ssh/id_rsa.pub \
   -e user=foo
   --limit oreja
```

