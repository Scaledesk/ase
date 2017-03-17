from django.conf.urls import url
from.import views
from core.views import *

		# from django.conf.urls import patterns, include, url

urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^$', index),
    url(r"^register/", CreateUser),
    url(r"^login/",login),
    url(r"^logout/",logout_view),
    url(r"^dashboard/",dashboard),
    url(r"^update/",update),
    url(r"^project/",project),
    url(r"^question/",QuestionView),
    url(r"^discussions/",Discussions),
    url(r'^answerupdate/(?P<id>[0-9]+)/$', AnswerUpdate, name='answerupdate'),
    url(r'^answerdelete/(?P<id>[0-9]+)/', AnswerDelete, name='answerdelete'),
    url(r'^questiondelete/(?P<id>[0-9]+)/', QuestionDelete, name='questiondelete'),
    url(r'^answer/', SendAnswer),
    url(r"^home/",Home),
    url(r"^signup/",Signup),
    url(r"^setting/",password),
    url(r"^questionList/",QuestionList),

    # url(r"^singleprofile/", SingleProfile),
    url(r"^menberlist/", ProfileList),
    url(r'^profiledetails/(?P<id>[0-9]+)/', ProfileDetails),
    url(r"^mailSend/", mailSend),
    url(r"^search/", Search),


]
