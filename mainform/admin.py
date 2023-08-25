from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import studentdata, itservices, langservices, frontendchanges
from django.utils.html import format_html
import requests

# Register your models here.

class langservicesad(admin.ModelAdmin):
    list_display = ('id', 'langser',)
    search_fields = ('langser',) 

admin.site.register(langservices, langservicesad)

class itservicesad(admin.ModelAdmin):
    list_display = ('id', 'itser',)
    search_fields = ('itser',) 

admin.site.register(itservices, itservicesad)

class studentdataadmin(admin.ModelAdmin):
    list_display = ('id', 'perimg', 'fullname', 'city', 'state', 'zip', 'mob', 'mail', 'dob', 'education', 'field', 'university', 'passyr', 'oneradio', 'applicationdate', 'secradio', 'itservice', 'langservice', 'thirdradio', 'feedata')
    search_fields = ('fullname',) 
    list_filter = ('thirdradio', )
    
    # def image_tag(self, obj):
    #     return format_html(f'<img src="/media/{obj.perimg}" width="100" height="150" />')

    # image_tag.short_description = 'Profile Image'

admin.site.register(studentdata, studentdataadmin)


class frontendchangesad(admin.ModelAdmin):
    list_display = ('id', 'image_tag2', 'title', 'image_tag3', 'image_tag', 'mainname', 'firsttitle', 'sectitle', 'thirdtitle', 'forthtitle', 'fifthtitle', 'queone', 'quesec', 'quethird', 'firstsertitle', 'secsertitle', 'queforth')
    fieldsets = (
        ('main', {
            'fields': ('fevi', 'title', 'backgroundimg',)
        }),
        ('Navbar', {
            'fields': ('logo', 'mainname',),
            'classes': ('collapse',),
        }),
        ('First Step Page', {
            'fields': ('firsttitle',),
            'classes': ('collapse',),
        }),
        ('Second Step Page', {
            'fields': ('sectitle',),
            'classes': ('collapse',),
        }),
        ('Third Step Page', {
            'fields': ('thirdtitle', 'queone', 'quesec', 'quethird',),
            'classes': ('collapse',),
        }),
        ('Forth Step Page', {
            'fields': ('forthtitle', 'firstsertitle', 'secsertitle',),
            'classes': ('collapse',),
        }),
        ('Forth Step Page', {
            'fields': ('fifthtitle', 'queforth',),
            'classes': ('collapse',),
        }),
    )
    
    def image_tag3(self, obj):
        return format_html(f'<img src="/media/{obj.backgroundimg}" width="" height="80px" />')

    image_tag3.short_description = 'Profile Image'
    
    def image_tag2(self, obj):
        return format_html(f'<img src="/media/{obj.fevi}" width="" height="50px" />')

    image_tag2.short_description = 'Profile Image'
    
    def image_tag(self, obj):
        return format_html(f'<img src="/media/{obj.logo}" width="" height="50px" />')

    image_tag.short_description = 'Profile Image'
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(frontendchanges, frontendchangesad)
