from django import forms
from Stickynotes.models import Entry

class EntryForm(forms.ModelForm):
	message=forms.CharField(max_length=40, help_text="Please enter your reminder")
	date=forms.DateTimeField(input_formats=['%m-%d-%Y'], help_text="Please enter the date for entry")
	priority=forms.ChoiceField(Entry.priority_choices,help_text="Please enter the priority of the entry")
	class Meta:
		model=Entry
