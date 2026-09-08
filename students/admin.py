from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'first_name', 'last_name', 'course', 'is_active')
    search_fields = ('first_name', 'last_name', 'roll_no', 'email')
    list_filter = ('course', 'is_active')
