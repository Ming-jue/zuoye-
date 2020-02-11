from django.db import models


class UserInfo(models.Model):
    """用户"""
    telephone = models.CharField(verbose_name='手机号', max_length=11)
    nickname = models.CharField(verbose_name='昵称', max_length=64)
    avatar = models.CharField(verbose_name='头像', max_length=64)
    token = models.CharField(verbose_name='用户Token', max_length=64,null=True,blank=True)


class Topic(models.Model):
    """
    话题
    """
    title = models.CharField(verbose_name='话题', max_length=32)
    count = models.PositiveIntegerField(verbose_name='关注度', default=0)


class News(models.Model):
    """
    动态
    """
    cover = models.CharField(verbose_name='封面', max_length=128)
    content = models.CharField(verbose_name='内容', max_length=255)
    topic = models.ForeignKey(verbose_name='话题', to='Topic', null=True, blank=True)
    address = models.CharField(verbose_name='位置', max_length=128, null=True, blank=True)
    user = models.ForeignKey(verbose_name='发布者', to='UserInfo', related_name='news')

    favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)

    viewer_count = models.PositiveIntegerField(verbose_name='浏览数', default=0)

    comment_count = models.PositiveIntegerField(verbose_name='评论数', default=0)

    create_date = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

class NewsDetail(models.Model):
    """
    动态详细
    """
    key = models.CharField(verbose_name='腾讯对象存储中的文件名', max_length=128, help_text="用于以后在腾讯对象存储中删除")
    cos_path = models.CharField(verbose_name='腾讯对象存储中图片路径', max_length=128)
    news = models.ForeignKey(verbose_name='动态', to='News')


class ViewerRecord(models.Model):
    """
    浏览记录
    """
    news = models.ForeignKey(verbose_name='动态', to='News')
    user = models.ForeignKey(verbose_name='用户', to='UserInfo')


class NewsFavorRecord(models.Model):
    """
    动态赞记录表
    """
    news = models.ForeignKey(verbose_name='动态', to='News')
    user = models.ForeignKey(verbose_name='点赞用户', to='UserInfo')


class CommentRecord(models.Model):
    """
    评论记录表
    """
    news = models.ForeignKey(verbose_name='动态', to='News')
    content = models.CharField(verbose_name='评论内容', max_length=255)
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo')
    create_date = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)

    reply = models.ForeignKey(verbose_name='回复', to='self', null=True, blank=True,related_name='replys')
    depth = models.PositiveIntegerField(verbose_name='评论层级', default=1)
    root = models.ForeignKey(verbose_name='根评论',to='self',null=True,blank=True,related_name="roots")

    favor_count = models.PositiveIntegerField(verbose_name='赞数', default=0)


class CommentFavorRecord(models.Model):
    """
    评论赞记录
    """
    comment = models.ForeignKey(verbose_name='动态', to='CommentRecord')
    user = models.ForeignKey(verbose_name='点赞用户', to='UserInfo')


#################### 拍卖

# 专题名称   拍卖状态   开始时间    围观数     图片   出价   拍品件数



class Acution(models.Model):
    """拍卖展示"""
    status_choices=[
        (1,'预展中'),
        (2,'拍卖中'),
        (3,'已结束')
    ]
    topic = models.CharField(verbose_name='标题',null=True,blank=True,max_length=64)
    status = models.PositiveIntegerField(choices=status_choices,verbose_name='拍卖状态',default=0)
    state_start_time = models.DateTimeField(verbose_name='开拍时间')
    state_end_time = models.DateTimeField(verbose_name='结束时间')
    look_count = models.PositiveIntegerField(verbose_name='围观次数',default=0)
    image = models.CharField('拍卖图',max_length=128)
    lot_count = models.IntegerField(verbose_name='拍品件数',default=0)
    offer = models.IntegerField(verbose_name='出价次数',default=0)




class Details(models.Model):
    """拍品"""
    status_choices=[
        (1,'未开拍'),
        (2,'拍卖中'),
        (3,'成交'),
    ]
    status = models.PositiveIntegerField(verbose_name='状态',choices=status_choices,default=1)
    title = models.CharField(verbose_name='标题',null=True,blank=True,max_length=64)
    start_price = models.PositiveIntegerField(verbose_name='起拍价')
    looks = models.IntegerField(verbose_name='浏览次数',default=0)
    follow = models.ForeignKey(verbose_name='关注',to=UserInfo)
    image = models.CharField(verbose_name='拍品图',max_length=64)
    # Filefield =
    priceup = models.IntegerField(verbose_name='加价幅度',default=100)

    preview_start_time = models.DateTimeField(verbose_name='预展开始时间')
    preview_end_time = models.DateTimeField(verbose_name='预展结束时间',)

    auction_start_time = models.DateTimeField(verbose_name='拍卖开始时间')
    auction_end_time = models.DateTimeField(verbose_name='拍卖结束时间')

    deposit = models.PositiveIntegerField(verbose_name='全场保证金', default=1000)



    def __str__(self):
        return self.title



class NewDetails(models.Model):
    """拍品详情"""
    key = models.CharField(verbose_name='腾讯对象存储中的文件名', max_length=128, help_text="用于以后在腾讯对象存储中删除")
    cos_path = models.CharField(verbose_name='腾讯对象存储中图片路径', max_length=128)
    details= models.ForeignKey(verbose_name='动态',to='Details')



class Payment(models.Model):
    """缴纳保证金"""
    status_choices=[
        (1,'单品'),
        (2,'全场'),
    ]
    status = models.PositiveIntegerField(verbose_name='状态',choices=status_choices,default=1)
    user = models.ForeignKey(verbose_name='出价人',to='UserInfo')
    unit_price= models.ForeignKey(verbose_name='单品保证金',to='Details')
    full_product = models.ForeignKey(verbose_name='全场保证金',to='Acution')



class Browse(models.Model):
    """关注"""
    item = models.ForeignKey(verbose_name='拍品',to='Details')
    username = models.ForeignKey(verbose_name='用户',to='UserInfo')













#
# from django.db import models
#
# # Create your models here.'
#
# """
# 竞拍首页
# """
# Home_status = (
#     (1, "预售中"),
#     (2, "拍卖中"),
#     (3, "已结束"),
# )
#
#
# class CommodityHome(models.Model):
#     status = models.CharField(choices=Home_status, max_length=128, verbose_name='标题')
#     title = models.CharField(max_length=128, verbose_name='标题')
#     showtime = models.DateTimeField(verbose_name='展示时间')
#     endtime = models.DateTimeField(verbose_name='结束时间')
#     home_price = models.IntegerField(verbose_name="全场保证金额")
#     cover = models.CharField(verbose_name='封面', max_length=256)
#     read_count = models.IntegerField(verbose_name='围观次数', default=10)
#     comm_count = models.IntegerField(verbose_name='拍卖数量', default=0)
#     deal_count = models.IntegerField(verbose_name='出价数', default=0)
#
#
# """
# 拍品内容
# """
# show_status = (
#     (1, "未拍卖"),
#     (2, "拍卖中"),
#     (3, "已结束"),
# )
#
#
# class ShowCommodity(models.Model):
#     status = models.CharField(max_length=32, verbose_name='拍品状态', choices=show_status, default=1)
#     read_count = models.IntegerField(verbose_name='围观次数', default=10)
#     home = models.ForeignKey(verbose_name='专场', to="ShowCommodity")
#     max_price = models.IntegerField(verbose_name='最大价格')
#     min_price = models.IntegerField(verbose_name='最小价格')
#     deal_price = models.IntegerField(verbose_name='起拍价格')
#     add_price = models.IntegerField(verbose_name='加价', default=100)
#     payment_price = models.IntegerField(verbose_name='单品保证金额')
#     auction_count = models.IntegerField(verbose_name='出价次数', default=0)
#
#
# """
# 拍品图片
# """
# pic_status = [
#     (1, "轮播"),
#     (2, "详情"),
#     (3, "封面"),
# ]
#
#
# class DetailCommodityPic(models.Model):
#     show_image = models.ForeignKey(verbose_name="关联拍品", to="ShowCommodity")
#     key = models.CharField(verbose_name='文件名', max_length=256)
#     image_path = models.CharField(verbose_name='网络图片地址', max_length=256)
#     status = models.CharField(max_length=32, verbose_name='图片类型', choices=pic_status, default=1)
#
#
# """
# 拍卖记录
# """
#
#
# class AuctionPayment(models.Model):
#     auction_price = models.IntegerField(verbose_name="每次拍卖的价格")
#     show_Auction = models.ForeignKey(verbose_name='关联拍品', to="ShowCommodity")
#     auction_user = models.ForeignKey(verbose_name="出价人", to="api.UserInfo")
#
#
# """
#
# 保证金
# 保证记录
# 单品保证金
# 全场保证金
# """
#
# payment_status = (
#
#     (1, "单品保证金"),
#     (2, "全场保证金"),
#
# )
#
#
# class Payment(models.Model):
#     status = models.CharField(verbose_name='保证金类型', max_length=256, choices=payment_status)
#     show_Payment = models.ForeignKey(verbose_name='关联单品', to="ShowCommodity", null=True, blank=True)
#     auction_user = models.ForeignKey(verbose_name="保证人", to="api.UserInfo")
#     home_payment = models.ForeignKey(verbose_name='关联全场', to="CommodityHome", null=True, blank=True)
#
#
# """
# 关注
# """
#
#
# class Focus(models.Model):
#     user_comm = models.ForeignKey(verbose_name='用户', to="api.UserInfo")
#     show_comm = models.ForeignKey(verbose_name='拍品', to="ShowCommodity")












