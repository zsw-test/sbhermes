import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

# 实例化对象
option = ChromeOptions()
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

for good in goods:
	goodinfo = good.find_element(By.TAG_NAME,"img")
	print(goodinfo.get_attribute('outerHTML'))


# t3=driver.find_element(By.XPATH,"//*[@id='content']/section[3]/ul/li[1]/div/a/picture/img")
# print(t.get_attribute('outerHTML'))

# driver.quit()