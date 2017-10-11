from django import forms
from django.core import validators
from appOne.models import Feedback
def checkfor5(value):
	if value > 5 or value < 1:
		raise forms.ValidationError('POINTS MUST BE IN THE RANGE 1 TO 5.')
class FeedbackForm(forms.ModelForm):
	fac = forms.CharField(max_length=128, widget = forms.TextInput(attrs={'placeholder':'Prof. ABC XYZ'}), required=True, label='Name of the Faculty Member:')
	subject = forms.CharField(max_length=128, widget = forms.TextInput(attrs={'placeholder':'AM 3'}), required=True ,label='Subject:')
	res1 = forms.IntegerField(required=True, validators=[checkfor5], label='Abilities to understand student"s difficulties and willingness to help them')
	res2 = forms.IntegerField(required=True, validators=[checkfor5], label='Commitment to academic work in the class')
	res3 = forms.IntegerField(required=True, validators=[checkfor5], label='Regularity and Punctuality')
	res4 = forms.IntegerField(required=True, validators=[checkfor5], label='Interaction in the class')
	res5 = forms.IntegerField(required=True, validators=[checkfor5], label='Coverage of syllabus')
	res6 = forms.IntegerField(required=True, validators=[checkfor5], label='Planning of lessons throughout the Semester')
	res7 = forms.IntegerField(required=True, validators=[checkfor5], label='Effective communication of subject matter')
	res8 = forms.IntegerField(required=True, validators=[checkfor5], label='Management of lecture and class control')
	res9 = forms.IntegerField(required=True, validators=[checkfor5], label='Overall ability to maintain sancity of Teaching - Learning process')
	sug = forms.CharField(widget=forms.Textarea,required=False, label='Any other suggestions')
	class Meta():
		model = Feedback
		fields = '__all__'