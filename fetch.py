import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


# 爬虫主要函数  返回爬取的数据
def FetchGoods():
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
	imageRes =[]
	for good in goods:
		goodinfo = good.find_element(By.TAG_NAME,"img")
		imageinfo=goodinfo.get_attribute("data-src")

		#print(imageinfo,len(imageinfo))
		if len(imageinfo)>2:
			imageinfo = imageinfo[2:]
		print(imageinfo,len(imageinfo))

		imageRes.append(imageinfo)
		

	driver.close()
	# 存入数据库
	return imageRes


