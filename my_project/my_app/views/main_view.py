from django.shortcuts import render,redirect,get_object_or_404
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
        elif len(phone)<7 or len(phone)>15: 
            errors['phone'] = "Phone num must contains more than 7 and less than 15 digits"
            
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
            return render(request,'main/CreateEmployee.html',{'error':errors,'data':request.POST})
   
    return render(request,'main/CreateEmployee.html')

def edit_employee(request, id):
    # emp_data = get_object_or_404(Employee, id)
    emp_data = Employee.objects.get(id=id)
    if request.method == 'POST':
        emp_data.fullname = request.POST.get('fullname')
        emp_data.email = request.POST.get('email')
        emp_data.salary = request.POST.get('salary')
        emp_data.address = request.POST.get('address')
        emp_data.phone = request.POST.get('phone')
        
        emp_data.save()
        return redirect("index")
    
    return render(request,'main/EditEmployee.html',{'emp_data':emp_data})

 # name = {'key':'value'}
 # arr = [1,2,4,5,6,87,9]
 # fruits = {'apple':200, 'orange':400}
 
 # errors = {'fullname':"Fullname is required",'email':'Email is required'}
 
 
 # select * from Employee where id=emp_id   
 
def delete_data(request,emp_id):
    emp_data = Employee.objects.get(id=emp_id)  # filter()
    print(emp_data.fullname)
    emp_data.delete()
    return redirect('index')


    
 
 
