import json

from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import pymysql
import datetime
# Create your views here.
from app01.models import Student
from django.views.decorators.csrf import csrf_exempt
def index(request) :
    return render(request , "index.html")

# get不传参数的Api
def indexApi(request) :
    return JsonResponse({"code":2000 , "msg":"ok" , "data":"这是get数据噢"})

# get传参数的Api
def indexApi2(request) :
    params = request.GET
    return JsonResponse({"code":2000 , "msg":"ok" , "data":"这是get传参,我传入的参数是"+params.get("id")})

# post无参数
@csrf_exempt
def indexApi3(request) :
    return JsonResponse({"code":2000 , "msg":"ok" , "data":"这是post数据噢"})

# post有参数
@csrf_exempt
def indexApi4(request) :
    params = request.POST
    return JsonResponse({"code":2000 , "msg":"ok" , "data":"这是post传参,我传入的参数是"+params.get("id")})

# 表单提交
@csrf_exempt
def indexApi5(request) :
    params = request.POST
    name = params.get("name")
    age = params.get("age")
    return JsonResponse({"code":2000 , "msg":"ok" , "data":"{0}今年{1}岁了".format(name, age)})

# 表单提交 Json格式
@csrf_exempt
def indexApi6(request) :
    print(request.method)
    params = json.loads(request.body)
    print(params)
    id = params.get("ids")
    sex = params.get("sex")
    return JsonResponse({"code":2000 , "msg":"ok" , "data":"ID是{0}，是{1}生".format(id, sex)})