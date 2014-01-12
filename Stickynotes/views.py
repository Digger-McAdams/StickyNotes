# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date,datetime,timedelta
from Stickynotes.models import Entry
from Stickynotes.forms import EntryForm
from Stickynotes.forms import UserForm
import calendar

month_name="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
month_name=month_name.split()

def index(request):
	return HttpResponse("Test")
@login_required
def month(request,year=datetime.now().year,month=datetime.now().month,button=None):
	context=RequestContext(request)
	context_dict={}
	year=int(year)
	month=int(month)
	if button in ("prev", "next"):
		now=date(year,month,15)
		mdelta=timedelta(days=31)
		if button=="next":
			mod=mdelta
		elif button=="prev":
			mod=-mdelta
		year,month=(now+mod).timetuple()[:2]
	current_month=datetime.now().month
	month_spell=month_name[month-1]
	current_year=datetime.now().year	
	current_day=datetime.now().day
	cal=calendar.Calendar(6)
	month_days=cal.itermonthdays(year,month)#how many days are in the month
	context_dict['month']=month
	context_dict['year']=year
	context_dict['month_spell']=month_spell
	lst=[[]]
	week=0
	for day in month_days:
		current=False
		entries=False
		if day:
			entries=Entry.objects.filter(date__year=year,date__month=month,date__day=day)
			if day==current_day and current_month==month and current_year==year:
				current=True

		lst[week].append((day,current,entries))
		if len(lst[week]) ==7:
			lst.append([])
			week+=1
	context_dict['month_days']=lst
	return render_to_response("Stickynotes/month.html",context_dict,context)			
@login_required
def add_entry(request):
	context=RequestContext(request)
	
	if request.method=='POST':
		form=EntryForm(request.POST)
		if form.is_valid():
			uid=User.objects.get(username=request.user)
			entry=form.save(commit=False)
			entry.user=uid
			entry.save()
			return redirect('/calendar/month')
		else:
			print form.errors
	else:
		form=EntryForm()
	return render_to_response('Stickynotes/add_entry.html',{'form':form},context)
@login_required
def completed_entry(request):
	context=RequestContext(request)
	entry_id=None
	if request.method=='GET':
		entry_id=request.GET['entry_id']
	e=Entry.objects.get(id=int(entry_id))
	if e:
		e.completed=True
		e.save()
	return HttpResponse()
@login_required
def delete_entry(request):
	context=RequestContext(request)
	entry_id=None
	if request.method=='GET':
		entry_id=request.GET['entry_id']
	e=Entry.objects.get(id=int(entry_id))
	if e:
		e.delete()
	return HttpResponse()
def register(request):
	context=RequestContext(request)
	registered=False
	if request.method =='POST':
		user_form=UserForm(data=request.POST)
		if user_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True
		else:
			print user_form.errors
	else:
		user_form=UserForm()
	return render_to_response('Stickynotes/register.html',{'user_form':user_form,'registered':registered},context)	
def user_login(request):
	context=RequestContext(request)
	if request.method == 'POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/calendar/month')
			else:
				return HttpResponse("Account is disabled.")
		else:
			print "Invalid login details:{0}, {1}".format(username,password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('Stickynotes/login.html',{},context)
	
