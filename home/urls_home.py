from django.contrib import admin
from django.urls import path
from . import views_home

urlpatterns = [
    path('', views_home.v_index, name='Index'),
    path('add/<str:expense>/<int:amount>/<str:desc>/<str:expdate>', views_home.v_add, name='AddExp'),
    path('add_inc/<str:inc>/<int:amount>/<str:desc>/<str:incdate>', views_home.v_add_inc, name='AddInc'),
    path('update/<int:eid>/<str:expense>/<int:amount>/<str:desc>/<str:expdate>', views_home.v_update, name='UpdateExp'),
    path('update_inc/<int:iid>/<str:inc>/<int:amount>/<str:desc>/<str:incdate>', views_home.v_update_inc, name='UpdateInc'),
    path('delete/<int:expid>/<str:expdate>', views_home.v_delete, name='DeleteExp'),
    path('delete_inc/<int:incid>/<str:incdate>', views_home.v_delete_inc, name='DeleteInc'),
    path('home/<str:sdate>',views_home.v_home,name='Home'),
    path('report/<str:mon>/<str:yr>',views_home.v_report,name="Report"),
    path('find/<str:p_txn_name>' , views_home.v_find , name = "FindTxn" ),
    path('find/' , views_home.v_find , name = "Find" ),
]