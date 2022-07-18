from . import views
from django.urls import path
app_name="bankapp1"

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('add_bank_details/',views.add_bank_details,name='add_bank_details'),
    # path('member/add/',views.create_view,name='add'),
    # path('member/ajax/load-branchs/',views.load_branchs,name='ajax_load_branchs'),
    path('done/',views.done,name='done'),





    ]