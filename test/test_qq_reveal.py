from selenium import webdriver

import qq_reveal


def test_get_qq():
    rows_it = qq_reveal.get_qq(r"C:\Users\fgdfr\Desktop\code\qq_reveal\data\邮箱.xlsx")
    for name, email in rows_it:
        print(name._value, ': ', email._value, end="\n")


def test_is_revealed():
    driver = webdriver.Chrome(r"C:\Users\fgdfr\Desktop\code\qq_reveal\config\chromedriver.exe")
    driver.maximize_window()
    driver.get('https://haveibeenpwned.com/')
    assert True == qq_reveal.is_revealed(driver, '*******@qq.com'), '********@qq.com 应该为已泄露账号'


def test_reveal_check():
    qq_list = {'*********@qq.com': '前尘忆梦', '*****@qq.com': 'kuaile_tiantian'}
    qq_reveal.reveal_check(qq_list)
