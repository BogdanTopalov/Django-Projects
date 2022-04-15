from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from ProjectSoftUni.main_app.forms import EditCourseForm, AddCourseForm
from ProjectSoftUni.main_app.models import Course

from ProjectSoftUni.common.custom_mixins import StaffRequiredMixin

from django.urls import reverse_lazy


class CoursesDashboardView(ListView):
    model = Course
    template_name = 'main/course/courses_dashboard.html'
    context_object_name = 'courses'


class CreateCourseView(StaffRequiredMixin, CreateView):
    model = Course
    form_class = AddCourseForm
    template_name = 'main/course/add_course.html'
    permission_required = 'main_app.add_course'

    # Go to the course dashboard page.
    def get_success_url(self):
        return reverse_lazy('course dashboard page')


class EditCourseView(StaffRequiredMixin, UpdateView):
    model = Course
    form_class = EditCourseForm
    template_name = 'main/course/edit_course.html'
    permission_required = 'main_app.change_course'

    # Go to the course dashboard page.
    def get_success_url(self):
        return reverse_lazy('course dashboard page')


class DeleteCourseView(StaffRequiredMixin, DeleteView):
    model = Course
    template_name = 'main/course/delete_course.html'
    permission_required = 'main_app.delete_course'

    # Go to the course dashboard page.
    def get_success_url(self):
        return reverse_lazy('course dashboard page')
