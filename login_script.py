import json
from DrissionPage import ChromiumPage, ChromiumOptions
import os
import requests 

# 从环境变量中获取 账号密码json、企业微信机器人webhook地址
account = os.environ.get('ACCOUNT')
accountList = json.loads(account)
wx_url = os.environ.get('WX_URL')
co = ChromiumOptions().headless()
message = ''


def action(username, password, url):
    page = ChromiumPage(co)
    page.get(url)
    page.wait(5)
    page.ele('#id_username').input(username)
    page.ele('#id_password').input(password)
    page.ele('#submit').click()
    page.wait(5)
    t = page.ele('css:#nav-menu-collapse > ul > li:nth-child(1) > p').inner_html
    su_text = t.split(':')[1] + '---登录成功'
    print(su_text)
    message = message + su_text + '\n'
    page.wait(10)
    page.close()

def send_markdown (message, wx_url):
    data = {"msgtype": "markdown", "markdown": {"content": message}}
    r = requests.post(url=wx_url,data=json.dumps(data))
    print(r.text)
    print(r.status_code)

def main():
    for i in accountList:
        action(i['username'], i['password'], i['url'])
    send_markdown(message)

if __name__ == '__main__':
    main()