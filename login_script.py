import json
from DrissionPage import ChromiumPage, ChromiumOptions
import os

# 从环境变量中获取 账号密码json
account = os.environ.get('ACCOUNT')
accountList = json.loads(account)
co = ChromiumOptions().headless()
page = ChromiumPage(co)
lst=[]

def action(username, password, url):
    page.get(url)
    page.wait(5)
    page.ele('#id_username').input(username)
    page.ele('#id_password').input(password)
    page.ele('#submit').click()
    page.wait(5)
    t = page.ele('css:#nav-menu-collapse > ul > li:nth-child(1) > p').inner_html
    su_text = t.split(':')[1] + '登录成功'
    print(su_text)
    lst.append(su_text)
    page.close()


def main():
    for i in accountList:
        action(i['username'], i['password'], i['url'])
    print(lst)

if __name__ == '__main__':
    main()