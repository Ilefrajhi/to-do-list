from django.shortcuts import render, redirect
from .models import Task, users
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# Create your views here.
def login(request):
    return render (request, 'login.html')


@require_POST
def login_user(request):
    try:
        firstname = request.POST['firstname']
        password = request.POST['password']
    except KeyError:
        # Handle missing keys gracefully, like redirecting to login page with an error message
        messages.error(request, 'Invalid form submission.')
        return redirect('login')

    user = users.objects.filter(firstname=firstname, password=password).first()
    if user:
        # Log user in and redirect to main page
        request.session['user_id'] = user.id
        return redirect('main')
    else:
        # Add error message
        messages.error(request, 'Invalid firstname or password.')
        return redirect('login')  # Redirect back to login page



def register(request):
    return render(request, 'register.html')

@require_POST
def add_user(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    phone = request.POST['phone']

    if firstname and lastname and email and password and phone:
        users.objects.create(firstname=firstname, lastname=lastname, email=email, password=password, phone=phone)
    
        # Add success message
        messages.success(request, 'Registration successful! You can now log in.')

    return redirect('register')  # Redirect to login after successful registration

def reset_password(request):
    template = loader.get_template('reset_password.html')
    return HttpResponse(template.render())

def logout(request):
    template = loader.get_template('logout.html')
    return HttpResponse(template.render())

def main(request):
    tasks = Task.objects.order_by('created_at')
    incomplete_tasks = Task.objects.filter(completed=False).order_by('created_at')
    completed_tasks = Task.objects.filter(completed=True).order_by('created_at')
    return render(request, 'main.html', {'tasks': tasks, 'incomplete_tasks': incomplete_tasks, 'completed_tasks': completed_tasks})

@require_POST
def add_task(request):
    title = request.POST['title']
    if title:
        Task.objects.create(title=title)
    return redirect('main')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('main')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST['title']
        task.title = title
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
    tasks = Task.objects.filter(completed=True). order_by('created_at')
    return render(request, 'completed_tasks.html', {'tasks': tasks})

def search_tasks(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(title__icontains=query).order_by('created_at')
    return render(request, 'search_results.html', {'tasks': tasks, 'query': query})
