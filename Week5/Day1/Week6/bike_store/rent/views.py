from django.shortcuts import render, redirect
from rent.models import Rental, Customer, Vehicle
from django.views import generic
from django.urls import reverse, reverse_lazy
from rent.forms import NewRentalForm, NewCustomerForm, NewVehicleForm, FindVehicle

# Create your views here.

class ShowAllRentals(generic.ListView):
    template_name = 'rental_all.html'
    context_object_name = 'rentals'
    model = Rental
    
# def rental(request):
#     rentals_unreturned = Rental.objects.filter(return_date__isnull=True)
#     rental_returned = Rental.objects.filter(return_date__isnull=False).order_by('-rental_date')
#     context = {'unreturned': rentals_unreturned,
#                'returned': rental_returned}
#     return render(request, 'rental_all.html', context)

class RentalDetails(generic.DetailView):
    template_name = 'rental_details.html'
    context_object_name = 'info'
    model = Rental
    
# def rental_details(request, id):
#     rental = Rental.objects.get(id=id)
#     context = {'info': rental}
#     return render(request, 'rental_details.html', context)
# how to check if the rental date is earlier than return date

class AddRental(generic.CreateView):
    template_name = 'rental_add.html'
    model = Rental
    form_class = NewRentalForm
    success_url = reverse_lazy('all_rental')
    
# def rental_add(request):
#     if request.method == 'POST':
#         filled_form = NewRentalForm(request.POST)
#         if filled_form.is_valid():
#             filled_form.save()
    
#     form = NewRentalForm()   
#     context = {'form' : form}
#     filled_form = NewRentalForm(request.POST)
    
#     return render(request, 'rental_add.html', context)
class FindCustomer(generic.DetailView):
    template_name = 'customer_details.html'
    model = Customer
    context_object_name = 'info'
    
# def customer_find(request, id):
#     customer = Customer.objects.get(id=id)
#     context = {'info': customer}
#     return render(request, 'customer_details.html', context)
class AllCustomers(generic.ListView):
    template_name = 'customers_all.html'
    model = Customer
    context_object_name = 'info'

# def customer_all(request):
#     customers = Customer.objects.all().order_by('first_name')
#     context = {'info': customers}
#     return render(request, 'customers_all.html', context)

class AddCustomer(generic.CreateView):
    template_name = 'customer_add.html'
    form_class = NewCustomerForm
    model = Customer
    success_url = reverse_lazy('all_customers')
    
# def customer_add(request):
#     if request.method == 'POST':
#         filled_form = NewCustomerForm(request.POST)
#         if filled_form.is_valid():
#             filled_form.save()
    
    # form = NewCustomerForm()   
    # context = {'form' : form}
    # filled_form = NewCustomerForm(request.POST)
    
    # return render(request, 'customer_add.html', context)
class AllVehicle(generic.ListView):
    template_name = 'vehicles_all.html'
    model = Vehicle
    context_object_name = 'info'
    

# def vehicle_all(request):
#     vehicle = Vehicle.objects.all().order_by('id')
#     context = {'info': vehicle}
#     return render(request, 'vehicles_all.html', context)

class FindVehicleView(generic.DetailView):
    template_name = 'vehicles_find.html'
    model = Vehicle
    context_object_name = 'info'
    
# def vehicle_find(request, id):
#     vehicle = Vehicle.objects.get(id=id)
#     try:
#         rental = Rental.objects.get(vehicle=id, return_date__isnull=True)
#     except:
#         rental = "no"
#     context = {'info': vehicle,
#                'is_rented': rental}
#     return render(request, 'vehicles_find.html', context)
class AddVehicle(generic.CreateView):
    template_name = 'vehicle_add.html'
    model = Vehicle
    form_class = NewVehicleForm
    success_url = reverse_lazy('all_vehicle')

# def vehicle_add(request):
#     if request.method == 'POST':
#         filled_form = NewVehicleForm(request.POST)
#         if filled_form.is_valid():
#             filled_form.save()
#     form = NewVehicleForm()   
#     context = {'form' : form}
#     filled_form = NewVehicleForm(request.POST)
#     return render(request, 'vehicle_add.html', context)

# class Home(generic.FormView):
#     template_name = 'home.html'
#     form_class = FindVehicle
#     context_object_name = 'form_vehicle'
    
def home(request):
    if request.method == 'POST':
        form_vehicle = FindVehicle(request.POST)
        if form_vehicle.is_valid():
            id_v = form_vehicle.cleaned_data['id_v']
            id_c = form_vehicle.cleaned_data['id_c']
            id_r = form_vehicle.cleaned_data['id_r']
            
            if id_v:
                return redirect('one_vehicle', id_v)
            elif id_c: 
                return redirect('one_customer', id_c)
            else:
                return redirect('one_rental', id_r)
    
    
    form_vehicle = FindVehicle()
    context = {'form_vehicle': form_vehicle
                #    'form_customer': form_customer,
                #    'form_rental': form_rental           
        }

    return render(request, 'home.html', context)



