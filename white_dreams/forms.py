from django import forms

from .models import Title,Write

class TitleForm(forms.ModelForm):
	class Meta:
		model = Title
		fields = ['text']
		labels = {'text': ''}

class WriteForm(forms.ModelForm):
	class Meta:
		model = Write
		fields = ['text']
		labels = {'text': ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}
