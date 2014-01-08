from django import forms
from Stickynotes.models import Entry
from django.forms.extras.widgets import SelectDateWidget
import datetime
class EntryForm(forms.ModelForm):
	message=forms.CharField(max_length=40, help_text="Please enter your reminder")
	day=forms.DateField(widget=SelectDateWidget(), help_text="Please enter the date for entry",initial=datetime.date.today)
	priority=forms.ChoiceField(Entry.priority_choices,help_text="Please enter the priority of the entry")
	class Meta:
		model=Entry
		fields=('message','day','priority')
