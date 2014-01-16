# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

import json
# Create your views here.
@csrf_exempt
def getHomeInfoAction(request):
	if request.POST:
		cbd = {'cbdid':'1','cbdname':'辛香汇'}
		cbdArray = [cbd,]
		hotMer = {'hotMerId':'2','hotMerName':'XXXX'}
		hotMerArray = [hotMer,]
		result = {'cbdinfo':cbdArray,'hotMerInfo':hotMerArray}
		js = json.dumps(result,ensure_ascii=False)
		return HttpResponse(js)
	else:raise Http404
# @csrf_exempt
# def getMerchantNamesAction(request):
# 	mer = {'merchantId':'1','merchantName':'辛香汇'}
# 	return HttpResponse()
# @csrf_exempt
# def getCbdMeListrAction(request):
# 	mer = {'merchantId':'1','merchantName':'小南国','uploaderId':'ton','uploaderName':'排队天王1','desp':'小南国小桌45号，大家快来抢啊！','uploadTime':'2014-1-3 19:30','imagePath':''}
# 	return HttpResponse()

