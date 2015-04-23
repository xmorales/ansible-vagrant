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
$ git clone https://github.com/wefner/ansible-vagrant.git
$ cd ansible-vagrant/
$ vagrant plugin install landrush
$ vagrant plugin install vagrant-host-shell
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

## Pre-steps

### Deployment host
* Install ansible

If you are running on OSX, you can easily install Ansible by typing

```sudo pip install ansible```

Beware you'll need [sshpass](http://sourceforge.net/projects/sshpass) installed. You can install it with brew or macports too.

```
./configure
make
sudo make install
```

After that, you can just clone this repo and run the first command.

### Destination host
* Make sure your destination machine has a `vagrant` user
* Distribute credentials to the machine. Suggested way of action would be to execute
`ssh-copy-id vagrant@<host>`
> You can define this before running `vagrant up` Vagrant
	* If you do not want to copy the your private key, a password will be prompted.
* Verify you can connect to that machine without a password
* Make sure `vagrant` user can execute root commands with `sudo` and that they have the
`!requiretty` flag activated
(probably by making sure the `vagrant` user is in the `wheels` group and then making sure
that `/etc/sudoers` has uncommented the line about wheel group users being able to execute
commands like in `%wheel ALL=NOPASSWD: ALL !requiretty`).
	* If there's no RSA authentication, you should provide `-K` option to ask for sudo password.

### Generating the secret.txt file
Issue the following command
```
echo PASSWORD > secret.txt
```
on the execution directory (usually, <tt>code</tt>). Replace PASSWORD with the vault password.
I'll use `vagrant` as password in this repository. It's recommended you play with `.gitignore` so that
this file is not commited.

### Dry-run Mode to show differences

In order to check all changes done in any configuration file (glusterfs, httpd, nginx...) of a new version we can use `--check --diff`. This check mode is just a simulation, it will not make any changes on remote systems and thanks to --diff argument if any templated files on the remote system are changed, the ansible-playbook CLI will report back the textual changes made to the file. It is important to use `--tags configuration` to obtain the expected result.
> Note that `shell` module will not be dry-run resulting in that task will be skipped.

Settings hierarchy
==================

Settings hold the real values that will be set in the templates.
If multiple variables of the same name are defined in different places, they win in a certain order, which is:

* -e variables always win
* then comes "most everything else"
* then comes variables defined in inventory
* then comes facts discovered about a system
* then "role defaults", which are the most "defaulty" and lose in priority to everything.

Roles
=====

There are many roles under a playbook. Each role will have the following structure. Let's have a look at this example

PATH=`code/roles/role1/`

You can always append more folders and get a different structure inside every main folder to keep your code organized.
These are the main folders we are using. There is also the option of group_vars folder but we'll not go that far just yet.

Name folders are restricted so they must be named as you see them. At least, the main ones as shown below:


    ┌─ defaults                 	# Default variables if nothing is specified. See `Setting hierarchy` for further info.
    │   ├── main.yml         		# YAML file where you'll specify the default behaviour of every variable.
    ├── files 						# Files that will be copied to the remote as they are.
    │   ├── crontab         		# Let's say you want to upload this crontab file as it is. Without modification.
    ├── handlers           			# Shortcuts such as `reboot <service_name>`. Will be used by `notify:` module under tasks.
    ├── tasks        				# Main goal here. Develop your task for this role. What should your role do?
    └── templates                   # Templates Jinja2 or anything that `template:` module will use.
        ├── apache              	# Apache templates go here
        ├───── virtualhost.conf.j2  # You have some variables inside that will be replaced like ``{{ server_name }}``
        └── logrotate               # Logrotate files go here


Now you know a little bit about how to configure your role. A role can be Ojo, Mano, Oreja... and every role have its tasks with its files.

Let's say you have one role that will deploy an Apache with some virtualhosts. You just need the virtualhost itself inside `files` folder and use the `copy:` module to copy it to the remote inside your `tasks:main.yml` file. That's easy if you just have one environment and you want that file exactly as you have it. The tricky thing turns out as your environment grows because you might need some parameters inside that you want to change. So either you modify the file as many environments you have or you just can have one single file with variables. Cool, that's what I thought.

Since our virtualhost will be a template, it should be placed inside the `templates` folder as it is shown in the example above.
Example:

```
$ cat virtualhost.conf.j2
ServerName {{ server_name }}
Listen {{ ssl_port }}
```

You can define variables basically anywhere but they will not have the same priority. Will not go that deep. Just imagine you have at somewhere a variable called `server_name` but you have several `ServerNames` that you want to define. We can do that with:

`PATH=code/enviro/webservers/group_vars/all`

* server_name: www.example.com
* ssl_port: 443

`PATH=code/enviro/backends/group_vars/all`

* server_name: api.example.com
* ssl_port: 4443

Now, if your webservers hostnames apply to the `role1`, will take `webservers` variables. On the other hand, if they are `backends`... guess!

So basically is the main and global idea about roles and parsing variables according to what you want to do or how you want your Ansible playbooks look like.

Tasks
=====
As you might already know, tasks are actually where the fun is. You want to define those to implement your automation.
You can find several examples in this repo which are pretty friendly to read.

You could define variables and a whole deployment in one task file but that is pretty lame and not recommendend. So all you've created before such as variables, hosts and the like, will be read from the tasks. A task is just how you want your deployment to be, the logical part. It will take the most suitable variable by your needs and will determine if the actual task make either sense or not to be executed.

Handlers
========
These are mainly shortcuts called by tasks. Quite useful. Example:

Handler definition in `code/roles/httpd/handlers/main.yml`

```
- name: reload httpd
  service: name=httpd state=reloaded
```

Handler usage in `code/roles/httpd/tasks/main.yml`

```
- name: Copy certificate key
  copy: src=cert.key dest=/etc/httpd/ssl/
  notify: reload httpd
```


# Techdebt

- [X] provision machines without disk
- [ ] inventory in json dump
- [X] dynamic inventory
- [X] glusterfs run tasks on one node only
- [X] glusterfs manual installation
- [X] glusterfs peer run only on slaves
- [ ] httpd cluster
- [ ] mysql cluster
- [ ] fdisk extra_disk automatically


# References:

* [Vagrant DNS plugin](https://github.com/phinze/landrush)
* [Sublime Text 2/3 Ansible Language Pack](https://github.com/clifford-github/sublime-ansible)
* [Ansible Examples](https://github.com/ansible/ansible-examples)
* [Ansible modules extra](https://github.com/ansible/ansible-modules-extras)
* [Apache Rewrite Rules](http://thornelabs.net/2014/06/02/manage-apache-virtualhosts-and-mod-rewrite-rules-with-ansible.html)
* [Jinja2 Template Examples](https://servercheck.in/blog/apache-virtualhosts-with-ansible-and-jinja2)
