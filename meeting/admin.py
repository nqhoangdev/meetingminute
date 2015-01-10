from django.contrib import admin

# Register your models here.
from meeting.models import Meeting, MeetingItem, Member

class MeetingItemInline(admin.StackedInline):
	model = MeetingItem
	extra = 1

class MeetingAdmin(admin.ModelAdmin):
	fieldsets = [
		('General', {'fields':['name', 'description', 'date', 'location', 'participants']}),
	]
	inlines = [MeetingItemInline]
	list_display = ('name','description','date','location')
admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Member)