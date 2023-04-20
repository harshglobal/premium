from django.contrib import admin
from .models import Course
# Register your models here.



class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','name_slug','author']
    prepopulated_fields = {'name_slug':('name',)}

admin.site.register(Course,CourseAdmin)


