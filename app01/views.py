from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.


##获取单表数据三种方法
def business(request):
    v1 = models.Business.objects.all()
    #QuerySet
    #[obj(id,caption,code),obj(id,caption,code),obj(id,caption,code)]

    v2 = models.Business.objects.all().values('id','caption')
    # QuerySet
    # [{'id':1,'caption':'xxxx'},{},{}]

    v3 = models.Business.objects.all().values_list('id', 'caption')
    # QuerySet
    # [(1,运维部),(),()]
    return render(request,'business.html',{'v1':v1,'v2':v2,'v3':v3})


# def host(request):
#     v1 = models.Host.objects.filter(nid__gt=0)
#     # QuerySet [hostobj(ip.host,另外一个对象(...)),]
#     for row in v1:
#         # 这里用.跨表查询
#         print(row.nid,row.hostname,row.ip,row.port,row.b_id,row.b.caption,row.b.code,row.b.id,sep='\t')
#
#         # print(row.b.fk.name)
#     #    return HttpResponse('HOST')
#
#     v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
#     # QuerySet [{}] 获取的字典
#
#     # 这里用__跨表查询
#     # print(v2)
#     for row in v2:
#         print(row['nid'],row['hostname'],row['b_id'],row['b__caption'])
#
#
#     v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')
#     # QuerySet [(),] 获取的是元组
#     print(v3)
#
#
#     return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3})


def host(request):
    if request.method == 'GET':
        v1 = models.Host.objects.filter(nid__gt=0)
        v2 = models.Host.objects.filter(nid__gt=0).values('nid', 'hostname', 'b_id', 'b__caption')
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'b_id', 'b__caption')

        b_list = models.Business.objects.all()

        return render(request,'host.html',{'v1':v1,'v2':v2,'v3':v3,'b_list':b_list})

    elif request.method == 'POST':
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        # models.Host.objects.create(hostname=h,ip=i,port=p,b=models.Business.objects.get(id=b))
        models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)

        # return render(request,'host.html')
        return redirect('/host')


def test_ajax(request):
    # # print(request.method,request.GET.get('user'),request.GET.get('pwd'),sep='\t')
    # print(request.method, request.POST, sep='\t')
    # import time
    # time.sleep(3)
    # return HttpResponse('门带上了')
    import json
    ret = {'status': True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h)>5:
            models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
            # return HttpResponse('OK')
            #
        else:
            # return HttpResponse('主机名太短')
            ret['status'] = False
            ret['error'] = '主机名太短'
    except Exception as e:
        ret['status'] = False
        # ret['error'] = str(e)
        ret['error'] = '请求错误'

    return HttpResponse(json.dumps(ret))
    # ajax 请求返回只能是HttpResponse
