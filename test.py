import unittest

import fetch


# 测试获取商品
class TestFetchMethod(unittest.TestCase):
	def test_fetch(self):
		#DB=db.InitDbConnection()
		fetch.FetchGoods()
		#DB.close()

unittest.main()