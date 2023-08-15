from django.contrib import admin
from django.urls import path
from home import views



urlpatterns = [
    path("",views.homepage , name="homepage"),
    path("index.html",views.homepage , name="homepage"),
    path("contact.html",views.contacts , name="contacts"),
    path("ques1.html",views.ques1 , name="ques1"),
    path("ques2.html",views.ques2 , name="ques2"),
    path("ques3.html",views.ques3 , name="ques3"),
    path("ques4.html",views.ques4 , name="ques4"),
    path("ques5.html",views.ques5 , name="ques5"),
    path("ques6.html",views.ques6 , name="ques6"),
    path("ques7.html",views.ques7 , name="ques7"),
    path("ques8.html",views.ques8 , name="ques8"),
    path("ques9.html",views.ques9 , name="ques9"),
    path("ques10.html",views.ques10 , name="ques10"),
    path("final.html",views.final , name="final"),
    path("final2.html",views.final2 , name="final2"),
    path('video_stream/', views.video_stream, name='video_stream'),
]