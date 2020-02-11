#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# __author__='杨泽涛'


from celery import Celery

app = Celery('tasks', broker='redis://192.168.16.27:6379', backend='redis://192.168.16.27:6379')


@app.task
def x1(x, y):

    return x + y