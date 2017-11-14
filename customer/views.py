from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import MySQLdb
from datetime import datetime
import employee.views
# Create your views here.
import base64
import hashlib

db=MySQLdb.connect("localhost","root","45201017","db7")
cr=db.cursor()

salt = 'pradeepsweets'.encode('utf_8')

def home(request) :
	login_logout=request.session.has_key('mobno')
	name='name_'
	if login_logout :
		if request.session['user']=='customer' :
			Mobno=request.session['mobno']
			q1=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			name=r1[0][0]
			return render(request,'home.html',{'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'home.html',{'login_logout':login_logout,'name':name})


def cat_l_r(request) :
	login_logout=request.session.has_key('mobno')
	name='name'
	headline="Catalog for Living Room : -"
	q1="""select image from catalog where image_type='living_room' """
	cr.execute(q1)
	r1=cr.fetchall()
	temp=[]
	for row in r1 :
		x=[]
		x.append(base64.encodestring(row[0]))
		temp.append(x)
	if login_logout :
		if request.session['user']=='customer' :
			Mobno=request.session['mobno']
			q2=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})

def cat_kit(request) :
	login_logout=request.session.has_key('mobno')
	name='name'
	headline="Catalog for Kitchen : -"
	q1="""select image from catalog where image_type='kitchen' """
	cr.execute(q1)
	r1=cr.fetchall()
	print "ppradep"
	temp=[]
	for row in r1 :
		x=[]
		x.append(base64.encodestring(row[0]))
		temp.append(x)
	if login_logout :
		if request.session['user']=='customer' :
			Mobno=request.session['mobno']
			q2=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		print "akf"
		return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})



def cat_b_r(request) :
	login_logout=request.session.has_key('mobno')
	name='name'
	headline="Catalog for Bed Room : -"
	q1="""select image from catalog where image_type='bed_room' """
	cr.execute(q1)
	r1=cr.fetchall()
	temp=[]
	for row in r1 :
		x=[]
		x.append(base64.encodestring(row[0]))
		temp.append(x)
	if login_logout :
		if request.session['user']=='customer' :
			Mobno=request.session['mobno']
			q2=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})


def cat_k_r(request) :
	login_logout=request.session.has_key('mobno')
	name='name'
	headline="Catalog for Kid Room : -"
	q1="""select image from catalog where image_type='kid_room' """
	cr.execute(q1)
	r1=cr.fetchall()
	temp=[]
	for row in r1 :
		x=[]
		x.append(base64.encodestring(row[0]))
		temp.append(x)
	if login_logout :
		if request.session['user']=='customer' :
			Mobno=request.session['mobno']
			q2=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})



def cat_off(request) :
	login_logout=request.session.has_key('mobno')
	name='name'
	headline="Catalog for Office : -"
	q1="""select image from catalog where image_type='office' """
	cr.execute(q1)
	r1=cr.fetchall()
	temp=[]
	for row in r1 :
		x=[]
		x.append(base64.encodestring(row[0]))
		temp.append(x)
	if login_logout :
		if request.session['user']=='customer' :
			Mobno=request.session['mobno']
			q2=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'catalog_customer.html',{'headline':headline,'image':temp,'login_logout':login_logout,'name':name})


def login(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		name='name_'
		if request.session['user']=='customer':
			Mobno=request.session['mobno']
			q1=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			name=r1[0][0]
			return render(request,'loggedin.html',{'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			name='Admin'
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')

def register(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		name='name_'
		if request.session['user']=='customer':
			Mobno=request.session['mobno']
			q1=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			name=r1[0][0]
			return render(request,'loggedin.html',{'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			name='Admin'
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'register.html')

def appointment(request) :
	login_logout=request.session.has_key('mobno')
	name='name_'
	if login_logout :
		if request.session['user']=='customer':
			Mobno=request.session['mobno']
			q1=""" select Name from customer_database where Mobile_No='%s' """ %(Mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			name=r1[0][0]
			return render(request,'appointment.html',{'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin':
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'appointment.html',{'login_logout':login_logout,'name':name})


def logout(request) :
	try :
		del request.session['mobno']
		del request.session['user']
	except :
		pass
	login_logout=False
	return render(request,'home.html',{'login_logout':login_logout})


def register_done(request) :
	if request.method == 'POST' :
		name=request.POST['name']
		email=request.POST['E-mail']
		mobileno=request.POST['mob']
		address=request.POST['addr']
		password=request.POST['password']
		q1="""select Email from customer_database where Email='%s' """ %(email)
		q2="""select Mobile_No from customer_database where Mobile_No='%s' """ %(mobileno)
		cr.execute(q1)
		r1=cr.fetchall()
		cr.execute(q2)
		r2=cr.fetchall()
		if len(r1)!=0 and len(r2)!=0 :
			return render(request,'mob_email_reg.html')
		elif len(r1)!=0 :
			return render(request,'email_reg.html')
		elif len(r2)!=0 :
			return render(request,'mob_reg.html')
		else :
			password=password.encode('utf-8')
			password=hashlib.sha256 (salt+password).hexdigest()
			cr.execute("""insert into customer_database values('%s','%s','%s','%s','%s')""" %(name,email,mobileno,address,password))
			db.commit()
			return render(request,'reg_done.html')
	else :
		login_logout=False
		return render(request,'home.html',{'login_logout':login_logout})


def loggedin(request) :
	if request.method == 'POST' :
		Mobno=request.POST['Mobno']
		password=request.POST['password']
		password=password.encode('utf-8')
		password=hashlib.sha256 (salt+password).hexdigest()
		q1=""" select Name from customer_database where Mobile_No='%s' and password='%s' """ %(Mobno,password)
		cr.execute(q1)
		r1=cr.fetchall()
		if len(r1) !=0 :
			request.session['mobno']=Mobno
			request.session['user']='customer'
			name=r1[0][0]
			login_logout=True
			return render(request,'loggedin.html',{'login_logout':login_logout,'name':name})
		else :
			print "Invalid login details: {0}, {1}".format(Mobno,password)
			return HttpResponse("Invalid login details supplied.")
	else :
		return login(request)
	




def appoint_done(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' :
			if request.method== 'POST' :
				#name=request.POST['name']
				mob=request.session['mobno']
				#emailid=request.POST['emailid']
				wadd=request.POST['wadd']
				madd=request.POST['madd']
				date=str(datetime.now().date())
				discription=request.POST['discription']
				status='Pending'
				q1="""select Mobile_No from appointment_database where Mobile_No='%s' and status='Pending' """ %(mob)
				cr.execute(q1)
				r1=cr.fetchall()
				flag=True
				if len(r1)!=0 :
					flag=False
				else :
					q3="""insert into appointment_database(Mobile_No,Working_Address,Meeting_Address,Date,Discription,status) values('%s','%s','%s','%s','%s','%s')""" %(mob,wadd,madd,date,discription,status) 
					cr.execute(q3)
					db.commit()
				q4=""" select Name from customer_database where Mobile_No='%s' """ %(mob)
				cr.execute(q4)
				r2=cr.fetchall()
				name=r2[0][0]
				return render(request,'appoint_done.html',{'flag':flag,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')



def appointment_history(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' :
			mob=request.session['mobno']
			q1="""select appoint_id,Working_Address,Meeting_Address,Date,Discription,status from appointment_database where Mobile_No='%s' """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			q2=""" select Name from customer_database where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'appoint_hist.html',{'appoint_hist':r1,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')

def site_history(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' :
			mob=request.session['mobno']
			q1="""select site_id,location,work_to_do,deadline from appointment_database,site_database where site_id=appoint_id and Mobile_No='%s' """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			q2="""select Name from customer_database where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'site_hist.html',{'site_hist':r1,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def site_hist_pay_info(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' and request.method=='POST':
			mob=request.session['mobno']
			siteid=request.POST['site_id']
			q1="""select payment_id,money_taken,date_of_taken from site_payment where site_no='%s' """ %(siteid)
			cr.execute(q1)
			r1=cr.fetchall()
			q2="""select Name from customer_database where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'site_hist_pay.html',{'pay_info':r1,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def site_hist_raw_info(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' and request.method=='POST':
			mob=request.session['mobno']
			siteid=request.POST['site_id']
			q1="""select product_id,product_name,date_of_supply,quantity,bill_amount,image from raw_materials where site_no='%s' """ %(siteid)
			cr.execute(q1)
			r1=cr.fetchall()
			temp=[]
			for row in r1 :
				x=[]
				x.append(row[0])
				x.append(row[1])
				x.append(row[2])
				x.append(row[3])
				x.append(row[4])
				x.append(base64.encodestring(row[5]))
				temp.append(x)
			q2="""select Name from customer_database where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'site_hist_raw.html',{'raw_info':temp,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def query(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' and request.method=='POST' :
			mob=request.session['mobno']
			enquiry=request.POST['enquiry']
			q1="""insert into customer_query (Mobile_No,query) values('%s','%s')""" %(mob,enquiry)
			cr.execute(q1)
			db.commit()
			q2="""select Name from customer_database where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			q3="""select query_id,query from customer_query where Mobile_No='%s' """ %(mob)
			cr.execute(q3)
			r3=cr.fetchall()
			return render(request,'customer_hist_query.html',{'query':r3,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')


def query_asked(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='customer' :
			mob=request.session['mobno']
			q1="""select query_id,query from customer_query where Mobile_No='%s' """ %(mob)
			cr.execute(q1)
			r1=cr.fetchall()
			q2="""select Name from customer_database where Mobile_No='%s' """ %(mob)
			cr.execute(q2)
			r2=cr.fetchall()
			name=r2[0][0]
			return render(request,'customer_hist_query.html',{'query':r1,'login_logout':login_logout,'name':name})
		elif request.session['user']=='admin' :
			return render(request,'superadmin_home.html')
		else :
			return customer.views.home(request)
	else :
		return render(request,'login.html')