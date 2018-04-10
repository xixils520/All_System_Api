#coding:utf-8
from BaseRequest.SuperUnit import SuperTest
from Public.log import Logger
from Public.readJson import read_json
from Public.randyData import allData
import unittest
import requests
import json
import time
class PurchaseM(SuperTest):
    """新采购系统接口测试"""
    TestData=read_json('purchase_management.json')
    def test1(self):
        """登录接口测试"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],
                               headers=self.headers)
        self.assertTrue(login_res.status_code==200)
        Logger(self.TestData["name"]).Info(str(self.TestData["login"])+'\n'+login_res.text)
        session.close()

    def test2(self):
        """城市商品管理展示"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            GoodsList_res=session.post(url=self.TestData["GoodsList"]["GoodsList_url"],data=self.TestData["GoodsList"]["GoodsList_data"])
            self.assertTrue(GoodsList_res.status_code==200)
        else:
            raise Exception("登录不成功不进行单元测试")
        session.close()

    def test3(self):
        """供应商信息管理"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            GoodsList_res=session.post(url=self.TestData["GoodsList"]["GoodsList_url"],data=self.TestData["GoodsList"]["GoodsList_data"])
            self.assertTrue(GoodsList_res.status_code==200)
            Logger(self.TestData["name"]).Info(str(self.TestData["GoodsList"])+'\n'+GoodsList_res.text)
        else:
            raise Exception("登录不成功不进行单元测试")
        session.close()

    def test4(self):
        """签约主体管理"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            subjectList_res=session.post(url=self.TestData["subjectList"]["subjectList_url"],data=self.TestData["subjectList"]["subjectList_data"])
            subjectList_json=json.loads(allData().changeIntoStr(subjectList_res.text))
            self.assertTrue(subjectList_res.status_code==200 and len(subjectList_json["data"])>=1)
            Logger(self.TestData["name"]).Info(str(self.TestData["subjectList"])+'\n'+subjectList_res.text)
        else:
            raise Exception("登录不成功不进行单元测试")
        session.close()

    def test5(self):
        """报价单列表信息查询"""
        session=requests.Session()
        login_res=session.post(url=self.TestData["login"]["login_url"],data=self.TestData["login"]["login_data"],headers=self.headers)
        if login_res.status_code==200:
            session.post(url=self.TestData["updateAgency"]["agency_url"],data=self.TestData["updateAgency"]["agency_data"])
            basePricePlan_res=session.post(url=self.TestData["basePricePlan"]["basePricePlan_url"],data=self.TestData["basePricePlan"]["basePricePlan_data"])
            basePricePlan_json=json.loads(allData().changeIntoStr(basePricePlan_res.text))
            self.assertTrue(basePricePlan_res.status_code==200 and len(basePricePlan_json["data"])>=1)
            Logger(self.TestData["name"]).Info(str(self.TestData["basePricePlan"]))
        else:
            raise Exception("登录不成功不进行单元测试")
        session.close()



if __name__=='__main__':
    unittest.main()


