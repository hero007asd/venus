# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def getHomeInfoAction(request):
	cbd = {'cbdid':'1','cbdname':'辛香汇'}
	cbdinfo = {'cbdinfo':cbd}
	js = json.dumps(cbdinfo,ensure_ascii=False)
	return HttpResponse(js)

def getMerchantNamesAction(request):
	mer = {'merchantId':'1','merchantName':'辛香汇'}
	return HttpResponse()

def getCbdMeListrAction(request):
	mer = {'merchantId':'1','merchantName':'小南国','uploaderId':'ton','uploaderName':'排队天王1','desp':'小南国小桌45号，大家快来抢啊！','uploadTime':'2014-1-3 19:30','imagePath':''}
	return HttpResponse()

def getHotMerListAction(request):
	line = {'merchantId':'1','merchantName':'小南国','address':'巴黎春天5楼近塘桥地铁'}
	return HttpResponse()

