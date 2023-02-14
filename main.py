import time

from flask import Flask, request
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import db
import fetch

app = Flask(__name__)

# 本地环境chrome和driver都在一个环境调试
@app.route("/local")
def fetchGoods():
	imageRes=fetch.FetchGoods()
	db.ClearGoods()
	db.GoodsInsert(imageRes)
	return imageRes

@app.route("/remote")
def sipderhermes():
	# 实例化对象
	option = ChromeOptions()
	# 无头模式
	option.add_argument("--headless")

	option.add_experimental_option('excludeSwitches',['enable-automation'])# 开启实验性功能
	# 不关闭窗口
	option.add_experimental_option("detach", True)
	# 去除特征值
	option.add_argument("--disable-blink-features=AutomationControlled")

	# 实例化远程谷歌
	driver = webdriver.Remote(
		command_executor="http://chrome:4444/wd/hub",
		desired_capabilities=DesiredCapabilities.CHROME,
		options=option
	) 

	driver.execute_script(
	script="""
		Object.defineProperty(navigator, 'webdriver', {
		get: () => undefined
		})
	"""
	)

	time.sleep(3)
	driver.get("https://www.hermes.cn/cn/zh/")
	goods=driver.find_elements(By.XPATH,"//*[@id='content']/section[3]/ul/li")

	res =[]
	for good in goods:
		goodinfo = good.get_attribute(By.TAG_NAME,"img")
		res.append(goodinfo)
		print(goodinfo)
		
	time.sleep(3)
	driver.close()
	return res


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/goods",methods=["POST"])
def getGoods():
	params = request.get_json()
	limit = params["limit"]
	start = params["start"]
	print(limit,start)
	res= db.GetGoods(start,limit)
	print(res)
	return res

# 主函数入口
if __name__ == '__main__':
	db.InitDbConnection()
	app.run(host="0.0.0.0", port=5000,debug=True)
    