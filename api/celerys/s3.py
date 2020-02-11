#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# __author__='杨泽涛'


from celery.result import AsyncResult
from s1 import app

# async = AsyncResult(id="f0b41e83-99cf-469f-9eff-74c8dd600002", app=app)

result_object = AsyncResult(id='f0b41e83-99cf-469f-9eff-74c8dd600002',app=app)
print(result_object)