Ansible + Vagrant
=================

# Requirements
Vagrant 1.7.2
VBox 4.3.26
Ansible 1.9.0.1



```
$ vagrant plugin install landrush
$ vagrant box add chef/centos-6.5 --provider virtualbox
```
edit Vagrantfile
edit ~/.ssh/config
```
# For vagrant virtual machines
Host 172.16.1.* *.vagrant.dev
StrictHostKeyChecking no
ServerAliveInterval 60
UserKnownHostsFile=/dev/null
User vagrant
LogLevel ERROR
$ vagrant up
```


References:

[https://github.com/phinze/landrush](Vagrant DNS plugin)
