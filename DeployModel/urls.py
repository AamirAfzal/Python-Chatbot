from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('chatbot/',views.chatbot,name='chatbot'),
    path('chatbotresult/',views.chatbotresult,name='chatbotresult'),
]
