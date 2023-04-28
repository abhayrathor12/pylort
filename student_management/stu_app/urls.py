from django.urls import path
from . views import *
urlpatterns = [
    path('',index,name='index'),
    path('all_stu',all_stu,name='all_stu'),
    path('add_stu',add_stu,name='add_stu'),
    path('rem_stu',rem_stu,name='rem_stu'),
    path('remove_stu/<int:stu_id>',remove_stu,name='remove_stu'),
    path('fil_stu',fil_Stu,name='fil_stu'),
]
