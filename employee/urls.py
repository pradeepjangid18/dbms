from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^home/$',views.home,name='home'),
	url(r'^profile/$',views.profile,name='profile'),
	url(r'^payment_info/$',views.employee_hist_pay_info,name='payment_info'),
	url(r'^work_history/$',views.work_history,name='work_history'),
	url(r'^query_asked/$',views.query_asked,name='query_asked'),
	url(r'^query/$',views.query,name='query'),
]