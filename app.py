import time

from flask import Flask
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import db

app = Flask(__name__)
DB = db.InitDb()

# 本地环境chrome和driver都在一个环境调试
@app.route("/local")
def fetchGoods():
# 实例化对象
	option = ChromeOptions()
	# 无头模式 linux环境下必须开无头模式，不然启动不了
	option.add_argument("--headless")
	# root环境下跑
	option.add_argument("--no-sandbox")
	option.add_experimental_option('excludeSwitches',['enable-automation'])# 开启实验性功能
	# 不关闭窗口
	option.add_experimental_option("detach", True)
	# 去除特征值
	option.add_argument("--disable-blink-features=AutomationControlled")


	# 实例化谷歌
	driver = webdriver.Chrome(options=option)
	driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
	"source": """
		Object.defineProperty(navigator, 'webdriver', {
		get: () => undefined
		})
	"""
	})

	# 清除一下cookie
	driver.delete_all_cookies

	time.sleep(3)
	driver.get("https://www.hermes.cn/cn/zh/")
	goods=driver.find_elements(By.XPATH,"//*[@id='content']/section[3]/ul/li")

	# 浅爬一下首页的几个图片
	res =[]
	for good in goods:
		goodinfo = good.find_element(By.TAG_NAME,"img")
		imageinfo=goodinfo.get_attribute("data-src")
		
		# 插入mysql
		cursor = DB.cursor()
		sql = 'insert into goods(image) values(%s)'
		cursor.execute(sql,(imageinfo))

		res.append(imageinfo)
		print(imageinfo)



	#driver.close()
	# 存入数据库
	return res


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

@app.route("/goods")
def getGoods():
	cursor= DB.cursor()
	cursor.execute("SELECT * from goods")
	datas = cursor.fetchall()
	images=[]
	for v in datas:
		images.append(v[1])
	return images