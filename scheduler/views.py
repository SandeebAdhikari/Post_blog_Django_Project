from django.shortcuts import render
from .models import Scheduler
from .forms import SchedulerForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def schedulerList(request):
    schedules = Scheduler.objects.all().order_by('-created_at')
    return render(request, 'schedulerList.html', {'schedules': schedules})

@login_required
def scheduleCreate(request):
    if request.method == 'POST': 
        form = SchedulerForm(request.POST, request.FILES)
        if form.is_valid():
            schedules = form.save(commit=False)
            schedules.user = request.user
            schedules.save()
            return redirect('schedulerList')
    else:
        form = SchedulerForm()
    return render(request, 'schedule_form.html', {'form': form})

@login_required
def scheduleEdit(request, scheduler_id):
    schedules = get_object_or_404(Scheduler, pk=scheduler_id, user=request.user)
    if request.method == 'POST':
        form = SchedulerForm(request.POST, request.FILES, instance=schedules)
        if form.is_valid():
            schedules= form.save(commit=False)
            schedules.user = request.user
            schedules.save()
            return redirect('schedulerList')
    else:
        form = SchedulerForm(instance=schedules)
    return render(request, 'schedule_form.html', {'form': form})

@login_required
def scheduleDelete(request, scheduler_id):
    schedules = get_object_or_404(Scheduler, pk=scheduler_id, user=request.user)
    if request.method == 'POST':
        schedules.delete()
        return redirect('schedulerList')
    return render(request, 'schedule_delete.html', {'schedules': schedules})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('schedulerList')
    else: 
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})