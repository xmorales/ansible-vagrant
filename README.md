Ansible + Vagrant
=================

Basic and Advanced examples using Ansible and Vagrant.

# Audience
This project aims education as fundamental with a nonprofit goal. If you'd like to learn how Ansible fits with Vagrant you might find useful code in here.

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


# Techdebt

- [X] provision machines without disk
- [ ] inventory in json dump
- [X] dynamic inventory
- [X] glusterfs run tasks on one node only
- [X] glusterfs manual installation
- [ ] glusterfs peer run only on slaves
- [ ] httpd cluster
- [ ] mysql cluster


# References:

* [Vagrant DNS plugin](https://github.com/phinze/landrush)
* [Sublime Text 2/3 Ansible Language Pack](https://github.com/clifford-github/sublime-ansible)
* [Ansible Examples](https://github.com/ansible/ansible-examples)
* [Ansible modules extra](https://github.com/ansible/ansible-modules-extras)
* [Apache Rewrite Rules](http://thornelabs.net/2014/06/02/manage-apache-virtualhosts-and-mod-rewrite-rules-with-ansible.html)
* [Jinja2 Template Examples](https://servercheck.in/blog/apache-virtualhosts-with-ansible-and-jinja2)
