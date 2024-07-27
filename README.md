# serv00-autologin

自动化运行脚本实现 serv00 保活，默认每 30 天运行一次，并通过企业微信机器人进行消息推送


## secrets 配置方式
Settings -> Secrets and variables -> Repository secrets -> New Repository secrets

### 账号密钥
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
### 企业微信机器人
- Name 设置为 WX_URL
Secret 设置为 完整的url
```
https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx
```