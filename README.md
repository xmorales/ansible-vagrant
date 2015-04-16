Ansible + Vagrant
=================

Basic and Advanced examples using Ansible and Vagrant.

# Requirements
Tested with:
* Vagrant 1.7.2
* VirtualBox 4.3.26
* Ansible 1.9.0.1

# Setting up your working tree
```
$ git clone git@pdihub.hi.inet:oriolf/ansible.git
$ vagrant plugin install landrush
$ vagrant box add chef/centos-6.5 --provider virtualbox
```

(optional)
edit ~/.ssh/config
```
# For vagrant virtual machines
Host 172.16.1.* *.vagrant.dev
StrictHostKeyChecking no
ServerAliveInterval 60
UserKnownHostsFile=/dev/null
User vagrant
LogLevel ERROR
```
`$ vagrant up`

# References:

* [https://github.com/phinze/landrush](Vagrant DNS plugin)
* [Sublime Text 2/3 Ansible Language Pack](https://github.com/clifford-github/sublime-ansible)
* [Ansible Examples](https://github.com/ansible/ansible-examples)
* [Apache Rewrite Rules](http://thornelabs.net/2014/06/02/manage-apache-virtualhosts-and-mod-rewrite-rules-with-ansible.html)
* [Jinja2 Template Examples](https://servercheck.in/blog/apache-virtualhosts-with-ansible-and-jinja2)
