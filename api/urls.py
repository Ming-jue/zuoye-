from django.conf.urls import url

from api.views import news
from api.views import auth
from api.views import auction
from api.views import task
urlpatterns = [
    url(r'^message/', auth.MessageView.as_view()),
    url(r'^login/', auth.LoginView.as_view()),
    url(r'^topic/$', news.TopicView.as_view()),

    url(r'^news/$', news.NewsView.as_view()),
    url(r'^news/(?P<pk>\d+)/$', news.NewsDetailView.as_view()),
    url(r'^comment/$', news.CommentView.as_view()),


    url(r'^auctions/$', auction.AuctionsView.as_view()),
    url(r'^details/$', auction.DetailsView.as_view()),
    url(r'^newdetails/(?P<pk>\d+)/$', auction.NewDetailsView.as_view()),
    url(r'^payment/$', auction.PaymentView.as_view()),

    url(r'^create/task/$', task.create_task),
    url(r'^get/result/$', task.get_result),

]



