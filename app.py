import time

from flask import Flask
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

app = Flask(__name__)


@app.route("/")
def sipderhermes():
	# 实例化对象
	option = ChromeOptions()
	# 无头模式
	option.add_argument("--headless")

	option.add_experimental_option('excludeSwitches',['enable-automation'])# 开启实验性功能
	# 不关闭窗口
	option.add_experimental_option("detach", True)
	# 去除特征值
	# option.add_argument("--disable-blink-features=AutomationControlled")
	# 实例化谷歌
	driver = webdriver.Chrome(options=option)

	driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
	"source": """
		Object.defineProperty(navigator, 'webdriver', {
		get: () => undefined
		})
	"""
	})

	time.sleep(3)
	driver.get("https://www.hermes.cn/cn/zh/")
	goods=driver.find_elements(By.XPATH,"//*[@id='content']/section[3]/ul/li")

	res =[]
	for good in goods:
		goodinfo = good.find_element(By.TAG_NAME,"img")
		res.append(goodinfo.get_attribute('outerHTML'))
		print(goodinfo.get_attribute('outerHTML'))

	
	return res



def hello():
    return "Hello, World!"
# t3=driver.find_element(By.XPATH,"//*[@id='content']/section[3]/ul/li[1]/div/a/picture/img")
# print(t.get_attribute('outerHTML'))

# driver.quit()