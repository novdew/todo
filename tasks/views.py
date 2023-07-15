from django.views import generic
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task


# Create your views here.
class CreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'


class HomeView(generic.ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'


class AboutView(generic.DetailView):
    model = Task
    template_name = 'tasks/about.html'
    context_object_name = 'task'


class UpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'


class DeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    template_name = 'tasks/delete.html'

