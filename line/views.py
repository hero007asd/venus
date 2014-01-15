from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def getHotMerInfoAction(request):
	line = {'nubmerId':'11','uploaderId':'11','uploaderName':'ton','desp':'小南国小桌2号，快来抢','uploadTime':'2013-12-12 19:30','imgPath':'XX'}
	return HttpResponse()

def getMerDetailAction(request):
	line = {'uploaderId':'1','uploaderName':'风中的排队者','desp':'大龙虾真美味，中桌32号，排队人真多','uploadTime':'2013-12-12 19:30','imgPath':'XX','price':'5.00rmb'}
	return HttpResponse()

def grabNumberAction(request):
	line = {'numberId':'1','telNumber':'13472843619','qqNumber':'417732702','other':'XXX'}
	return HttpResponse()

