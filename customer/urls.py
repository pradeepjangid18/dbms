from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^home$',views.home,name='home'),
	url(r'^home/login$',views.login,name='login'),
	url(r'^home/register$',views.register,name='register'),
	url(r'^home/appointment$',views.appointment,name='appointment'),
	url(r'^register_done/$',views.register_done,name='register_done'),
	url(r'^home/appoint_done/$',views.appoint_done,name='appoint_done'),
	url(r'^home/loggedin/$',views.loggedin,name='loggedin'),
	url(r'^home/logout/$',views.logout,name='logout'),
	url(r'^home/appointment_history/$',views.appointment_history,name='appointment_history'),
	url(r'^home/site_history/$',views.site_history,name='site_history'),
	url(r'^home/site_hist/payment_info/$',views.site_hist_pay_info,name='site_hist_pay_info'),
	url(r'^home/site_hist/raw_info/$',views.site_hist_raw_info,name='site_hist_raw_info'),
	url(r'^home/query_asked/$',views.query_asked,name='query_asked'),
	url(r'^home/query/$',views.query,name='query'),
	url(r'^home/cat_l_r/$',views.cat_l_r,name='cat_l_r'),
	url(r'^home/cat_kit/$',views.cat_kit,name='cat_kit'),
	url(r'^home/cat_b_r/$',views.cat_b_r,name='cat_b_r'),
	url(r'^home/cat_k_r/$',views.cat_k_r,name='cat_k_r'),
	url(r'^home/cat_off/$',views.cat_off,name='cat_off'),
]
