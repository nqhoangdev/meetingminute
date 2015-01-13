from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from meeting.models import Meeting, MeetingItem, Member
# Create your views here.

def index(request):
	meeting_list = Meeting.objects.all()
	# template = loader.get_template('meeting/index.html')
	# context = RequestContext(request, {
	# 	'meeting_list':meeting_list,
	# })
	# return HttpResponse(template.render(context))

	# Other way to do the same thing:
	context = {'meeting_list':meeting_list}
	return render(request, 'meeting/index.html', context)

def meeting(request, meeting_id):
	queried_meeting = get_object_or_404(Meeting, pk=meeting_id)
	return render(request, 'meeting/meeting_details.html', {'meeting':queried_meeting})
def participants(request, meeting_id):
	return HttpResponse("Meeting participants of : %s" % meeting_id)

def meetingitems(request, meetingitem_id):
	return HttpResponse("Meeting items of : %s" % meeting_id)