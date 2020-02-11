from django.conf.urls import url
from web01 import views

urlpatterns = [
    url(r'^showdetails/$',views.showdetails,name='showdetails'),
    url(r'^adddetails/$',views.adddetails,name='adddetails'),
    url(r'^deldetails/$',views.deldetails,name='deldetails'),
    url(r'^editdetails/(\d+)/$',views.editdetails,name='editdetails'),

]