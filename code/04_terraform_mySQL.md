# SETTING UP MYSQL AND QUICK TEST

```txt
$ sudo apt install mysql-server
  Reading package lists... Done
  Building dependency tree       
  Reading state information... Done
  The following additional packages will be installed:
    libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-7 libevent-pthreads-2.1-7 libfcgi-perl libhtml-parser-perl libhtml-tagset-perl libhtml-template-perl libhttp-date-perl
    libhttp-message-perl libio-html-perl liblwp-mediatypes-perl libmecab2 libtimedate-perl liburi-perl mecab-ipadic mecab-ipadic-utf8 mecab-utils mysql-client-8.0 mysql-client-core-8.0 mysql-common
    mysql-server-8.0 mysql-server-core-8.0
  Suggested packages:
    libdata-dump-perl libipc-sharedcache-perl libwww-perl mailx tinyca
  The following NEW packages will be installed:
    libcgi-fast-perl libcgi-pm-perl libencode-locale-perl libevent-core-2.1-7 libevent-pthreads-2.1-7 libfcgi-perl libhtml-parser-perl libhtml-tagset-perl libhtml-template-perl libhttp-date-perl
    libhttp-message-perl libio-html-perl liblwp-mediatypes-perl libmecab2 libtimedate-perl liburi-perl mecab-ipadic mecab-ipadic-utf8 mecab-utils mysql-client-8.0 mysql-client-core-8.0 mysql-common mysql-server
    mysql-server-8.0 mysql-server-core-8.0
  0 upgraded, 25 newly installed, 0 to remove and 15 not upgraded.
  Need to get 36.8 MB of archives.
  After this operation, 318 MB of additional disk space will be used.
  Do you want to continue? [Y/n] Y
  Get:1 http://archive.ubuntu.com/ubuntu focal/main amd64 mysql-common all 5.8+1.0.5ubuntu2 [7496 B]
  Get:2 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-client-core-8.0 amd64 8.0.36-0ubuntu0.20.04.1 [5084 kB]
  Get:3 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-client-8.0 amd64 8.0.36-0ubuntu0.20.04.1 [22.0 kB]
  Get:4 http://archive.ubuntu.com/ubuntu focal/main amd64 libevent-core-2.1-7 amd64 2.1.11-stable-1 [89.1 kB]
  Get:5 http://archive.ubuntu.com/ubuntu focal/main amd64 libevent-pthreads-2.1-7 amd64 2.1.11-stable-1 [7372 B]
  Get:6 http://archive.ubuntu.com/ubuntu focal/main amd64 libmecab2 amd64 0.996-10build1 [233 kB]
  Get:7 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-server-core-8.0 amd64 8.0.36-0ubuntu0.20.04.1 [22.7 MB]
  Get:8 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-server-8.0 amd64 8.0.36-0ubuntu0.20.04.1 [1326 kB]
  Get:9 http://archive.ubuntu.com/ubuntu focal/main amd64 libhtml-tagset-perl all 3.20-4 [12.5 kB]
  Get:10 http://archive.ubuntu.com/ubuntu focal/main amd64 liburi-perl all 1.76-2 [77.5 kB]
  Get:11 http://archive.ubuntu.com/ubuntu focal/main amd64 libhtml-parser-perl amd64 3.72-5 [86.3 kB]
  Get:12 http://archive.ubuntu.com/ubuntu focal/main amd64 libcgi-pm-perl all 4.46-1 [186 kB]
  Get:13 http://archive.ubuntu.com/ubuntu focal/main amd64 libfcgi-perl amd64 0.79-1 [33.1 kB]
  Get:14 http://archive.ubuntu.com/ubuntu focal/main amd64 libcgi-fast-perl all 1:2.15-1 [10.5 kB]
  Get:15 http://archive.ubuntu.com/ubuntu focal/main amd64 libencode-locale-perl all 1.05-1 [12.3 kB]
  Get:16 http://archive.ubuntu.com/ubuntu focal/main amd64 libhtml-template-perl all 2.97-1 [59.0 kB]
  Get:17 http://archive.ubuntu.com/ubuntu focal/main amd64 libtimedate-perl all 2.3200-1 [34.0 kB]
  Get:18 http://archive.ubuntu.com/ubuntu focal/main amd64 libhttp-date-perl all 6.05-1 [9920 B]
  Get:19 http://archive.ubuntu.com/ubuntu focal/main amd64 libio-html-perl all 1.001-1 [14.9 kB]
  Get:20 http://archive.ubuntu.com/ubuntu focal/main amd64 liblwp-mediatypes-perl all 6.04-1 [19.5 kB]
  Get:21 http://archive.ubuntu.com/ubuntu focal/main amd64 libhttp-message-perl all 6.22-1 [76.1 kB]
  Get:22 http://archive.ubuntu.com/ubuntu focal/main amd64 mecab-utils amd64 0.996-10build1 [4912 B]
  Get:23 http://archive.ubuntu.com/ubuntu focal/main amd64 mecab-ipadic all 2.7.0-20070801+main-2.1 [6714 kB]
  Get:24 http://archive.ubuntu.com/ubuntu focal/main amd64 mecab-ipadic-utf8 all 2.7.0-20070801+main-2.1 [4380 B]
  Get:25 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 mysql-server all 8.0.36-0ubuntu0.20.04.1 [9484 B]
  Fetched 36.8 MB in 2s (17.5 MB/s)       
  Preconfiguring packages ...
  Selecting previously unselected package mysql-common.
  (Reading database ... 64082 files and directories currently installed.)
  Preparing to unpack .../0-mysql-common_5.8+1.0.5ubuntu2_all.deb ...
  Unpacking mysql-common (5.8+1.0.5ubuntu2) ...
  Selecting previously unselected package mysql-client-core-8.0.
  Preparing to unpack .../1-mysql-client-core-8.0_8.0.36-0ubuntu0.20.04.1_amd64.deb ...
  Unpacking mysql-client-core-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Selecting previously unselected package mysql-client-8.0.
  Preparing to unpack .../2-mysql-client-8.0_8.0.36-0ubuntu0.20.04.1_amd64.deb ...
  Unpacking mysql-client-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Selecting previously unselected package libevent-core-2.1-7:amd64.
  Preparing to unpack .../3-libevent-core-2.1-7_2.1.11-stable-1_amd64.deb ...
  Unpacking libevent-core-2.1-7:amd64 (2.1.11-stable-1) ...
  Selecting previously unselected package libevent-pthreads-2.1-7:amd64.
  Preparing to unpack .../4-libevent-pthreads-2.1-7_2.1.11-stable-1_amd64.deb ...
  Unpacking libevent-pthreads-2.1-7:amd64 (2.1.11-stable-1) ...
  Selecting previously unselected package libmecab2:amd64.
  Preparing to unpack .../5-libmecab2_0.996-10build1_amd64.deb ...
  Unpacking libmecab2:amd64 (0.996-10build1) ...
  Selecting previously unselected package mysql-server-core-8.0.
  Preparing to unpack .../6-mysql-server-core-8.0_8.0.36-0ubuntu0.20.04.1_amd64.deb ...
  Unpacking mysql-server-core-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Setting up mysql-common (5.8+1.0.5ubuntu2) ...
  update-alternatives: using /etc/mysql/my.cnf.fallback to provide /etc/mysql/my.cnf (my.cnf) in auto mode
  Selecting previously unselected package mysql-server-8.0.
  (Reading database ... 64298 files and directories currently installed.)
  Preparing to unpack .../00-mysql-server-8.0_8.0.36-0ubuntu0.20.04.1_amd64.deb ...
  Unpacking mysql-server-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Selecting previously unselected package libhtml-tagset-perl.
  Preparing to unpack .../01-libhtml-tagset-perl_3.20-4_all.deb ...
  Unpacking libhtml-tagset-perl (3.20-4) ...
  Selecting previously unselected package liburi-perl.
  Preparing to unpack .../02-liburi-perl_1.76-2_all.deb ...
  Unpacking liburi-perl (1.76-2) ...
  Selecting previously unselected package libhtml-parser-perl.
  Preparing to unpack .../03-libhtml-parser-perl_3.72-5_amd64.deb ...
  Unpacking libhtml-parser-perl (3.72-5) ...
  Selecting previously unselected package libcgi-pm-perl.
  Preparing to unpack .../04-libcgi-pm-perl_4.46-1_all.deb ...
  Unpacking libcgi-pm-perl (4.46-1) ...
  Selecting previously unselected package libfcgi-perl.
  Preparing to unpack .../05-libfcgi-perl_0.79-1_amd64.deb ...
  Unpacking libfcgi-perl (0.79-1) ...
  Selecting previously unselected package libcgi-fast-perl.
  Preparing to unpack .../06-libcgi-fast-perl_1%3a2.15-1_all.deb ...
  Unpacking libcgi-fast-perl (1:2.15-1) ...
  Selecting previously unselected package libencode-locale-perl.
  Preparing to unpack .../07-libencode-locale-perl_1.05-1_all.deb ...
  Unpacking libencode-locale-perl (1.05-1) ...
  Selecting previously unselected package libhtml-template-perl.
  Preparing to unpack .../08-libhtml-template-perl_2.97-1_all.deb ...
  Unpacking libhtml-template-perl (2.97-1) ...
  Selecting previously unselected package libtimedate-perl.
  Preparing to unpack .../09-libtimedate-perl_2.3200-1_all.deb ...
  Unpacking libtimedate-perl (2.3200-1) ...
  Selecting previously unselected package libhttp-date-perl.
  Preparing to unpack .../10-libhttp-date-perl_6.05-1_all.deb ...
  Unpacking libhttp-date-perl (6.05-1) ...
  Selecting previously unselected package libio-html-perl.
  Preparing to unpack .../11-libio-html-perl_1.001-1_all.deb ...
  Unpacking libio-html-perl (1.001-1) ...
  Selecting previously unselected package liblwp-mediatypes-perl.
  Preparing to unpack .../12-liblwp-mediatypes-perl_6.04-1_all.deb ...
  Unpacking liblwp-mediatypes-perl (6.04-1) ...
  Selecting previously unselected package libhttp-message-perl.
  Preparing to unpack .../13-libhttp-message-perl_6.22-1_all.deb ...
  Unpacking libhttp-message-perl (6.22-1) ...
  Selecting previously unselected package mecab-utils.
  Preparing to unpack .../14-mecab-utils_0.996-10build1_amd64.deb ...
  Unpacking mecab-utils (0.996-10build1) ...
  Selecting previously unselected package mecab-ipadic.
  Preparing to unpack .../15-mecab-ipadic_2.7.0-20070801+main-2.1_all.deb ...
  Unpacking mecab-ipadic (2.7.0-20070801+main-2.1) ...
  Selecting previously unselected package mecab-ipadic-utf8.
  Preparing to unpack .../16-mecab-ipadic-utf8_2.7.0-20070801+main-2.1_all.deb ...
  Unpacking mecab-ipadic-utf8 (2.7.0-20070801+main-2.1) ...
  Selecting previously unselected package mysql-server.
  Preparing to unpack .../17-mysql-server_8.0.36-0ubuntu0.20.04.1_all.deb ...
  Unpacking mysql-server (8.0.36-0ubuntu0.20.04.1) ...
  Setting up libmecab2:amd64 (0.996-10build1) ...
  Setting up mysql-client-core-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Setting up libhtml-tagset-perl (3.20-4) ...
  Setting up liblwp-mediatypes-perl (6.04-1) ...
  Setting up libencode-locale-perl (1.05-1) ...
  Setting up mecab-utils (0.996-10build1) ...
  Setting up libevent-core-2.1-7:amd64 (2.1.11-stable-1) ...
  Setting up libio-html-perl (1.001-1) ...
  Setting up libtimedate-perl (2.3200-1) ...
  Setting up mysql-client-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Setting up libfcgi-perl (0.79-1) ...
  Setting up liburi-perl (1.76-2) ...
  Setting up libevent-pthreads-2.1-7:amd64 (2.1.11-stable-1) ...
  Setting up libhttp-date-perl (6.05-1) ...
  Setting up mecab-ipadic (2.7.0-20070801+main-2.1) ...
  Compiling IPA dictionary for Mecab.  This takes long time...
  reading /usr/share/mecab/dic/ipadic/unk.def ... 40
  emitting double-array: 100% |###########################################| 
  /usr/share/mecab/dic/ipadic/model.def is not found. skipped.
  reading /usr/share/mecab/dic/ipadic/Adverb.csv ... 3032
  reading /usr/share/mecab/dic/ipadic/Noun.nai.csv ... 42
  reading /usr/share/mecab/dic/ipadic/Prefix.csv ... 221
  reading /usr/share/mecab/dic/ipadic/Adnominal.csv ... 135
  reading /usr/share/mecab/dic/ipadic/Noun.adverbal.csv ... 795
  reading /usr/share/mecab/dic/ipadic/Noun.adjv.csv ... 3328
  reading /usr/share/mecab/dic/ipadic/Postp.csv ... 146
  reading /usr/share/mecab/dic/ipadic/Conjunction.csv ... 171
  reading /usr/share/mecab/dic/ipadic/Noun.org.csv ... 16668
  reading /usr/share/mecab/dic/ipadic/Symbol.csv ... 208
  reading /usr/share/mecab/dic/ipadic/Interjection.csv ... 252
  reading /usr/share/mecab/dic/ipadic/Suffix.csv ... 1393
  reading /usr/share/mecab/dic/ipadic/Noun.verbal.csv ... 12146
  reading /usr/share/mecab/dic/ipadic/Adj.csv ... 27210
  reading /usr/share/mecab/dic/ipadic/Auxil.csv ... 199
  reading /usr/share/mecab/dic/ipadic/Noun.number.csv ... 42
  reading /usr/share/mecab/dic/ipadic/Verb.csv ... 130750
  reading /usr/share/mecab/dic/ipadic/Others.csv ... 2
  reading /usr/share/mecab/dic/ipadic/Filler.csv ... 19
  reading /usr/share/mecab/dic/ipadic/Noun.csv ... 60477
  reading /usr/share/mecab/dic/ipadic/Postp-col.csv ... 91
  reading /usr/share/mecab/dic/ipadic/Noun.demonst.csv ... 120
  reading /usr/share/mecab/dic/ipadic/Noun.proper.csv ... 27328
  reading /usr/share/mecab/dic/ipadic/Noun.others.csv ... 151
  reading /usr/share/mecab/dic/ipadic/Noun.place.csv ... 72999
  reading /usr/share/mecab/dic/ipadic/Noun.name.csv ... 34202
  emitting double-array: 100% |###########################################| 
  reading /usr/share/mecab/dic/ipadic/matrix.def ... 1316x1316
  emitting matrix      : 100% |###########################################| 
  
  done!
  update-alternatives: using /var/lib/mecab/dic/ipadic to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
  Setting up mysql-server-core-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  Setting up mecab-ipadic-utf8 (2.7.0-20070801+main-2.1) ...
  Compiling IPA dictionary for Mecab.  This takes long time...
  reading /usr/share/mecab/dic/ipadic/unk.def ... 40
  emitting double-array: 100% |###########################################| 
  /usr/share/mecab/dic/ipadic/model.def is not found. skipped.
  reading /usr/share/mecab/dic/ipadic/Adverb.csv ... 3032
  reading /usr/share/mecab/dic/ipadic/Noun.nai.csv ... 42
  reading /usr/share/mecab/dic/ipadic/Prefix.csv ... 221
  reading /usr/share/mecab/dic/ipadic/Adnominal.csv ... 135
  reading /usr/share/mecab/dic/ipadic/Noun.adverbal.csv ... 795
  reading /usr/share/mecab/dic/ipadic/Noun.adjv.csv ... 3328
  reading /usr/share/mecab/dic/ipadic/Postp.csv ... 146
  reading /usr/share/mecab/dic/ipadic/Conjunction.csv ... 171
  reading /usr/share/mecab/dic/ipadic/Noun.org.csv ... 16668
  reading /usr/share/mecab/dic/ipadic/Symbol.csv ... 208
  reading /usr/share/mecab/dic/ipadic/Interjection.csv ... 252
  reading /usr/share/mecab/dic/ipadic/Suffix.csv ... 1393
  reading /usr/share/mecab/dic/ipadic/Noun.verbal.csv ... 12146
  reading /usr/share/mecab/dic/ipadic/Adj.csv ... 27210
  reading /usr/share/mecab/dic/ipadic/Auxil.csv ... 199
  reading /usr/share/mecab/dic/ipadic/Noun.number.csv ... 42
  reading /usr/share/mecab/dic/ipadic/Verb.csv ... 130750
  reading /usr/share/mecab/dic/ipadic/Others.csv ... 2
  reading /usr/share/mecab/dic/ipadic/Filler.csv ... 19
  reading /usr/share/mecab/dic/ipadic/Noun.csv ... 60477
  reading /usr/share/mecab/dic/ipadic/Postp-col.csv ... 91
  reading /usr/share/mecab/dic/ipadic/Noun.demonst.csv ... 120
  reading /usr/share/mecab/dic/ipadic/Noun.proper.csv ... 27328
  reading /usr/share/mecab/dic/ipadic/Noun.others.csv ... 151
  reading /usr/share/mecab/dic/ipadic/Noun.place.csv ... 72999
  reading /usr/share/mecab/dic/ipadic/Noun.name.csv ... 34202
  emitting double-array: 100% |###########################################| 
  reading /usr/share/mecab/dic/ipadic/matrix.def ... 1316x1316
  emitting matrix      : 100% |###########################################| 
  
  done!
  update-alternatives: using /var/lib/mecab/dic/ipadic-utf8 to provide /var/lib/mecab/dic/debian (mecab-dictionary) in auto mode
  Setting up libhtml-parser-perl (3.72-5) ...
  Setting up libhttp-message-perl (6.22-1) ...
  Setting up mysql-server-8.0 (8.0.36-0ubuntu0.20.04.1) ...
  update-alternatives: using /etc/mysql/mysql.cnf to provide /etc/mysql/my.cnf (my.cnf) in auto mode
  Renaming removed key_buffer and myisam-recover options (if present)
  mysqld will log errors to /var/log/mysql/error.log
  mysqld is running as pid 4673
  Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service → /lib/systemd/system/mysql.service.
  Setting up libcgi-pm-perl (4.46-1) ...
  Setting up libhtml-template-perl (2.97-1) ...
  Setting up mysql-server (8.0.36-0ubuntu0.20.04.1) ...
  Setting up libcgi-fast-perl (1:2.15-1) ...
  Processing triggers for systemd (245.4-4ubuntu3.23) ...
  Processing triggers for man-db (2.9.1-1) ...
  Processing triggers for libc-bin (2.31-0ubuntu9.14) ...

$ sudo service mysql status
  ● mysql.service - MySQL Community Server
       Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
       Active: active (running) since Tue 2024-03-26 21:35:06 EDT; 2min 58s ago
     Main PID: 4919 (mysqld)
       Status: "Server is operational"
        Tasks: 37 (limit: 2317)
       Memory: 365.2M
       CGroup: /system.slice/mysql.service
               └─4919 /usr/sbin/mysqld
  
  Mar 26 21:35:01 mysql2 systemd[1]: Starting MySQL Community Server...
  Mar 26 21:35:06 mysql2 systemd[1]: Started MySQL Community Server.

$ sudo ss -tap | grep mysql
  LISTEN   0         70               127.0.0.1:33060             0.0.0.0:*        users:(("mysqld",pid=4919,fd=31))                                              
  LISTEN   0         151              127.0.0.1:mysql             0.0.0.0:*        users:(("mysqld",pid=4919,fd=33))

$ sudo mysql
  Welcome to the MySQL monitor.  Commands end with ; or \g.
  Your MySQL connection id is 9
  Server version: 8.0.36-0ubuntu0.20.04.1 (Ubuntu)
  
  Copyright (c) 2000, 2024, Oracle and/or its affiliates.
  
  Oracle is a registered trademark of Oracle Corporation and/or its
  affiliates. Other names may be trademarks of their respective
  owners.
  
  Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
  
  mysql> 
```
If we found mysql prompt above, it means that mySQL was successfully installed.</br>
Herewith some quick test on querying.
```txt
mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | information_schema |
    | mysql              |
    | performance_schema |
    | sys                |
    +--------------------+
    4 rows in set (0.02 sec)
  
  mysql> USE mysql;
  Reading table information for completion of table and column names
  You can turn off this feature to get a quicker startup with -A
  
  Database changed

mysql> select * from global_grants;
  +------------------+-----------+------------------------------+-------------------+
  | USER             | HOST      | PRIV                         | WITH_GRANT_OPTION |
  +------------------+-----------+------------------------------+-------------------+
  | debian-sys-maint | localhost | APPLICATION_PASSWORD_ADMIN   | Y                 |
  | debian-sys-maint | localhost | AUDIT_ADMIN                  | Y                 |
  | debian-sys-maint | localhost | AUTHENTICATION_POLICY_ADMIN  | Y                 |
  | debian-sys-maint | localhost | BACKUP_ADMIN                 | Y                 |
  | debian-sys-maint | localhost | BINLOG_ADMIN                 | Y                 |
  | debian-sys-maint | localhost | BINLOG_ENCRYPTION_ADMIN      | Y                 |
  | debian-sys-maint | localhost | CLONE_ADMIN                  | Y                 |
  | debian-sys-maint | localhost | CONNECTION_ADMIN             | Y                 |
  | debian-sys-maint | localhost | ENCRYPTION_KEY_ADMIN         | Y                 |
  | debian-sys-maint | localhost | FLUSH_OPTIMIZER_COSTS        | Y                 |
  | debian-sys-maint | localhost | FLUSH_STATUS                 | Y                 |
  | debian-sys-maint | localhost | FLUSH_TABLES                 | Y                 |
  | debian-sys-maint | localhost | FLUSH_USER_RESOURCES         | Y                 |
  | debian-sys-maint | localhost | GROUP_REPLICATION_ADMIN      | Y                 |
  | debian-sys-maint | localhost | GROUP_REPLICATION_STREAM     | Y                 |
  | debian-sys-maint | localhost | INNODB_REDO_LOG_ARCHIVE      | Y                 |
  | debian-sys-maint | localhost | INNODB_REDO_LOG_ENABLE       | Y                 |
  | debian-sys-maint | localhost | PASSWORDLESS_USER_ADMIN      | Y                 |
  | debian-sys-maint | localhost | PERSIST_RO_VARIABLES_ADMIN   | Y                 |
  | debian-sys-maint | localhost | REPLICATION_APPLIER          | Y                 |
  | debian-sys-maint | localhost | REPLICATION_SLAVE_ADMIN      | Y                 |
  | debian-sys-maint | localhost | RESOURCE_GROUP_ADMIN         | Y                 |
  | debian-sys-maint | localhost | RESOURCE_GROUP_USER          | Y                 |
  | debian-sys-maint | localhost | ROLE_ADMIN                   | Y                 |
  | debian-sys-maint | localhost | SENSITIVE_VARIABLES_OBSERVER | Y                 |
  | debian-sys-maint | localhost | SERVICE_CONNECTION_ADMIN     | Y                 |
  | debian-sys-maint | localhost | SESSION_VARIABLES_ADMIN      | Y                 |
  | debian-sys-maint | localhost | SET_USER_ID                  | Y                 |
  | debian-sys-maint | localhost | SHOW_ROUTINE                 | Y                 |
  | debian-sys-maint | localhost | SYSTEM_USER                  | Y                 |
  | debian-sys-maint | localhost | SYSTEM_VARIABLES_ADMIN       | Y                 |
  | debian-sys-maint | localhost | TABLE_ENCRYPTION_ADMIN       | Y                 |
  | debian-sys-maint | localhost | TELEMETRY_LOG_ADMIN          | Y                 |
  | debian-sys-maint | localhost | XA_RECOVER_ADMIN             | Y                 |
  | mysql.infoschema | localhost | AUDIT_ABORT_EXEMPT           | N                 |
  | mysql.infoschema | localhost | FIREWALL_EXEMPT              | N                 |
  | mysql.infoschema | localhost | SYSTEM_USER                  | N                 |
  | mysql.session    | localhost | AUDIT_ABORT_EXEMPT           | N                 |
  | mysql.session    | localhost | AUTHENTICATION_POLICY_ADMIN  | N                 |
  | mysql.session    | localhost | BACKUP_ADMIN                 | N                 |
  | mysql.session    | localhost | CLONE_ADMIN                  | N                 |
  | mysql.session    | localhost | CONNECTION_ADMIN             | N                 |
  | mysql.session    | localhost | FIREWALL_EXEMPT              | N                 |
  | mysql.session    | localhost | PERSIST_RO_VARIABLES_ADMIN   | N                 |
  | mysql.session    | localhost | SESSION_VARIABLES_ADMIN      | N                 |
  | mysql.session    | localhost | SYSTEM_USER                  | N                 |
  | mysql.session    | localhost | SYSTEM_VARIABLES_ADMIN       | N                 |
  | mysql.sys        | localhost | AUDIT_ABORT_EXEMPT           | N                 |
  | mysql.sys        | localhost | FIREWALL_EXEMPT              | N                 |
  | mysql.sys        | localhost | SYSTEM_USER                  | N                 |
  | root             | localhost | APPLICATION_PASSWORD_ADMIN   | Y                 |
  | root             | localhost | AUDIT_ABORT_EXEMPT           | Y                 |
  | root             | localhost | AUDIT_ADMIN                  | Y                 |
  | root             | localhost | AUTHENTICATION_POLICY_ADMIN  | Y                 |
  | root             | localhost | BACKUP_ADMIN                 | Y                 |
  | root             | localhost | BINLOG_ADMIN                 | Y                 |
  | root             | localhost | BINLOG_ENCRYPTION_ADMIN      | Y                 |
  | root             | localhost | CLONE_ADMIN                  | Y                 |
  | root             | localhost | CONNECTION_ADMIN             | Y                 |
  | root             | localhost | ENCRYPTION_KEY_ADMIN         | Y                 |
  | root             | localhost | FIREWALL_EXEMPT              | Y                 |
  | root             | localhost | FLUSH_OPTIMIZER_COSTS        | Y                 |
  | root             | localhost | FLUSH_STATUS                 | Y                 |
  | root             | localhost | FLUSH_TABLES                 | Y                 |
  | root             | localhost | FLUSH_USER_RESOURCES         | Y                 |
  | root             | localhost | GROUP_REPLICATION_ADMIN      | Y                 |
  | root             | localhost | GROUP_REPLICATION_STREAM     | Y                 |
  | root             | localhost | INNODB_REDO_LOG_ARCHIVE      | Y                 |
  | root             | localhost | INNODB_REDO_LOG_ENABLE       | Y                 |
  | root             | localhost | PASSWORDLESS_USER_ADMIN      | Y                 |
  | root             | localhost | PERSIST_RO_VARIABLES_ADMIN   | Y                 |
  | root             | localhost | REPLICATION_APPLIER          | Y                 |
  | root             | localhost | REPLICATION_SLAVE_ADMIN      | Y                 |
  | root             | localhost | RESOURCE_GROUP_ADMIN         | Y                 |
  | root             | localhost | RESOURCE_GROUP_USER          | Y                 |
  | root             | localhost | ROLE_ADMIN                   | Y                 |
  | root             | localhost | SENSITIVE_VARIABLES_OBSERVER | Y                 |
  | root             | localhost | SERVICE_CONNECTION_ADMIN     | Y                 |
  | root             | localhost | SESSION_VARIABLES_ADMIN      | Y                 |
  | root             | localhost | SET_USER_ID                  | Y                 |
  | root             | localhost | SHOW_ROUTINE                 | Y                 |
  | root             | localhost | SYSTEM_USER                  | Y                 |
  | root             | localhost | SYSTEM_VARIABLES_ADMIN       | Y                 |
  | root             | localhost | TABLE_ENCRYPTION_ADMIN       | Y                 |
  | root             | localhost | TELEMETRY_LOG_ADMIN          | Y                 |
  | root             | localhost | XA_RECOVER_ADMIN             | Y                 |
  +------------------+-----------+------------------------------+-------------------+
  86 rows in set (0.00 sec)
  
  mysql> 
```
# TERRAFORM
Herewith the terraform code for setting up basic MySQL. </br>
Further database creation, need in-depth requirement, schema design, data mapping, etc. </br>

```txt
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  tags = {
    Name = "example-instance"
  }
}

resource "null_resource" "install_mysql" {
  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install mysql-server",
      "sudo service mysql status"
    ]

    connection {
      type        = "ssh"
      user        = "ubuntu"
      private_key = file("~/.ssh/id_rsa")
      host        = aws_instance.example.public_ip
    }
  }

  depends_on = [aws_instance.example]
}
```
