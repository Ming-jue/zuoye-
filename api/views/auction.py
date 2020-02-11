#! /usr/bin/env/python
# -*- coding:utf-8 -*-
# __author__='杨泽涛'

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView
from rest_framework import status
from api import models
from django.forms import model_to_dict
from utils.filters import MaxFilterBackend, MinFilterBackend
from utils.pagination import OldBoyLimitPagination

# 拍卖首页展示
class AuctionsModelSerializer(serializers.ModelSerializer):
    state_start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    state_end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = models.Acution
        fields = "__all__"


class AuctionsView(ListAPIView):
    serializer_class = AuctionsModelSerializer
    queryset = models.Acution.objects.all()

    pagination_class = OldBoyLimitPagination
    filter_backends = [MinFilterBackend, MaxFilterBackend]

# 拍卖页


class DetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Details
        fields = "__all__"


class DetailsView(ListAPIView):
    serializer_class = DetailsModelSerializer
    queryset = models.Details.objects.all().order_by('-id')
    pagination_class = OldBoyLimitPagination
    filter_backends = [MinFilterBackend, MaxFilterBackend]


class NewsDetailsModelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    # title = serializers.SerializerMethodField()
    look_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Details
        exclude = ['follow']

    def get_image(self,obj):
        detail_queryset = models.NewDetails.objects.filter(details=obj)
        # print([model_to_dict(row,['id','cos_path']) for row in detail_queryset])
        return [model_to_dict(row,['id','cos_path']) for row in detail_queryset]


    # def get_title(self,obj):
    #     if not obj.title:
    #         return
    #     return model_to_dict(obj.title,fields=['id','title'])

    def get_look_count(self,obj):
        look_queryset = models.NewDetails.objects.filter(details=obj)
        print(look_queryset)


class NewDetailsView(RetrieveAPIView):
    queryset = models.Details.objects.all()
    serializer_class = NewsDetailsModelSerializer



class TopicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Topic
        fields = "__all__"



class TopicView(ListAPIView):
    serializer_class = TopicModelSerializer
    queryset = models.Topic.objects.all().order_by('-id')

    pagination_class = OldBoyLimitPagination
    filter_backends = [MinFilterBackend, MaxFilterBackend]




class PaymentModelSerializer(serializers.ModelSerializer):
    unit_price = serializers.SerializerMethodField()
    class Meta:
        model = models.Payment
        fields = "__all__"

    def get_unit_price(self,obj):
        payment_price = models.Payment.objects.filter(unit_price_id=obj.id)
        print(payment_price)

class PaymentView(ListAPIView):
    queryset = models.Payment.objects.all()

    serializer_class = PaymentModelSerializer




