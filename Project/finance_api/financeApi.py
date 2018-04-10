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
        ''''查询分流单收款核销'''
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

if __name__=='__main__':
    unittest.main()


