from django.shortcuts import render,HttpResponse,redirect
from base.models import daysactivity
# Create your views here.

# Home page
def index(request):
    tasks = daysactivity.objects.all()
    return render(request, "main.html", {"tasks": tasks})


# Add task
def add_task(request):
    if request.method == "POST":
        title = request.POST["title"]
        daysactivity.objects.create(title=title, completed=False)
    return redirect("index")


# Edit task
def edit_task(request, task_id):
    task = daysactivity.objects.filter(id=task_id).first()
    if not task:
        return redirect("index")   # If task doesn’t exist, go back

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.due_date = request.POST.get("due_date") or task.due_date
        task.save()
        return redirect("index")

    return render(request, "edit_task.html", {"task": task})


# Mark done
def mark_done(request, task_id):
    task = daysactivity.objects.filter(id=task_id).first()
    if task:
        task.completed = True
        task.save()
    return redirect("index")


# Mark undone
def mark_undone(request, task_id):
    task = daysactivity.objects.filter(id=task_id).first()
    if task:
        task.completed = False
        task.save()
    return redirect("index")


# Delete task
def delete_task(request, task_id):
    task = daysactivity.objects.filter(id=task_id).first()
    if task:
        task.delete()
    return redirect("index")
