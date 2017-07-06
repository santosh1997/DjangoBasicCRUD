from django.http import HttpResponse
from django.shortcuts import render
from .models import details
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

def index(request):
	return HttpResponse("<title>login</title><h1>hi santosh</h1>")

def ad(request):
	all_emp = details.objects.all()
	context = {'all_emp' : all_emp}
	return render(request,'index.html',context)
	
def emp(request, id):
	return HttpResponse("<title>emp</title><h1>The Employee ID is : "+str(id)+"</h1>")

def empdel(request, id):
	return HttpResponse("<title>emp</title><h1>The Employee ID : "+str(id)+" is deleted</h1>")

	
class detailsCreate(CreateView):
	model = details
	fields = ['first_name','last_name','ph','mail','department','college','emp_pic','resume']