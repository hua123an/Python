import time
import unittest

from selenium import webdriver


# 需求：
# 1.测试用户名不正确 密码正确
# 2.测试用户名正确  密码不正确
# 3.测试用户名不正确  密码不正确
# 4.测试用户名正确  密码正确
# 5.测试输入用户名或者密码为空值
# 6.测试输入用户名或者密码为空值
# 7.测试输入用户名为非数字字符
# 测试账号 19916481564
# 测试密码 wanwbgq12



class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.drive = webdriver.Chrome()
        self.drive.get("https://passport2.chaoxing.com/login?fid=&newversion=true&refer=https://i.chaoxing.com")
        self.drive.maximize_window()
        self.username = self.drive.find_element_by_css_selector('#phone')
        self.pwd = self.drive.find_element_by_css_selector('#pwd')
        self.btn = self.drive.find_element_by_css_selector('#loginBtn')

    def tearDown(self) -> None:
        time.sleep(2)
        self.drive.quit()

    # 1.测试用户名不正确 密码正确
    def test_login_username_err(self):
        self.username.send_keys('123456')
        self.pwd.send_keys('wanwbgq12')
        self.btn.click()
        time.sleep(2)
        message = self.drive.find_element_by_css_selector('#err-txt')
        if message.text == '手机号或密码错误':
            print('测试成功')
        else:
            print('测试失败')
    # 2.测试用户名正确  密码不正确
    def test_login_pwd_error(self):
        self.username.send_keys('19916481564')
        self.pwd.send_keys('456789')
        self.btn.click()
        time.sleep(2)
        message = self.drive.find_element_by_css_selector('#err-txt')
        if message.text == '手机号或密码错误':
            print('测试成功')
        else:
            print('测试失败')
    # 3.测试用户名不正确  密码不正确
    def test_login_username_pwd_error(self):
        self.username.send_keys('123456')
        self.pwd.send_keys('456789')
        self.btn.click()
        time.sleep(2)
        message = self.drive.find_element_by_css_selector('#err-txt')
        if message.text == '手机号或密码错误':
            print('测试成功')
        else:
            print('测试失败')

    # 4.测试用户名正确  密码正确
    def test_login_success(self):
        self.username.send_keys('19916481564')
        self.pwd.send_keys('wanwbgq12')
        self.btn.click()
        time.sleep(2)
        userinfo = self.drive.find_element_by_css_selector('#siteName')
        if userinfo.text == '超星网空间':
            print('测试成功')
        else:
            print('测试失败')
    # 5.测试输入用户名为空值
    def test_login_username_null(self):
        self.pwd.send_keys('wanwbgq12')
        self.btn.click()
        time.sleep(2)
        userinfo = self.drive.find_element_by_css_selector('.err-txt')
        if userinfo.text == '请输入手机号':
            print('测试成功')
        else:
            print('测试失败')
#     6.输入手机号非数字
    def test_login_username_NaN(self):
        self.username.send_keys('#56784758')
        self.pwd.send_keys('wanwbgq12')
        self.btn.click()
        time.sleep(2)
        userinfo = self.drive.find_element_by_css_selector('#err-txt')
        if userinfo.text == '手机号或密码错误':
            print('测试成功')
        else:
            print('测试失败')

