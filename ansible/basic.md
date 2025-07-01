# Bootstrapping

Assuming you have a login (ubuntu, pi, etc.) you can use this to install an `ansible` user

```
---
- hosts: all
  become: yes
  become_method: sudo
  tasks:
  - name: Create users
    ansible.builtin.user:
      name: ansible
  - name: Add ansible user to sudoers
    ansible.builtin.copy:
      dest: "/etc/sudoers.d/ansible"
      content: "ansible  ALL=(ALL)  NOPASSWD: ALL"
  - name: Add my key to authorized_key
    ansible.posix.authorized_key:
      user: ansible
      state: present
      key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
```

You can run against individual hosts in your inventory file like

```
$ ansible-playbook bootstrap.yml -k -b -K -i hosts -l 192.168.3.40
```

# Various adhoc

Running commands, use `-o` to do single-line output
```
$ ansible -o -i ansible-hosts -m ansible.builtin.command -a "uptime" -u ansible all
```
Installing packages

```
ansible -o -b -i ansible-hosts -m ansible.builtin.apt -a "name=auditd state=present" -u ansible all
```
