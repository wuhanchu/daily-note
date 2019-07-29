mkdir /opt/centos-yum.bak;
mv /etc/yum.repos.d/* /opt/centos-yum.bak/;
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo;
yum clean all;
yum makecache;