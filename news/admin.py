from django.contrib import admin
from news.models import *
def make_deactive(self, request, queryset):
	queryset.update(status='Deactive')
def make_active(self, request, queryset):
	queryset.update(status='Active')
make_deactive.short_description = "Deactivate Selected Item"
make_active.short_description = "activate Selected Item"

class SectionAdmin(admin.ModelAdmin):
	search_fields = ['title','publish', 'status']
	list_display = ['title','publish', 'status']
	actions = [make_deactive, make_active]

class SmallSectionAdmin(admin.ModelAdmin):
	search_fields = ['title','publish', 'status']
	list_display = ['title','publish', 'status']
	actions = [make_deactive, make_active]


class BasicConfigurationAdmin(admin.ModelAdmin):
	list_display = ['theme_name','status']
	actions = [make_deactive, make_active]	
class CardAdmin(admin.ModelAdmin):
	search_fields = ['title', 'top','section','publish', 'status']
	list_display = ['title','top','publish', 'status']
	actions = [make_deactive, make_active]

class SmallCardAdmin(admin.ModelAdmin):
	search_fields = ['title','section','publish', 'status']
	list_display = ['title','publish', 'status']
	actions = [make_deactive, make_active]
	
class BreakingAdmin(admin.ModelAdmin):
	search_fields = ['text','publish', 'status']
	list_display = ['text','publish', 'status']
	actions = [make_deactive, make_active]
class SlideAdmin(admin.ModelAdmin):
	search_fields = ['text','publish', 'status']
	list_display = ['text','publish', 'status']
	actions = [make_deactive,make_active]
# class Top_5Admin(admin.ModelAdmin):
# 	search_fields = ['top']
# 	list_display = ['top',]

class AdvertisementAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name', 'status']
	actions = [make_deactive,make_active]

admin.site.register(Section, SectionAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Breaking, BreakingAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(BasicConfiguration, BasicConfigurationAdmin)
admin.site.register(SmallSection, SmallSectionAdmin)
admin.site.register(SmallCard, SmallCardAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
# admin.site.register(Top_5,Top_5Admin)
