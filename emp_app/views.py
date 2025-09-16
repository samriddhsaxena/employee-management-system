from django.shortcuts import render,HttpResponse
from .models import Employees,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employees.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phone')
        salary = int(salary) if salary and salary.isdigit() else 0
        bonus = int(bonus) if bonus and bonus.isdigit() else 0
        phone = int(phone) if phone and phone.isdigit() else 0
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        hire_date = request.POST.get('hire_data')

        new_emp = Employees(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept_id,role_id=role_id,hire_data=datetime.now())
        new_emp.save()
        return HttpResponse("Employee Added Successfully")
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return render("An exception occured")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employees.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please enter a valid employee id")
    emps = Employees.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        emps = Employees.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(Q(dept__name__icontains = dept))
        if role:
            emps = emps.filter(Q(role__name__icontains=role))
        context = {
            'emps':emps
        }
        return render(request,'view_all_emp.html',context)
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An exception occured")