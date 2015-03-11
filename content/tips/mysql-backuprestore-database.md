Title: MySQL - Backup/Restore database
Date: 2014-04-24 14:08
Author: dai
Category: Tips
Tags: backup, database, mysql, restore
Slug: mysql-backuprestore-database

` backup: # mysqldump -u root -p[root_password] [database_name] > dumpfilename.sql restore:# mysql -u root -p[root_password] [database_name] < dumpfilename.sql`
