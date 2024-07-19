from django.shortcuts import render, redirect
from .models import Task, users, MyModel
from .forms import MyModelForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def show_login_page(request):
    return render(request, 'login.html')

@require_POST
def login_user(request):
    print("POST request received")  # For debugging
    firstname = request.POST.get('firstname')
    password = request.POST.get('password')

    if not firstname or not password:
        messages.error(request, 'Please fill out both fields.')
        return redirect('login')

    user = authenticate(request, username=firstname, password=password)
    if user is not None:
       auth_login(request, user)  # Use the aliased login function
       return redirect('main')
    else:
        messages.error(request, 'Invalid username or password.')
        return redirect('login')

def register(request):
    return render(request, 'register.html')

@require_POST
def add_user(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone = request.POST.get('phone')

    if firstname and lastname and email and password and phone:
        if users.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            users.objects.create(firstname=firstname, lastname=lastname, email=email, password=password, phone=phone)
            messages.success(request, 'Registration successful! You can now log in.')

    return redirect('register')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@require_POST
def add_task(request):
    title = request.POST.get('title')
    category = request.POST.get('category')
    date = request.POST.get('date')
    time = request.POST.get('time')
    if title and category:
        Task.objects.create(title=title, category=category, date=date, time=time)
    return redirect('main')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('main')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        task.title = title
        task.category = category
        task.save()
    return redirect('main')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('main')

def incomplete_tasks(request):
    tasks = Task.objects.filter(completed=False).order_by('created_at')
    return render(request, 'incomplete_tasks.html', {'tasks': tasks})

def completed_tasks(request):
    tasks = Task.objects.filter(completed=True).order_by('created_at')
    return render(request, 'completed_tasks.html', {'tasks': tasks})

def search_tasks(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(title__icontains=query).order_by('created_at')
    return render(request, 'search_results.html', {'tasks': tasks, 'query': query})

def reset_password(request):
    return render(request, 'reset_password.html')

def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyModelForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return HttpResponse('Successfully uploaded')

def display_images(request):
    objects = MyModel.objects.all()
    return render(request, 'display.html', {'objects': objects})

@login_required
def main(request):
    tasks = Task.objects.order_by('created_at')
    incomplete_tasks = Task.objects.filter(completed=False).order_by('created_at')
    completed_tasks = Task.objects.filter(completed=True).order_by('created_at')
    return render(request, 'main.html', {'tasks': tasks, 'incomplete_tasks': incomplete_tasks, 'completed_tasks': completed_tasks})

def test_login_user(request):
    if request.method == 'POST':
        return HttpResponse('POST request received')
    return HttpResponse('GET request received')