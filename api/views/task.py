#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# __author__='杨泽涛'


from django.shortcuts import HttpResponse
from api.tasks import add

def create_task(request):

    print('请求来了')
    result = add.delay(2,2)
    print('执行完毕')
    return HttpResponse(result.id)


def get_result(request):
    nid = request.GET.get('nid')
    from celery.result import AsyncResult
    # from demos.celery import app
    from demos import celery_app
    result_object = AsyncResult(id=nid, app=celery_app)
    # print(result_object.status)
    data = result_object.get()
    return HttpResponse(data)