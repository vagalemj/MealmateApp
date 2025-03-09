from django.shortcuts import render, redirect, get_object_or_404
from delivery.models import Restaurants
from delivery.models import Menu
from .forms import ResForm
from .forms import MenuForm
from django.http import HttpResponse
from delivery.models import Customer

# Create your views here.
def index(request):
    return render(request, 'delivery/index.html')

def sign_in(request):
    return render(request, 'delivery/sign_in.html')

def sign_up(request):
    return render(request, 'delivery/sign_up.html')

def handle_signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = Customer.objects.get(username = username, password = password)
            if username == 'admin':
                return render(request, 'delivery/success.html')
            else:
                return render(request, 'delivery/customer_home.html')
        except Customer.DoesNotExist:
            return render(request, 'delivery/fail.html')

def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        try:
            Customer.objects.get(username=username, password=password)
        except Customer.DoesNotExist: # Properly handle exception
            cus = Customer(username=username, password=password, email=email, mobile=mobile, address=address)
            cus.save()
        return render(request, 'delivery/sign_in.html')
    else:
        return HttpResponse('Invalid Request')


def add_res(request):
    form = ResForm(request.POST or None, request.FILES or None)  # Handle image uploads
    if form.is_valid():
        res_name = form.cleaned_data['Res_name']  # Use cleaned_data
        try:
            Restaurants.objects.get(Res_name=res_name)
        except Restaurants.DoesNotExist:  # Handle only the expected exception
            form.save()
            return redirect('delivery:display_res')

    return render(request, 'delivery/add_res.html', {'form': form})

def display_res(request):
    li = Restaurants.objects.all()
    return render(request, 'delivery/display_res.html', {'li':li})

def view_menu(request, id):
    res = Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)
    return render(request, 'delivery/menu.html', {'res':res, 'menu': menu})

def add_menu(request, id):
    restaurant = get_object_or_404(Restaurants, pk=id)  # Get the restaurant
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.res = restaurant  # Associate menu item with restaurant
            menu_item.save()
            return redirect('delivery:view_menu', id=id)
    else:
        form = MenuForm()
    return render(request, 'delivery/menu_form.html', {'form': form, 'restaurant': restaurant})

def delete_menu(request, id):
    item = Menu.objects.get(pk=id)
    res_id = item.res_id
    item.delete()
    return redirect('delivery:view_menu', res_id)

# def viewcustomer_menu(request, id):
#     res = Restaurants.objects.get(pk=id)
#     menu = Menu.objects.filter(res=res)
#     return render(request, 'delivery/customer_menu.html', {'res': res, 'menu': menu})

def cusdisplay_res(request):
    li = Restaurants.objects.all()
    return render (request, 'delivery/cusdisplay_res.html', {'li':li})
    
def cusmenu(request,id):
    res = Restaurants.objects.get(pk=id)
    menu = Menu.objects.filter(res=res)
    return render (request, 'delivery/cusmenu.html', {'res': res, 'menu': menu})




