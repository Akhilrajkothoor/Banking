from django.urls import path
from . import views

urlpatterns =[
    path('member/add/',views.create_view,name='add'),
    path('member/ajax/load-branchs/',views.load_branchs,name='ajax_load_branchs'),
]