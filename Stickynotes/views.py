# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import date,datetime,timedelta
import calendar

month_name="Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"
month_name=month_name.split()
def index(request):
	return HttpResponse("Test")
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
		if day:
			if day==current_day and current_month==month and current_year==year:
				current=True

		lst[week].append((day,current))
		if len(lst[week]) ==7:
			lst.append([])
			week+=1	
	context_dict['month_days']=lst
	return render_to_response("Stickynotes/month.html",context_dict,context)			
