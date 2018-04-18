#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import time
class FinanceApi(SuperTest):
    """新财务系统接口测试"""
    TestData=read_json('finance.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"]) + '\n' + login_res.text)
        self.assertTrue(login_res.status_code==200)
        session.close()

    def test2(self):
        """获取权限信息"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"])
        if login_res.status_code==200:
            storage_res=session.post(url=self.TestData["storage"]["storage_url"],data=json.dumps(self.TestData["storage"]["storage_data"]),headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["storage"]) + '\n' + storage_res.text)
            data=json.loads(storage_res.text)
            print(data)
            self.assertTrue(data["status"]==1)
        else:
            raise Exception("登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """查询主订单核销订单号"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            checkSale_res=session.post(url=self.TestData["checkSale"]["checkSale_url"],data=json.dumps(self.TestData["checkSale"]["checkSale_data"]),headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["checkSale"]) + '\n' + checkSale_res.text)
            data=json.loads(checkSale_res.text)
            print(data)
            self.assertTrue(data["status"]==1)
        else:
            raise Exception("登录不成功")
        session.close()


    def test4(self):
        '''查询分流单收款核销'''
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"], data=self.TestData["login"]["login_data"],
                                 headers=self.headers)
        if login_res.status_code == 200:
            checkorder_res = session.post(url=self.TestData["checkOrder"]["checkOrder_url"],
                                         data=json.dumps(self.TestData["checkOrder"]["checkOrder_data"]),
                                         headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["checkOrder"]) + '\n' + checkorder_res.text)
            data = json.loads(checkorder_res.text)
            self.assertTrue(data["status"] == 1)
            list1=[{
			"storeGoodsOrderId": 11118422,
			"splitOrderId": "DD13146",
			"storeGoodsOrderState": 20,
			"splitOrderState": "partArrive",
			"splitOrderOff": 0,
			"payMethod": "online",
			"splitOrderSum": 0.01,
			"splitOrderSumAll": 0.01,
			"payType": "wechat",
			"tradeRecordNo": "01001201804081230084",
			"createdAt": "2018-04-08 16:22:54",
			"pickupTime": "2018-04-09 00:25:08",
			"arrivedTime": "2018-04-08 16:25:41",
			"payTime": "2018-04-08 16:23:10",
			"deliveryManId": 106,
			"deliveryManName": "李松",
			"refundState": 10,
			"refundTradeNo": "01001201804081100014",
			"refundTime": "2018-04-08T08:25:41.000Z",
			"refundFee": 0.01,
			"errorMsg": None,
            "checkState":None,
            "diffSum":None,
			"payer": "店家",
			"splitOrderStateStr": "部分送达",
			"payTypeStr": "微信",
			"payMethodStr": "店家下单在线支付",
			"storeGoodsOrderStateStr": "部分送达",
			"refundStateStr": "退款成功"}]
            list2=data['data']['rows']
            print(list2)
            self.assertListEqual(list1=list1,list2=list2)
        else:
            raise Exception("登录不成功")
        session.close()

    def test5(self):
        '''退货退款核销查询'''
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"], data=self.TestData["login"]["login_data"],
                                 headers=self.headers)
        if login_res.status_code == 200:
            backGoodsOrder_res = session.post(url=self.TestData["backGoodsOrder"]["backGoodsOrder_url"],
                                          data=json.dumps(self.TestData["backGoodsOrder"]["backGoodsOrder_data"]),
                                          headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["checkOrder"]) + '\n' + backGoodsOrder_res.text)
            data = json.loads(backGoodsOrder_res.text)
            self.assertTrue(data["status"] == 1)
            list1=[{
			"id": 702,
			"refundNo": "TH20180416702",
			"realSum": 5,
			"orgSum": 5,
			"checkSum": 5,
			"checkState": 99,
			"checker": "超级管理员(1)",
			"checkTime": "2018-04-16 15:12:52",
			"receiptMan": "超级管理员",
			"takeTime": "2018-04-16 15:11:36",
			"receiptTime": "2018-04-16 15:11:47",
			"BranchOrderId": 5398,
			"storeName": "hdhaada",
			"orderId": 11118531,
			"arrivedTime": "2018-04-16 14:48:49",
			"createdAt": "2018-04-16 14:41:42",
			"deliveryMan": "南昌司机",
			"deliveryPhone": "15221587777",
			"warehouseName": "南昌市仓库"
		}]
            list2 = data['data']['rows']
            print(list2)
            self.assertListEqual(list1=list1, list2=list2)
        else:
            raise Exception("登录不成功")
        session.close()

    def test6(self):
        '''入库订单查询'''
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"], data=self.TestData["login"]["login_data"],
                                 headers=self.headers)
        if login_res.status_code == 200:
            reportorder_res = session.post(url=self.TestData["reportorder"]["reportorder_url"],
                                          data=json.dumps(self.TestData["reportorder"]["reportorder_data"]),
                                          headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["reportorder"]) + '\n' + reportorder_res.text)
            data = json.loads(reportorder_res.text)
            self.assertTrue(data["status"] == 1)
            list1 = [{
			"checkerName": "超级管理员",
			"cityId": 320100,
			"cityName": "南京市",
			"extraOrder": 260945,
			"fromName": "供应商test13",
			"receiptId": 14730054,
			"receiptTime": "2018-04-16 21:16:26",
			"receiptType": 1,
			"receiptTypeName": "stockIn",
			"sum": "170.94015",
			"sumWithTax": "200.00000",
			"tax": "29.05985",
			"toName": "南京仓库",
			"taxType": 0
		}]
            list2 = data['data']['rows']
            print(list2)
            self.assertListEqual(list1=list1, list2=list2)
        else:
            raise Exception("登录不成功")
        session.close()

    def test7(self):
        '''入库订单详细汇总'''
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"], data=self.TestData["login"]["login_data"],
                                 headers=self.headers)
        if login_res.status_code == 200:
            storageinfo_res = session.post(url=self.TestData["storageinfo"]["storageinfo_url"],
                                           data=json.dumps(self.TestData["storageinfo"]["storageinfo_data"]),
                                           headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["storageinfo"]) + '\n' + storageinfo_res.text)
            data = json.loads(storageinfo_res.text)
            self.assertTrue(data["status"] == 1)
            list1 = {
		"checkerName": "超级管理员",
		"cityId": 320100,
		"cityName": "南京市",
		"extraOrder": 260945,
		"fromName": "供应商test13",
		"receiptId": 14730054,
		"receiptTime": "2018-04-16 21:16:26",
		"receiptType": 1,
		"receiptTypeName": "stockIn",
		"sum": "170.94015",
		"sumWithTax": "200.00000",
		"tax": "29.05985",
		"toName": "南京仓库",
		"taxType": 0
	}
            list2 = data['data']
            print(list2)
            self.assertDictEqual(list1, list2)
        else:
            raise Exception("登录不成功")
        session.close()

    def test8(self):
        '''入库订单商品明细查询'''
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"], data=self.TestData["login"]["login_data"],
                                 headers=self.headers)
        if login_res.status_code == 200:
            storagedetail_res = session.post(url=self.TestData["storagedetail"]["storagedetail_url"],
                                           data=json.dumps(self.TestData["storagedetail"]["storagedetail_data"]),
                                           headers=self.headers1)
            Logger(self.TestData["name"]).Info(str(self.TestData["storagedetail"]) + '\n' + storagedetail_res.text)
            data = json.loads(storagedetail_res.text)
            self.assertTrue(data["status"] == 1)
            list1 = [{
    "barCode": "1234567890147",
    "goodsBrandName": "一头牛",
    "firstCatalogName": "旧-进口红酒",
    "goodId": 171424,
    "goodsName": "LOCK",
    "num": 5,
    "transProportion": 1,
    "secondCatalogName": "旧-酒类",
    "specification": "1",
    "sum": "200.00000",
    "unit": "瓶",
    "newArrivedNum": 5
}]
            list2 = data['data']
            print(list2)
            self.assertListEqual(list1=list1, list2=list2)
        else:
            raise Exception("登录不成功")
        session.close()

    def test9(self):
        '''出库订单查询'''
        session = requests.Session()
        login_res = session.post(url=self.TestData["login"]["login_url"],
                                 data=self.TestData["login"]["login_data"],
                                 headers=self.headers)
        if login_res.status_code == 200:
            outWarehouse_res = session.post(url=self.TestData["outWarehouse"]["outWarehouse_url"],
                                             data=json.dumps(
                                                 self.TestData["outWarehouse"]["outWarehouse_data"]),
                                             headers=self.headers1)
            Logger(self.TestData["name"]).Info(
                str(self.TestData["outWarehouse"]) + '\n' + outWarehouse_res.text)
            data = json.loads(outWarehouse_res.text)
            self.assertTrue(data["status"] == 1)
            list1 =  [{
			"storeOrderBranchId": 5419,
			"cityId": 320100,
			"cityName": "南京市",
			"warehouseId": 13,
			"storeId": 122033,
			"storeName": "硕硕百货",
			"off": 0,
			"createdAt": "2018-04-17 11:20:21",
			"storeGoodsOrderId": 11118552,
			"sum": "120.0000",
			"arrivedTime": "2018-04-17 11:41:46",
			"fromName": "南京仓库",
			"toName": "硕硕百货",
			"sales": 205.12820513,
			"salesWithTax": 240,
			"salesTax": "34.87179487",
			"salesTaxRate": 0.1699999999897625
		}]
            list2 = data['data']['rows']
            print(list2)
            self.assertListEqual(list1=list1, list2=list2)
        else:
            raise Exception("登录不成功")
        session.close()

if __name__=='__main__':
    unittest.main()


