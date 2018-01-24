# Ansible整体说明
> 这是一个完整的ansible模块,用来服务器的所有变更，包括：系统初始化，配置文件同步，应用部署，应用发布等功能。
## 1 整体结构说明
### ansible目录结构
```
ansible
├── README
├── ansible.cfg
├── ansible_modul_custom
├── docs
├── init.yml
├── inventories
│   ├── dev
│   │   ├── group_vars
│   │   │   ├── all
│   │   │   └── tomcat
│   │   ├── host_vars
│   │   └── hosts
│   ├── prod
│   └── test
├── playbooks
│   └── test.yml
├── roles
│   ├── commons
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── tasks
│   │   │   ├── SELinux.yml
│   │   │   └── main.yml
│   │   └── templates
│   │       ├── 20-nproc.conf
│   │       ├── hosts
│   │       │   ├── etc_hosts_dev
│   │       │   ├── etc_hosts_prod
│   │       │   └── etc_hosts_test
│   │       ├── limits.conf
│   │       ├── rc.local
│   │       ├── sshd_config
│   │       ├── sudoers
│   │       └── sysctl.conf
│   ├── init
│   │   ├── README.md
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
│   │   │   ├── CentOS-Base.repo
│   │   │   ├── epel.repo
│   │   │   └── iot.repo
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── templates
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   └── tomcat
│       ├── README.md
│       ├── defaults
│       │   └── main.yml
│       ├── files
│       │   └── tomcat
│       │       ├── Catalina
│       │       │   └── localhost
│       │       ├── catalina.policy
│       │       ├── catalina.properties
│       │       ├── conf.d
│       │       │   └── README
│       │       ├── context.xml
│       │       ├── log4j.properties
│       │       ├── logging.properties
│       │       ├── server.xml
│       │       ├── tomcat-users.xml
│       │       ├── tomcat.conf
│       │       └── web.xml
│       ├── handlers
│       │   └── main.yml
│       ├── meta
│       │   └── main.yml
│       ├── tasks
│       │   ├── configure.yml
│       │   ├── deploy.yml
│       │   ├── install.yml
│       │   └── main.yml
│       ├── templates
│       │   └── jenkins
│       ├── tests
│       │   ├── inventory
│       │   └── test.yml
│       └── vars
│           └── main.yml
├── script
│   ├── inithostname.py         #本地脚本
├── site.yml                    #playbook入口
└── tomcat_rolling_update.yml   
```
## 2 一些常用操作
2.1 系统初始化：
```bash
#1)给所有主机组all初始化,项目名在inventory里面
ansible-playbook -i environments/dev/hosts init.yml --extra-vars "hosts=all"
#或者项目名再次指定
ansible-playbook -i environments/dev/hosts init.yml --extra-vars "hosts=jenkins PROJECT_NAME=jenkins"
#2)更新项目：jenkins
ansible-playbook -i environments/dev/hosts tomcat_rolling_update.yml --extra-vars "hosts=jenkins"
#3)安装项目：rocketmq集群
ansible-playbook -i environments/dev/hosts rocketmq.yml
```