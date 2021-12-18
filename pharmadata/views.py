from django.shortcuts import render, redirect
from .models import Faculty
from .forms import FacultyForm

def index(request):
    return render(request, 'index.html')

def all_faculties(request):
    faculties = Faculty.objects.all()
    ctx = {
        'faculties': faculties,
    }
    return render(request, 'all-faculty.html', ctx)

def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'add-faculty.html')

def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("all-faculties")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "edit-faculty.html", ctx)

def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect("all-faculties")

def add_user(request):
    return render(request, 'add-user.html')