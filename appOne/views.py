from django.shortcuts import render
from appOne.forms import FeedbackForm
from . import forms
# Create your views here.
def index(request):
	return render(request, 'appOne/index.html')

def flot(request):
	return render(request, 'appOne/flot.html')

def form(request):
	form = FeedbackForm()
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
	return render(request, 'appOne/form.html', {'form':form})