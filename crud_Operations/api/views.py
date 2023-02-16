from django.shortcuts import render, redirect
from api.models import Employees


def INDEX(request):
    emp = Employees.objects.all()
    context = {
        'emp': emp,
    }
    return render(request, 'index.html', context)

# for add data


def ADD(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # creating variables
        emp = Employees(
            name=name,  # left side name is for db & right side name is for form
            email=email,
            address=address,
            phone=phone,
        )

        emp.save()
        return redirect('home')
    return render(request, 'index.html')


# for edit data
def EDIT(request):
    emp = Employees.objects.all()
    context = {
        emp: 'emp'
    }
    return render(request, 'index.html', context)


# for update the data
def UPDATE(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id=id,
            name=name,  # left side name is for db & right side name is for form
            email=email,
            address=address,
            phone=phone,
        )

        emp.save()
        return redirect('home')
    return render(request, 'index.html')


#for delete the data

def DELETE(request, id):
    
    emp = Employees.objects.filter(id = id)
    emp.delete()

    context={
        emp:'emp'
    }

    return redirect('home')