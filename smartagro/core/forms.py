from django.db import models
from django.forms import ModelForm

from core.models import Machine

# https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-forms-django/

class MachineForm(ModelForm):
	class Meta:
		model = Machine
		fields = ['name', 'model',]
	
	#name = forms.CharField(required=True)
	#model_name = forms.CharField(required=False)
	
	#type = forms.ChoiceField(widget=forms.RadioSelect, choices=MACHINE_TYPES)
	#horsepower = forms.IntegerField(required=False)
	#volume = forms.IntegerField(required=False)
	#width = forms.IntegerField(required=False)
	
	#def save(self):
	#	machine = self.instance
	#	machine.name = self.cleaned_data["name"]
	#	#machine.owner = request.user
	#	
	#	# todo
	#	# take over value from model if set, otherwise set from form data
	
	
		