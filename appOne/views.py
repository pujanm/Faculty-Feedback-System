from django.shortcuts import render
# Create your views here.
def index(request):
	return render(request, 'appOne/index.html')

def flot(request):
	return render(request, 'appOne/flot.html')

def form(request):
	return render(request, 'appOne/form.html')
