from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Welcome to Meeting index view!")

def meeting(request, meeting_id):
	return HttpResponse("Meeting: %s." % meeting_id)

def participants(request, meeting_id):
	return HttpResponse("Meeting participants of : %s" % meeting_id)

def meetingitems(request, meetingitem_id):
	return HttpResponse("Meeting items of : %s" % meeting_id)