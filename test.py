#!/usr/bin/python
#-*- encoding:UTF-8 -*-

from public.request import *
from public.sqldb import *
from public.log import *
from public.run import *
from public.sqldb import Transferip_db
import unittest,re,json
class UserLoginInfoAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.transferlogname=Transferlogname()
        cls.transferip_db=Transferip_db()
        api="/business/user/loginInfo/add"
        cls.url=cls.transferip_db.ip+api
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def test_UserLoginInfoAddP0(self):
        makesqldata=None
        newVariableObj={}
        sqlDatalist = [{'sql_condition': 0, 'is_select': True, 'variable': 'sysCode',
                        'sql': 'select FSystemCode from t_SystemAccess where FIsDelete=0'},
                       {'sql_condition': 0, 'is_select': True, 'variable': 'apiKey',
                        'sql': "select s.FApiKey from t_SystemAccessApi s,t_ApiConfig a where s.FApiID=a.FID and a.fUrl like '%/business/user/loginInfo/add'"},
                       {'sql_condition': 0, 'is_select': True, 'variable': 'businessAccount,thirdPartyAccountId',
                        'sql': "select FAccount,FAccountId from t_BusinessAccount where FRegisterSystemCode = '${sysCode}' and FIsDelete = 0"},
                       {'sql_condition': 0, 'is_select': True, 'variable': 'bizCode',
                        'sql': 'select FBusinessCode from t_BussinessAccess where FIsDelete=0'}]
        for sqlDatalistCount in range(len(sqlDatalist)):
            sqlData=sqlDatalist[sqlDatalistCount]
            if sqlData['sql_condition']==0:
                if sqlData['is_select']!=True:
                    self.transferip_db.db.ExecNoQuery(sqlData['sql'])
                else:
                    makesqldata=MakeSqlData(sqlData['variable'],sqlData['sql'])
                    newVariableObj=dict(newVariableObj,**makesqldata.variableObj)
                if makesqldata:
                    sqlDatalist=json.dumps(sqlDatalist,ensure_ascii = False)
                    for i in makesqldata.variableObj.keys():
                        regex=r"\${"+i+r"}"
                        sqlDatalist = re.sub(regex, str(makesqldata.variableObj[i]), sqlDatalist)
                    sqlDatalist=json.loads(sqlDatalist)
                else:
                    #makesqldata not exist,not sql
                    pass
        headers={"Content-Type":"application/json","Route_Api_Auth_Heard":"{'apiKey':'${apiKey}'}","Hyaline-Auth-AccessHeader":"{'sysCode':'${sysCode}','bizCode':'${bizCode}','sign':'03559e3e74efc9f60b6abd7d55c9df60','timeStamp':'12312'}"}
        #replace variable
        if makesqldata:
            params=json.dumps(params,ensure_ascii = False)
            headers=json.dumps(headers,ensure_ascii = False)
            for i in newVariableObj.keys():
                regex=r"\${"+i+r"}"
                params = re.sub(regex, str(newVariableObj[i]), params)
                headers = re.sub(regex, str(newVariableObj[i]), headers)
            params=json.loads(params)
            headers=json.loads(headers)
        else:
            #makesqldata not exist,not sql
            pass
        responseJson=postbody(url=self.url,params=params,headers=headers)
        #__init__
        makesqldata=None
        newVariableObj={}
        for sqlDatalistCount in range(len(sqlDatalist)):
            sqlData=sqlDatalist[sqlDatalistCount]
            if sqlData['sql_condition']==1:
                if sqlData['is_select']!=True:
                    self.transferip_db.db.ExecNoQuery(sqlData['sql'])
                else:
                    makesqldata=MakeSqlData(sqlData['variable'],sqlData['sql'])
                    newVariableObj=dict(newVariableObj,**makesqldata.variableObj)
                if makesqldata:
                    sqlDatalist=json.dumps(sqlDatalist,ensure_ascii = False)
                    for i in makesqldata.variableObj.keys():
                        regex=r"\${"+i+r"}"
                        sqlDatalist = re.sub(regex, str(makesqldata.variableObj[i]), sqlDatalist)
                    sqlDatalist=json.loads(sqlDatalist)
                else:
                    #makesqldata not exist,not sql
                    pass
        assert_response={"code":"0"}
        #replace assert_response
        if makesqldata:
            assert_response=json.dumps(assert_response,ensure_ascii = False)
            for i in newVariableObj.keys():
                regex=r"\${"+i+r"}"
                assert_response = re.sub(regex, str(newVariableObj[i]), assert_response)
            assert_response=json.loads(assert_response)
        else:
            #makesqldata not exist,not sql
            pass

        way="postbody"
        for i in assert_response.keys():
            try:
                self.assertEquals(str(responseJson[i]),assert_response[i])
            except:
                @Log(self.transferlogname.Errorlogname, level="ERROR")
                def writeLog(step_name,url, way, header, params,message,assertResult):
                    print("write Errorlogname")
                writeLog("UserLoginInfoAddP0",self.url,way,headers,params,responseJson['message'],str(responseJson[i])+"!="+assert_response[i])
                self.assertEquals(str(responseJson[i]),assert_response[i])
        pass
        @Log(self.transferlogname.Successlogname, level="INFO")
        def writeLog(step_name,url, way, header, params,message):
            print("write Successlogname")
        writeLog("UserLoginInfoAddP0",self.url,way,headers,params,responseJson['message'])
