# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def uploadInfoAction(request):
	return HttpResponse()
@csrf_exempt
def myFinishedPublishListAction(request):
	return HttpResponse()
@csrf_exempt
def myUnfinishPublishListAction(request):
	return HttpResponse()
@csrf_exempt
def myUnfinishPublishDetailAction(request):
	return HttpResponse()
@csrf_exempt
def finishPushlishAction(request):
	return HttpResponse()
@csrf_exempt
def cancelPushlishAction(request):
	return HttpResponse()
@csrf_exempt
def myFinishedGrapListAction(request):
	return HttpResponse()
@csrf_exempt
def myUnfinishGrapListAction(request):
	return HttpResponse()