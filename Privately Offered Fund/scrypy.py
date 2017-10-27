#encoding:utf-8
from selenium import webdriver  
import os
import sys
import time
import importlib
def main():
    #点击次数，与页面总页数
    click_num = 1
    total_num = 1067
    
    #引入chromedriver.exe
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)

    #设置浏览器需要打开的url
    url = "http://gs.amac.org.cn/amac-infodisc/res/pof/manager/index.html"  
    driver.get(url)
    #等待5秒，5秒后模拟点击关闭按钮
    time.sleep(5)
    driver.find_element_by_class_name('ui-button-text-only').click()
    #删除文件，并创建新的空白文件
    f = open("source.txt", "w",encoding='utf-8')
    #获取网页源代码
    page = driver.page_source + '\n'
    f.write(page)
    f.close()
    
    #点击下一页操作，并记录每一页的源代码
    f = open('source.txt', 'a',encoding='utf-8')
    while click_num < total_num:
        #定位至下一页按钮并打开至下一页
        driver.find_element_by_class_name("next").click()
        #等待javascript渲染完成
        time.sleep(2)
        #获取网页源代码
        page = driver.page_source + '\n'
        #将网页源代码写入指定文件
        f.write(page)
        
        click_num += 1

    #程序结束后清理
    driver.quit()
    f.close()

if __name__ == '__main__':
    main()
