from idlelib.rpc import request_queue
from winreg import CreateKey

from django.core.signals import request_started
from django.shortcuts import render, redirect
from django.template.base import kwarg_re
from django.utils.text import phone2numeric
from django.urls import reverse_lazy
from .forms import CarForm, ContactForm
from .models import Cars
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


# Create your views here.
def home(request):
    return render(request, 'home.html')


from django.shortcuts import get_object_or_404, redirect

def contact_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        return redirect('home')
    return render(request, 'contact.html', {'form':form})



class CarsList(ListView):
    model = Cars
    template_name = 'cars/cars_list.html'
    context_object_name = 'cars'

class CarDetail(DetailView):
    model = Cars
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

class CarDelete(DeleteView):
    model = Cars
    success_url = reverse_lazy('cars-list')
    template_name = 'cars/cars_delete.html'
    context_object_name = 'car'

class CarCreate(CreateView):
    model = Cars
    form_class = CarForm
    success_url = reverse_lazy('cars-list')
    template_name = 'cars/car_create.html'
    # fields = '__all__'

class CarUpdate(UpdateView):
    model = Cars
    form_class = CarForm
    template_name = 'cars/car_update.html'
    context_object_name = 'car'

    def get_success_url(self):
        return reverse_lazy('car-detail', kwargs={'pk':self.object.pk})















    # def cars_list(request):
    #     cars = Cars.objects.all()
    #     context = {'cars': cars}
    #     return render(request, 'cars/cars_list.html', context=context)

    # def car_detail(request, pk):
    #     car = Cars.objects.get(id=pk)
    #     context = {'car': car}
    #     return render(request, 'cars/car_detail.html', context=context)

    # car = Cars()
    # car.brand = request.POST.get('brand', '')
    # car.model = request.POST.get('model', '')
    # car.price = request.POST.get('price', 0)
    # car.year = request.POST.get('year', 0)
    # car.color = request.POST.get('color', '')
    # car.miliage = request.POST.get('miliage', 0)
    # car.fuel_type = request.POST.get('fuel_type', '')
    # car.desciptions = request.POST.get('desciptions', '')
    # car.image = request.FILES.get('image',' ')
    # car.save()

    # def car_create(request):
    #     if request.method == 'POST':
    #         brand = request.POST['brand']
    #         model = request.POST['model']
    #         year = request.POST['year']
    #         price = request.POST['price']
    #         fuel_type = request.POST['fuel_type']
    #         descriptions = request.POST['descriptions']
    #         image = request.POST['image']
    #         mileage = request.POST['mileage']
    #         color = request.POST['color']
    #         Cars.objects.create(
    #             brand=brand,
    #             model=model,
    #             year=year,
    #             price=price,
    #             fuel_type=fuel_type,
    #             descriptions=descriptions,
    #             image=image,
    #             mileage=mileage,
    #             color=color
    #         )
    #
    #         return redirect('cars-list')
    #     return render(request, 'cars/car_create.html', {'car':'car'})

    # def car_update(request, pk):
    #     car = Cars.objects.get(id=pk)
    #     if request.method == 'POST':
    #         car.brand = request.POST.get('brand', car.brand)
    #         car.color = request.POST.get('color', car.color)
    #         car.price = request.POST.get('price', car.price)
    #         car.model = request.POST.get('model', car.model)
    #         car.miliage = request.POST.get('miliage', car.miliage)
    #         car.fuel_type = request.POST.get('fuel_type', car.fuel_type)
    #         car.desciptions = request.POST.get('desciptions', car.desciptions)
    #         car.year = request.POST.get('year', car.year)
    #         car.image = request.FILES.get('image', car.image)
    #         car.save()
    #         return redirect('car-detail', pk=pk)
    #     return render(request, 'cars/car_update.html', {'car':car})



# def car_delete(request, pk):
#     car = get_object_or_404(Cars, id=pk)
#     car.delete()
#     return redirect('cars-list')





# def car_create_form(reqeust):
#     form = CarForm(reqeust.POST, reqeust.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('cars-list')
#     return render(reqeust, 'cars/car_create.html', {'form':form})


# def car_update(request, pk):
#     car = get_object_or_404(Cars, id=pk)
#     form = CarForm(request.POST or None, instance=car, files=request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('car-detail', pk=pk)
#     return render(request, 'cars/car_update.html', {'form':form, 'car':car})