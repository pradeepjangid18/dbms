from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^home/$',views.home,name='home'),
	url(r'^home/appoint_come/',views.appoint_come,name='appoint_come'),
	url(r'^home/appoint_accept/',views.appoint_accept,name='appoint_accept'),
	url(r'^home/appoint_remove/',views.appoint_remove,name='appoint_remove'),
	url(r'^home/site_accept/',views.site_accept,name='site_accept'),
	url(r'^home/site_all/',views.site_all,name='site_all'),
	url(r'^home/site_filter/',views.site_filter,name='site_filter'),
	url(r'^home/site/raw_add/',views.site_raw_add,name='site_raw_add'),
	url(r'^home/site/raw_added/',views.site_raw_added,name='site_raw_added'),
	url(r'^home/site/raw_info/',views.site_raw_info,name='site_raw_info'),
	url(r'^home/site/payment_info/',views.site_payment_info,name='site_payment_info'),
	url(r'^home/site/workers_working/',views.workers_working,name='workers_working'),
	url(r'^home/site/workers_worked/',views.workers_worked,name='workers_worked'),
	url(r'^home/site/site_del/',views.site_del,name='site_del'),
	url(r'^home/employee/employee_del/',views.employee_del,name='employee_del'),
	url(r'^home/add_employee/',views.add_employee,name='add_employee'),
	url(r'^home/added_employee/',views.added_employee,name='added_employee'),
	url(r'^home/employee_all/',views.employee_all,name='employee_all'),
	url(r'^home/employee_filter/',views.employee_filter,name='employee_filter'),
	url(r'^home/employee/payment_info',views.employee_payment_info,name='employee_payment_info'),
	url(r'^home/employee/payment_form',views.employee_payment_form,name='employee_payment_form'),
	url(r'^home/employee/employee_payment_complete',views.employee_payment_complete,name='employee_payment_complete'),
	url(r'^home/employee/assign_work_form',views.assign_work_form,name='assign_work_form'),
	url(r'^home/employee/assign_work',views.assign_work,name='assign_work'),
	url(r'^home/employee/assigning',views.assigning,name='assigning'),
	url(r'^home/employee/work_history',views.work_history,name='work_history'),
	url(r'^home/employee_query',views.employee_query,name='employee_query'),
	url(r'^home/customer_query',views.customer_query,name='customer_query'),
	url(r'^home/catalog',views.catalog,name='catalog'),
	url(r'^home/add_catalog/',views.add_catalog,name='add_catalog'),
	url(r'^home/see_catalog',views.see_catalog,name='see_catalog'),
	url(r'^home/del_catalog',views.del_catalog,name='del_catalog'),
	url(r'^home/del_query',views.del_query,name='del_query'),
]