# serv00-autologin

自动化运行脚本实现 serv00 保活，默认每 30 天运行一次


## secrets 配置方式
Settings -> Secrets and variables -> Repository secrets -> New Repository secrets

- Name 设置为 ACCOUNT            
- Secret 格式如下

```json
[
    {
        "username": "test",
        "password": "test",
        "url": "http://xxxx/login"
    },
    {
        "username": "test2",
        "password": "test2",
        "url": "http://xxxx/login"
    }
]

```