from django.db import models
from django.urls import reverse

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    course = models.CharField(max_length=100, blank=True)
    enrollment_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['roll_no', 'last_name', 'first_name']

    def __str__(self):
        return f"{self.roll_no} - {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('students:student-detail', args=[str(self.pk)])
