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
    assert True == qq_reveal.is_revealed(driver, '1542940053@qq.com'), '1542940053@qq.com 应该为已泄露账号'


def test_reveal_check():
    qq_list = {'839684679@qq.com': '前尘忆梦', 'kuaile_tiantian@qq.com': 'kuaile_tiantian', '1669194839@qq.com': '崔老师', '799014240@qq.com': '799014240', '1426987342@qq.com': '此去经年，回首已成空', '√小时光xpard08@163.com': 'xpard924011057@qq.com', '伤痛不过百日长': '7559166859@qq.com', '7559166859': '759166859@qq.com', '759166859': 'zhaohw@jlu.edu.cn', 'Zhaohw': '284418373@qq.com', '王 喆': '5483667@qq.com', '5483667': '839684679@qq.com', '前尘忆梦': 'kuaile_tiantian@qq.com', 'kuaile_tiantian': '1669194839@qq.com', '崔老师': '799014240@qq.com', '郭天硕': '799014240@qq.com', '799014240': '1426987342@qq.com', '此去经年，回首已成空1067949592@qq.com': '√小时光xpard08@163.com', 'xpard924011057@qq.com': '伤痛不过百日长', '7559166859@qq.com': '7559166859', '759166859@qq.com': '759166859', 'zhaohw@jlu.edu.cn': 'Zhaohw', '284418373@qq.com': '王 喆', '5483667@qq.com': '5483667', '1067949592@qq.com': '√小时光xpard08@163.com'}
    qq_reveal.reveal_check(qq_list)
