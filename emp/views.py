from django.shortcuts import render, redirect
# Create your views here.
from .models import Employee
from .forms import EmployeeForm

def home(request):
    emps = Employee.objects.all()

    context = {
        'emps': emps
    }

    return render(request, 'emps.html', context)

def deleteEmp(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()

    return redirect('/')

def updateEmp(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(instance=emp)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
        
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'updateEmp.html', context)

def addEmp(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    context = {
        'form': form
    }

    return render(request, 'addEmp.html', context)