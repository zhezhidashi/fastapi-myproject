Python环境

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

设置mysql
用户名 root，密码 zzh12345
```sql
create database myproject
```