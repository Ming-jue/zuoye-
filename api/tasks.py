#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# __author__='杨泽涛'

from celery import shared_task

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y