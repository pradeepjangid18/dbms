from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import MySQLdb
import customer.views
import employee.views

import base64
# Create your views here.


db=MySQLdb.connect("localhost","root","45201017","db7")
cr=db.cursor()

def home(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' :
			return render(request,'supadmin_home.html')
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		if request.method == 'POST' :
			Mobno=request.POST['Mobno']
			password=request.POST['password']
			if Mobno=='9826585403' and password=='45201017' :
				request.session['mobno']=Mobno
				request.session['user']='admin'
				return render(request,'supadmin_home.html')
			else :
				return HttpResponse("Invalid login details supplied.")
		else :
				return render(request,'login.html')



def appoint_come(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' :
			q1="""select Name,appointment_database.Mobile_No,Email,Working_Address,Meeting_Address,Date,Discription,appoint_id from appointment_database,customer_database where status='Pending' and customer_database.Mobile_No=appointment_database.Mobile_No """
			cr.execute(q1)
			r1=cr.fetchall()
			print r1
			print "pradeep"
			return render(request,'appoint_come.html',{'appointment':r1})
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def appoint_remove(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST':
			appoint_id=request.POST['apid']
			q1="""update appointment_database set status='Cancel' where appoint_id='%s' """ %(appoint_id)
			cr.execute(q1)
			db.commit()
			return appoint_come(request)
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def appoint_accept(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			appoint_id=request.POST['apid']
			#q1="""update appointment_database set status='Accept' where appoint_id='%s' """ %(appoint_id)
			#cr.execute(q1)
			#db.commit()
			#return appoint_come(request)
			return render(request,'appoint_accept.html',{'appoint_id':appoint_id})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def site_accept(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['siteid']
			location=request.POST['location']
			work_to_do=request.POST['w_t_d']
			deadline=request.POST['deadline']
			q1="""insert into site_database values('%s','%s','%s','%s')""" %(site_id,location,work_to_do,deadline)
			cr.execute(q1)
			db.commit()
			q2="""update appointment_database set status='Accept' where appoint_id='%s' """ %(site_id)
			cr.execute(q2)
			db.commit()
			return appoint_come(request)
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def site_all(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' :
			q1="""select site_id,customer_database.Name,customer_database.Email,appointment_database.Mobile_No,location,work_to_do,deadline from site_database,appointment_database,customer_database where site_id=appoint_id and appointment_database.Mobile_No=customer_database.Mobile_No"""
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'site.html',{'site':r1})
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def site_filter(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			mobno=request.POST['mob']
			q1="""select site_id,customer_database.Name,customer_database.Email,appointment_database.Mobile_No,location,work_to_do,deadline from site_database,appointment_database,customer_database where site_id=appoint_id and appointment_database.Mobile_No='%s' """ %(mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'site.html',{'site':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def site_raw_add(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['site_id']
			return render(request,'site_raw_add.html',{'site_id':site_id})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def site_raw_added(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			name=request.POST['name']
			date=request.POST['date']
			quantity=request.POST['quantity']
			bill_amou=request.POST['bill_amou']
			image=request.FILES["image"].read()
			site_id=request.POST['site_id']
			#q1="""insert into raw_materials(product_name,date_of_supply,quantity,bill_amount,site_no) values('%s','%s','%s','%s','%s') """ %(name,date,quantity,bill_amou,site_id)
			args=(name,date,quantity,bill_amou,image,site_id)
			q1='INSERT INTO raw_materials(product_name,date_of_supply,quantity,bill_amount,image,site_no) VALUES(%s,%s,%s,%s,%s,%s)'
			cr.execute(q1,args)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def site_raw_info(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['site_id']
			q1="""select product_id,product_name,date_of_supply,quantity,bill_amount,image from raw_materials where site_no='%s' """ %(site_id)
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
			return render(request,'site_raw_info.html',{'raw':temp})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def site_payment_info(request) :
	print "pradeep"
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' and request.method == 'POST' :
			site_id=request.POST['site_id']
			print site_id
			print "pradeep"
			q1="""select payment_id,money_taken,date_of_taken from site_payment where site_no='%s' """ %(site_id)
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'site_payment.html',{'payment':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def add_employee(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' :
			return render(request,'add_employee.html')
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)


def added_employee(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' and request.method == 'POST' :
			name=request.POST['name']
			mob=request.POST['mob']
			addr=request.POST['addr']
			salary=request.POST['salary']
			account_no=request.POST['account_no']
			bank_name=request.POST['bank_name']
			ifsc_code=request.POST['ifsc_code']
			password=request.POST['password']
			q1="""insert into employee(Name,Mobile_No,Address,salary,account_no,bank_name,ifsc_code,password) values('%s','%s','%s','%s','%s','%s','%s','%s') """ %(name,mob,addr,salary,account_no,bank_name,ifsc_code,password)
			cr.execute(q1)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def employee_all(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' :
			q1="""select Name,Mobile_No,Address,salary,work_location from employee """
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'employee.html',{'employee':r1})
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def employee_filter(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			mobno=request.POST['mob']
			q1="""select Name,Mobile_No,Address,salary,work_location from employee where Mobile_No='%s' """ %(mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'employee.html',{'employee':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')



def employee_payment_info(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' and request.method == 'POST' :
			mobno=request.POST['mobno']
			q1="""select payment_no,money_given,date_of_given from employee_payment where Mobile_No='%s' """ %(mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'employee_payment.html',{'payment':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')





def employee_payment_form(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' and request.method == 'POST' :
			mobno=request.POST['mobno']
			q1="""select Name,Mobile_No,salary,work_location from employee where Mobile_No='%s' """ %(mobno)
			cr.execute(q1)
			r1=cr.fetchone()
			return render(request,'employee_payment_form.html',{'payment':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def employee_payment_complete(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user'] == 'admin' and request.method == 'POST' :
			mobno=request.POST['mobno']
			amount=request.POST['amount']
			date=request.POST['date']
			q1="""insert into employee_payment (money_given,date_of_given,Mobile_No) values('%s','%s','%s') """ %(amount,date,mobno)
			cr.execute(q1)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def workers_working(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['site_id']
			print site_id
			q1="""select Name,employee.Mobile_No,Address,salary,date_of_start from employee,employee_site_history where work_location='%s' and employee.Mobile_No=employee_site_history.Mobile_No and employee.work_location=employee_site_history.site_id""" %(site_id)
			cr.execute(q1)
			r1=cr.fetchall()
			print r1
			return render(request,'workers_working.html',{'workers_working':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def workers_worked(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['site_id']
			print site_id
			q1="""select Name,employee.Mobile_No,Address,salary,date_of_start,date_of_end from employee,employee_site_history where site_id='%s' and employee.Mobile_No=employee_site_history.Mobile_No """ %(site_id)
			cr.execute(q1)
			r1=cr.fetchall()
			print r1
			return render(request,'workers_worked.html',{'workers_worked':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def assign_work_form(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			name=request.POST['name']
			work_location=request.POST['work_location']
			mobno=request.POST['mobno']
			work_location=str(work_location)
			#s=type(work_location)
			#j=""
			print work_location
			#print s,j
			if work_location!="None" :
				print "pradeep"
				q1="""select customer_database.Name,location,work_to_do,deadline from site_database,appointment_database,customer_database where site_id='%s' and site_id=appoint_id and appointment_database.Mobile_No=customer_database.Mobile_No""" %(work_location)
				cr.execute(q1)
				r1=cr.fetchone()
				q2="""select date_of_start from employee_site_history where Mobile_No='%s' and site_id='%s' and date_of_end IS NULL """ %(mobno,work_location)
				cr.execute(q2)
				r2=cr.fetchone()
				date_of_start=r2[0]
				return render(request,'assign_work_form.html',{'site':r1,'name':name,'work_location':work_location,'mobno':mobno,'date_of_start':date_of_start})
			else :
				print "jangid"	
				q3="""select site_id,customer_database.Name,appointment_database.Mobile_No,location,work_to_do,deadline from site_database,appointment_database,customer_database where site_id=appoint_id and appointment_database.Mobile_No=customer_database.Mobile_No"""
				cr.execute(q3)
				r3=cr.fetchall()
				return render(request,'site_for_assign.html',{'r3':r3,'mobno':mobno})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def assign_work(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['site_id']
			mobno=request.POST['mobno']
			date_of_start=request.POST['start_date']
			date_of_end=request.POST['end_date']
			next_site_no=request.POST['site_mobno']
			q1="""update employee_site_history set date_of_end='%s' where site_id='%s' and Mobile_No='%s' and date_of_start='%s' """ %(date_of_end,site_id,mobno,date_of_start)
			cr.execute(q1)
			db.commit()
			q2="""update employee set work_location=NULL  where Mobile_No='%s' """ %(mobno)
			cr.execute(q2)
			db.commit()
			r3=()
			if next_site_no :
				q3="""select site_id,customer_database.Name,appointment_database.Mobile_No,location,work_to_do,deadline from site_database,appointment_database,customer_database where site_id=appoint_id and appointment_database.Mobile_No='%s' """ %(next_site_no)
				cr.execute(q3)
				r3=cr.fetchall()
			else :
				q4="""select site_id,customer_database.Name,appointment_database.Mobile_No,location,work_to_do,deadline from site_database,appointment_database,customer_database where site_id=appoint_id and appointment_database.Mobile_No=customer_database.Mobile_No"""
				cr.execute(q4)
				r3=cr.fetchall()
			return render(request,'site_for_assign.html',{'r3':r3,'mobno':mobno})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def assigning(request)  :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			mobno=request.POST['mobno']
			site_id=request.POST['site_id']
			date_of_start=request.POST['date_of_start']
			q1="""update employee set work_location='%s' where Mobile_No='%s' """ %(site_id,mobno)
			cr.execute(q1)
			db.commit()
			#print site_id,mobno,"fghjk"
			q2="""insert into employee_site_history(site_id,Mobile_No,date_of_start) values('%s','%s','%s') """ %(site_id,mobno,date_of_start)
			cr.execute(q2)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def work_history(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			mobno=request.POST['mobno']
			#print mobno
			q1="""select employee_site_history.site_id,Name,location,work_to_do,date_of_start,date_of_end from customer_database,appointment_database,site_database,employee_site_history  where employee_site_history.Mobile_No='%s' and employee_site_history.site_id=site_database.site_id and site_database.site_id=appointment_database.appoint_id and appointment_database.Mobile_No=customer_database.Mobile_No """ %(mobno)
			cr.execute(q1)
			r1=cr.fetchall()
			#print r1
			return render(request,'work_history.html',{'work_history':r1})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def employee_query(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' :
			query_of=False
			q1="""select query_id,Name,employee.Mobile_No,query from employee_query,employee where employee_query.Mobile_No=employee.Mobile_No"""
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'query.html',{'query':r1,'query_of':query_of})
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')



def customer_query(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' :
			query_of=True
			q1="""select query_id,Name,customer_database.Mobile_No,query from customer_query,customer_database where customer_query.Mobile_No=customer_database.Mobile_No"""
			cr.execute(q1)
			r1=cr.fetchall()
			return render(request,'query.html',{'query':r1,'query_of':query_of})
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def catalog(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' :
			return render(request,'catalog.html')
		elif request.session['user']=='customer' :
			return customer.views.home(request)
		else :
			return employee.views.home(request)
	else :
		return render(request,'login.html')


def add_catalog(request) :
	print "ganesh"
	print "dfdg"
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST':
			image_type=request.POST['Type']
			print "pradeep"
			image=request.FILES['image'].read()
			args=(image_type,image)
			q1='insert into catalog (image_type,image) values(%s,%s)'
			cr.execute(q1,args)
			db.commit()
			print "pradeep"
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def see_catalog(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			image_type=request.POST['Type']
			q1="""select image_id,image from catalog where image_type='%s' """ %(image_type)
			cr.execute(q1)
			r1=cr.fetchall()
			temp=[]
			for row in r1 :
				x=[]
				x.append(row[0])
				x.append(base64.encodestring(row[1]))
				temp.append(x)
			return render(request,'catalog_see.html',{'image':temp})
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')
 

def del_catalog(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			image_id=request.POST['image_id']
			q1="""delete from catalog where image_id='%s' """ %(image_id)
			cr.execute(q1)
			db.commit()
			return render(request,'catalog.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def del_query(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			query_id=request.POST['query_id']
			q1="""delete from customer_query where query_id='%s' """ %(query_id)
			cr.execute(q1)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


def site_del(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			site_id=request.POST['site_id']
			q1="""delete from site_database where site_id='%s' """ %(site_id)
			cr.execute(q1)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')

def employee_del(request) :
	login_logout=request.session.has_key('mobno')
	if login_logout :
		if request.session['user']=='admin' and request.method=='POST' :
			mobno=request.POST['mobno']
			q1="""delete from employee where Mobile_No='%s' """ %(mobno)
			cr.execute(q1)
			db.commit()
			return render(request,'supadmin_home.html')
		else :
			del request.session['mobno']
			del request.session['user']
			login_logout=False
			return render(request,'home.html',{'login_logout':login_logout})
	else :
		return render(request,'login.html')


