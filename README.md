# Python环境

```shell
# 初始化虚拟环境
python3 -m venv .venv

# 激活虚拟环境
. .venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行
uvicorn main:app --reload

# 测试
pytest
```

# 安装mysql
下载地址：https://dev.mysql.com/downloads/mysql/
选择 8.0.34 版本；操作系统选择 Linux - Generic
Mysql 版本选择：Linux - Generic (glibc 2.28) (x86, 64-bit), Compressed TAR Archive (mysql-8.0.34-linux-glibc2.28-x86_64.tar.gz)

下载到 /usr/local 路径下，解压后改为为 mysql，即 /usr/local/mysql
添加 mysql 用户组
```shell
groupadd mysql
useradd -r -g mysql -s /bin/false mysql
```

在 /usr/local/mysql 目录下
```shell
# 修改目录拥有者为 mysql 用户
chown -R mysql:mysql ./

# 安装 Mysql，注意输出的最后一行会显示出来生成的默认密码！！！
./bin/mysqld --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --initialize

# 开启mysql服务
./support-files/mysql.server start

# 将mysql进程放入系统进程中
cp support-files/mysql.server /etc/init.d/mysqld

# 重新启动mysql服务
service mysqld restart

# 配置mysql环境变量  export PATH=$PATH:/usr/local/mysql/bin
vim /etc/profile
source /etc/profile

# 启动 Mysql
mysql -u root -p
```

```sql
# 重新设置密码为 zzh12345
alter user 'root'@'localhost' identified by 'root';
use mysql;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'zzh12345';
# 也可能是 ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'zzh12345';
flush privileges;
```

用户名 root，密码 zzh12345

```sql
create database myproject
```

# 部署
开启 gunicorn
```shell
bash start-gunicorn.sh
```

关闭 gunicorn
```shell
bash stop-gunicorn.sh
```