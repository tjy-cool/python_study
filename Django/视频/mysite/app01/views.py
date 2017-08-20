from django.shortcuts import render, HttpResponse
from app01 import models
# Create your views here.

def db_handle(request):
    # request封装了用户请求的所有内容
    # request.POST      用户以POST提交
    # request.GET       用户以GET提交
    
    # 增加
    # 方法一：直接传单个数据
    # models.UserInfo.objects.create(username='tjy', password='123', age=18)   
    # 方法二： 传递字典
    # dic = {"username":'tjy', "password": '12343', "age": 25}
    # models.UserInfo.objects.create(**dic)

    # 删除
    # models.UserInfo.objects.filter(age=18).delete()

    # 修改
    # models.UserInfo.objects.all().update(age=18)

    # 打印
    # user_list_obj = models.UserInfo.objects.all()
    # for line in user_list_obj:
    #     print(line.username, line.age)
    
    # 查找
    # models.UserInfo.objects.all()   # 查找所有用户
    # models.UserInfo.objects.filter(age=19)  # 查找所有age=19
    # models.UserInfo.objects.filter(age=19).first()  # 查找age=19的第一个
    # return HttpResponse('ok')

    if request.method == "POST":
        print(request.POST)
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'],)
        # models.UserInfo.objects.create(**request.POST)
    user_list_obj = models.UserInfo.objects.all()
    return render(request, "t1.html", {'li': user_list_obj})


def home(request):
    return HttpResponse("app01/home")
