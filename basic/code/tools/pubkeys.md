USAGE
=====
This will copy a public key to the user provided among the specified hosts in case it doesn't exist.

```
ap -i enviro/<enviro>/hosts pubkeys.yml -k --vault-password-file=secret.txt -e pub_file=<path/to/key.pub> -e user=foo
```

Use `--limit` to specify the hosts within the environment if you like.
The `--vault-password-file` parameter is required since Ansible loads its whole code in memory.
`-k` will prompt for `vagrant` user password before triggering any task.

EXAMPLES
========
```
# Copy id_rsa.pub to all London staging servers for vagrant user
ap -i enviro/vagrant/hosts pubkeys.yml \
   -k \
   --vault-password-file=secret.txt \
   -e pub_file=/Users/oriolf/.ssh/id_rsa.pub \
   -e user=vagrant
```

```
# Copy id_rsa.pub to only Miami production Orejas for foo user
ap -i enviro/vagrant/hosts pubkeys.yml \
   -k \
   --vault-password-file=secret.txt \
   -e pub_file=/Users/oriolf/.ssh/id_rsa.pub \
   -e user=foo
   --limit db
```

