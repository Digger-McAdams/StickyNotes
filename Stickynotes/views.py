# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from datetime import date,datetime,timedelta
import calendar
def index(request):
	return HttpResponse("Test")
def month(request):
	context=RequestContext(request)
	context_dict={}
	month=datetime.now().month
	year=datetime.now().year	
	cal=calendar.Calendar(6)
	month_days=cal.itermonthdays(year,month)#how many days are in the month
	context_dict['month']=month
	context_dict['year']=year
	lst=[[]]
	week=0
	for day in month_days:
		lst[week].append((day))
		if len(lst[week]) ==7:
			lst.append([])
			week+=1	
	context_dict['month_days']=lst
	return render_to_response("Stickynotes/month.html",context_dict,context)			
