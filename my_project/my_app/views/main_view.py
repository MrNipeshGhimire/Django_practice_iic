from django.shortcuts import render,redirect
from ..models import Employee

def index(request):
    # select * from Employee where id=2;    
    empData = Employee.objects.all()
    return render(request,'main/index.html',{'hello':empData})

def create_employee(request):
    errors = {}   # num = {'first':'1','second':'2'} 
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        salary = request.POST.get('salary')
        
        if not fullname:
            errors['fullname'] = 'Fullname is required'
        
        if not email:
            errors['email'] = "Email is required"
        elif Employee.objects.filter(email=email):
            errors['email'] = "Email already exists. add another"
        
        if not salary:
            errors['salary'] = "Salary is required"
        
        if not phone:
            errors['phone'] = "Phone is required"
            
        if not errors:
            data = Employee.objects.create(
                fullname = fullname,
                email = email,
                address = address,
                phone = phone,
                salary = salary
            )
            data.save()
            return redirect('index')
        else:
            return render(request,'main/CreateEmployee.html',{'error':errors})
   
    return render(request,'main/CreateEmployee.html')

def edit_employee(request):
    return render(request,'main/EditEmployee.html')

 # name = {'key':'value'}
 # arr = [1,2,4,5,6,87,9]
 # fruits = {'apple':200, 'orange':400}
 
 # errors = {'fullname':"Fullname is required",'email':'Email is required'}