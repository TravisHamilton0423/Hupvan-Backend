from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.utils.text import slugify
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.models import User
from api.models import Customer, Driver, Book, PromoCode, Storage, StoreHouse

def list_store_house(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    store_houses = StoreHouse.objects.all()
    return render(request, 'admins/store_house/list.html', {'store_houses': store_houses})

def create_store_house(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'GET':
        storages = Storage.objects.all()
        return render(request, 'admins/store_house/create.html', {'storages': storages})
    else:
        storage = Storage.objects.get(id=request.POST['storage_id'])
        StoreHouse.objects.create(title=request.POST['title'],description=request.POST['description'],size=request.POST['size']\
            ,time=request.POST['time'],cost=request.POST['cost'],storage=storage)
        return redirect('/hupvan/admin/store_house/')

def edit_store_house(request, store_house_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'POST':
        storage = Storage.objects.get(id=request.POST['storage_id'])
        store_house = StoreHouse.objects.get(id=store_house_id)
        store_house.title = request.POST['title']
        store_house.description = request.POST['description']
        store_house.size = request.POST['size']
        store_house.time = request.POST['time']
        store_house.cost = request.POST['cost']
        store_house.storage = storage
        store_house.save()
        return redirect('/hupvan/admin/store_house/')
    else:
        store_house = StoreHouse.objects.get(id=store_house_id)
        return render(request, 'admins/store_house/edit.html', {'store_house':store_house, 'storages':Storage.objects.all()})

def delete_store_house(request, store_house_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    StoreHouse.objects.get(id=store_house_id).delete()
    return redirect('/hupvan/admin/store_house/')

def list_storage(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    storages = Storage.objects.all()
    return render(request, 'admins/storage/list.html', {'storages': storages})

def create_storage(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'GET':
        return render(request, 'admins/storage/create.html')
    else:
        Storage.objects.create(name=request.POST['name'],location=request.POST['location'],rating=request.POST['rating'],image=request.FILES['image'])
        return redirect('/hupvan/admin/storage/')

def edit_storage(request, storage_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'POST':
        storage = Storage.objects.get(id=storage_id)
        storage.name = request.POST['name']
        storage.location = request.POST['location']
        storage.rating = request.POST['rating']
        storage.image = request.FILES['image']
        storage.save()
        return redirect('/hupvan/admin/storage/')
    else:
        storage = Storage.objects.get(id=storage_id)
        return render(request, 'admins/storage/edit.html', {'storage':storage})

def delete_storage(request, storage_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    Storage.objects.get(id=storage_id).delete()
    return redirect('/hupvan/admin/storage/')

def list_promo_code(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    promo_codes = PromoCode.objects.all()
    return render(request, 'admins/promo_code/list.html', {'promo_codes': promo_codes})

def create_promo_code(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'GET':
        return render(request, 'admins/promo_code/create.html')
    else:
        PromoCode.objects.create(code=request.POST['code'],times=request.POST['times'],percent=request.POST['percent'])
        return redirect('/hupvan/admin/promo_code/')

def edit_promo_code(request, promo_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'POST':
        promo_code = PromoCode.objects.get(id=promo_id)
        promo_code.times = request.POST['times']
        promo_code.percent = request.POST['percent']
        promo_code.save()
        return redirect('/hupvan/admin/promo_code/')
    else:
        promo_code = PromoCode.objects.get(id=promo_id)
        return render(request, 'admins/promo_code/edit.html', {'promo_code':promo_code})

def delete_promo_code(request, promo_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    PromoCode.objects.get(id=promo_id).delete()
    return redirect('/hupvan/admin/promo_code/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/hupvan/admin/login/')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.filter(email=cd['email'])
            if user.count() and user.get().role.role == 'admin' and user.get().check_password(cd['password']):
                user = user.get()
                if user.is_active:
                    login(request, user)
                    return redirect('/hupvan/admin/customer/')
                else:
                    return redirect('/hupvan/admin/login/')
            else:
                return redirect('/hupvan/admin/login/')
    else:
        form = LoginForm()
    return render(request, 'admins/auth/login.html', {'form': form})

def list_customer(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'GET':
        return render(request, 'admins/customer/list.html', {'customers': Customer.objects.all()})
    return render(request, 'admins/customer/list.html', {'customers':[]})

def delete_customer(request, customer_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    customer = Customer.objects.filter(id=customer_id).get()
    user = customer.user
    customer.delete()
    user.delete()
    return redirect('/hupvan/admin/customer/')

def list_driver(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'GET':
        return render(request, 'admins/driver/list.html', {'drivers': Driver.objects.all()})
    return render(request, 'admins/driver/list.html', {'drivers':[]})

def edit_driver(request, driver_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    driver = Driver.objects.filter(id=driver_id).values()[0]
    if request.method == 'GET':
        return render(request, 'admins/driver/edit.html', {'driver': driver})
    driver = Driver.objects.get(id=driver_id)
    approve = request.POST.get('approve')
    if approve == 'on':
        driver.approved_state = True
    else:
        driver.approved_state = False
    driver.save()
    return redirect('/hupvan/admin/driver/')

def delete_driver(request, driver_id):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    driver = Driver.objects.filter(id=driver_id).get()
    driver.delete()
    return redirect('/hupvan/admin/driver/')

def list_book(request):
    if request.user.is_authenticated == False:
        return redirect('/hupvan/admin/login/')
    if request.method == 'GET':
        return render(request, 'admins/book/list.html', {'books': Book.objects.all()})
    return render(request, 'admins/book/list.html', {'books':[]})
