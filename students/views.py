from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student

class StudentListView(ListView):
    model = Student
    paginate_by = 20
    template_name = 'students/student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name','last_name','roll_no','email','date_of_birth','course','enrollment_date','is_active']
    template_name = 'students/student_form.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['first_name','last_name','roll_no','email','date_of_birth','course','enrollment_date','is_active']
    template_name = 'students/student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:student-list')
    template_name = 'students/student_confirm_delete.html'
