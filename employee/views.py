from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import MySQLdb
from datetime import datetime
# Create your views here.

db=MySQLdb.connect("localhost","root","45201017","db7")
cr=db.cursor()

def home(request) :
	if request.method=='POST' :
			Mobno=request.POST['Mobno']
			password=request.POST['password']
			q1=""" select Name from employee where Mobile_No='%s' and password='%s' """ %(Mobno,password)
			cr.execute(q1)
			r1=cr.fetchall()
			if len(r1) != 0 :
				request.session['mobno']=Mobno
				request.session['user']='employee'
				name=r1[0][0]
				login_logout=True
				return render(request,'employee_home.html',{'name':name})
			else :
				return HttpResponse("Invalid login details supplied.")
	else :
		login_logout=request.session.has_key('mobno')
		if login_logout :
			 if request.session['user']=='employee' :
			 	Mobno=request.session['mobno']
			 	q2=""" select Name from employee where Mobile_No='%s' """ %(Mobno)
			 	cr.execute(q2)
			 	r2=cr.fetchall()
			 	name=r2[0][0]
			 	return render(request,'employee_home.html',{'name':name})
			 else :
			 	del request.session['user']
			 	del request.session['mobno']
			 	login_logout=False
			 	return render(request,'home.html',{'login_logout':login_logout})
		else :
			return render(request,'login.html')

def profile(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='employee' :
			mob=request.session['mobno']
			q1="""select Name,Mobile_No,Address,salary,work_location,account_no,bank_name,ifsc_code,password from employee where Mobile_No='%s' """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			name=r1[0][0]
			print r1
			return render(request,'employee_profile.html',{'profile':r1,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')

def employee_hist_pay_info(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='employee':
			mob=request.session['mobno']
			#siteid=request.POST['site_id']
			q1="""select payment_no,money_given,date_of_given from employee_payment where Mobile_No='%s' """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			q2="""select Name from employee where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'employee_hist_pay.html',{'pay_info':r1,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')

def work_history(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='employee' :
			mob=request.session['mobno']
			q1="""select employee_site_history.site_id,Name,location,work_to_do,date_of_start,date_of_end from customer_database,appointment_database,site_database,employee_site_history  where employee_site_history.Mobile_No='%s' and employee_site_history.site_id=site_database.site_id and site_database.site_id=appointment_database.appoint_id and appointment_database.Mobile_No=customer_database.Mobile_No """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			q2="""select Name from employee where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'employee_work_history.html',{'work_history':r1,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')

def query(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='employee' and request.method=='POST' :
			mob=request.session['mobno']
			enquiry=request.POST['enquiry']
			q1="""insert into employee_query (Mobile_No,query) values('%s','%s')""" %(mob,enquiry)
			cr.execute(q1)
			db.commit()
			q2="""select Name from employee where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			q3="""select query_id,query from employee_query where Mobile_No='%s' """ %(mob)
			cr.execute(q3)
			r3=cr.fetchall()
			return render(request,'employee_hist_query.html',{'query':r3,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')

def query_asked(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='employee' :
			mob=request.session['mobno']
			q1="""select query_id,query from employee_query where Mobile_No='%s' """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			q2="""select Name from employee where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'employee_hist_query.html',{'query':r1,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')

