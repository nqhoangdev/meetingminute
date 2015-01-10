from django.conf.urls import patterns, url
from meeting import views

urlpatterns = patterns('',
	# 
	url(r'^$', views.index, name='index'),
	#
	url(r'^(?P<meeting_id>\d+)/$', views.meeting, name='meeting_detail'),
	url(r'^(?P<meeting_id>\d+)/participants/$', views.participants, name='meeting_participants'),
	url(r'^(?P<meeting_id>\d+)/meetingitems/$', views.meetingitems, name='meeting_items'),
)