from django.shortcuts import render, redirect
from .models import Workouts
from .forms import WorkoutsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def workouts_home(request):
    workouts = Workouts.objects.order_by('-date')
    return render(request, 'workouts/workouts_home.html', {'workouts': workouts})


class WorkoutsDetailView(DetailView):
    model = Workouts
    template_name = 'workouts/training_review.html'
    context_object_name = 'workouts'


class WorkoutsDeleteView(DeleteView):
    model = Workouts
    success_url = '/workouts/'
    template_name = 'workouts/workouts_delete.html'


class NewsUpdateView(UpdateView):
    model = Workouts
    template_name = 'workouts/w_o_create.html'
    form_class = WorkoutsForm


def w_o_create(request):
    error = " "
    if request.method == 'POST':
        form = WorkoutsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts_home')
        else:
            error = 'Some ERROR'

    form = WorkoutsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'workouts/w_o_create.html', data)
