# 查询是否锁表
show OPEN TABLES where In_use > 0;

# 查看慢语句日志
show variables like '%slow%';

# 查看进程
show processlist;

# 查询到相对应的进程
kill id