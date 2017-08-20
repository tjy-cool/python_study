from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("OK")


# def news(request, nid):     # nid接收的是urls里面路由系统中news/后面的参数，即(\d+)
#     return HttpResponse(nid)

def news(request, nid1, nid2):     # nid接收的是urls里面路由系统中news/后面的参数，即(\d+)
    nid = nid1 + nid2   # 字符串类型
    return HttpResponse(nid)


def page(request, n2, n1):     # nid接收的是urls里面路由系统中news/后面的参数，即(\d+)
    nid = n2 + n1   # 字符串类型
    return HttpResponse(nid)
