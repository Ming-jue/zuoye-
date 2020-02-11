from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django import forms
from api import models

class DetailsModelForm(forms.ModelForm):
    class Meta:
        model = models.Details
        fields = '__all__'

        labels = {
            'title': '标题',
            'image': '封面',
            'preview_start_time': '预展开始时间',
            'preview_end_time': '预展结束时间',
            'auction_start_time': '拍卖开始时间',
            'auction_end_time': '拍卖结束时间',
            'deposit':'全场保证金'

        }
        widgets = {
            'preview_start_time': forms.TextInput(attrs={'type': 'date'}),
            'preview_end_time': forms.TextInput(attrs={'type': 'date'}),
            'auction_start_time': forms.TextInput(attrs={'type': 'date'}),
            'auction_end_time': forms.TextInput(attrs={'type': 'date'}),

        }

        error_messages = {
            'title': {'require': '标题不能为空', },
            'image': {'require': '不能为空', },
            'preview_start_time': {'require': '不能为空', },
            'preview_end_time': {'require': '不能为空', },
            'auction_start_time': {'require': '不能为空', },
            'auction_end_time': {'require': '不能为空', },
            'deposit': {'require': '不能为空', },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():  # 循环所有的字段

            field.widget.attrs.update({'class': 'form-control'})


# 展示拍品页面
def showdetails(request):
    details_obj = models.Details.objects.all()
    return render(request,'showdetails.html',{'details_obj':details_obj})


# 添加页面
def adddetails(request):
    if request.method == 'GET':
        detail_model_obj = DetailsModelForm()
        return render(request,'adddetails.html',{'detail_model_obj':detail_model_obj})
    else:
        detail_model_obj = DetailsModelForm(request.POST)
        if detail_model_obj.is_valid():
            detail_model_obj.save()
            return redirect('showdetails')
        else:
            return render(request,'adddetails.html',{'detail_model_obj':detail_model_obj})


# 删除页面
def deldetails(request):

    data = {'status': 0}
    if request.method == 'POST':

        details_id = request.POST.get('details_id')

        models.Details.objects.filter(pk=details_id).delete()

        data = {'status': 1}
        return JsonResponse(data)
    else:
        details_id = request.GET.get('details_id')
        # print(11111,book_id)
        models.Details.objects.filter(pk=details_id).delete()
        return redirect('showdetails')



# 编辑页面
def editdetails(request,obj_id):
    old_objs = models.Details.objects.filter(pk=obj_id)
    if request.method == 'GET':
        old_obj = old_objs.first()
        return render(request, 'editdetails.html',
                      {'old_obj': old_obj})
    else:
        # authors = request.POST.getlist('authors')
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        # data.pop('authors')

        old_objs.update(**data)
        # old_objs.first().authors.set(authors)
        return redirect('showdetails')
