from django.shortcuts import render, redirect
from .models import Cars

# Create your views here.
def home(request):
    return render(request, 'home.html')


def cars_list(request):
    cars = Cars.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/cars_list.html', context=context)

def car_detail(request, pk):
    car = Cars.objects.get(id=pk)
    context = {'car': car}
    return render(request, 'cars/car_detail.html', context=context)

def car_create(request):
    if request.method == 'POST':
        car = Cars()
        car.brand = request.POST.get('brand', '')
        car.model = request.POST.get('model', '')
        car.price = request.POST.get('price', 0)
        car.year = request.POST.get('year', 0)
        car.color = request.POST.get('color', '')
        car.miliage = request.POST.get('miliage', 0)
        car.fuel_type = request.POST.get('fuel_type', '')
        car.desciptions = request.POST.get('desciptions', '')
        car.image = request.FILES.get('image',' ')
        car.save()
        return redirect('cars-list')
    return render(request, 'cars/car_create.html', {'car':'car'})







