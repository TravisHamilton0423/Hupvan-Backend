from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User, AnonymousUser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .models import Customer, Driver, Partner, Role, Book, HomeOfficeStuff, Rubbish, VanHire, Item, Picture, Storage, StoreHouse, PromoCode
from .serializers import UserSerializer, BookSerializer, StorageSerializer, StoreHouseSerializer, DriverSerializer
from django.db.models import Q

class BookStorageAPIView(generics.ListAPIView):
    serializer_class = StorageSerializer
    def get_queryset(self):
        return Storage.objects.all()

class BookStoreHouseAPIView(generics.ListAPIView):
    serializer_class = StoreHouseSerializer
    def get_queryset(self):
        storage_id = self.request.data['storage_id']
        storage = Storage.objects.filter(id=storage_id).get()
        return StoreHouse.objects.filter(storage=storage).all()

class BookPromoCodeAPIView(APIView):
    def post(self, request):
        promo_code = request.data['promo_code']
        promo = PromoCode.objects.filter(code=promo_code)
        if(promo.count() == 0):
            return JsonResponse({'state':'no'})
        promo = promo.get()
        if(promo.times == 0):
            return JsonResponse({'state':'no'})
        promo.times -= 1
        promo.save()
        return JsonResponse({'state':'ok','percent':promo.percent})

class BookCompleteAPIView(APIView):
    def post(self, request):
        id = request.data['id']
        book = Book.objects.filter(id=id).get()
        book.state = 'completed'
        book.save()
        return JsonResponse({'state':'ok'})

class BookAcceptAPIView(APIView):
    def post(self, request):
        id = request.data['id']
        book = Book.objects.filter(id=id).get()
        book.driver = request.user.driver
        book.state = 'in_progress'
        book.save()
        return JsonResponse({'state':'ok'})

class BookCancelAPIView(APIView):
    def post(self, request):
        id = request.data['id']
        Book.objects.filter(id=id).delete()
        return JsonResponse({'state':'ok'})

class BookPreviousAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        current_user = self.request.user
        if(current_user.role.is_customer()):
            return Book.objects.filter(state='completed',customer=current_user.customer)
        elif(current_user.role.is_driver()):
            return Book.objects.filter(state='completed',driver=current_user.driver)
        return JsonResponse({'state':'error'})

class BookCurrentAPIView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        current_user = self.request.user
        if(current_user.role.is_customer()):
            return Book.objects.exclude(state='completed').filter(customer=current_user.customer)
        elif(current_user.role.is_driver()):
            if(Book.objects.filter(state='in_progress',driver=current_user.driver).count()):
                return Book.objects.filter(state='in_progress',driver=current_user.driver)
            return Book.objects.filter(state='waiting')
        return JsonResponse({'state':'error'})

class SetPasswordAPIView(APIView):
    def post(self, request):
        user = request.user
        if(user.check_password(request.data['current_password'])):
            user.set_password(request.data['password'])
            user.save()
            return JsonResponse({'state':'ok'})
        else:
            return JsonResponse({'state':'error'})

class ProfileUpdateAPIView(APIView):
    def get(self, request):
        print(request.user)
        response_data = UserSerializer(request.user).data
        response_data['token'] = Token.objects.filter(user=request.user).get().key
        return JsonResponse(response_data)
    def post(self, request):
        current_user = request.user
        current_user.email = request.data['email']
        current_user.save()
        if current_user.role.is_customer():
            profile = current_user.customer
            profile.phone_number = request.data['phone_number']
        elif current_user.role.is_driver():
            profile = current_user.driver
        profile.name = request.data['name']
        profile.save()
        return JsonResponse({'state':'ok'})

class RegisterAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        username = email
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        rolename = request.data['role']
        role = Role.objects.create(user=user, role=rolename)
        if(rolename == 'customer'):
            name = request.data['name']
            phone_number = request.data['phone_number']
            verification_code = request.data['verification_code']
            customer = Customer.objects.create(user=user,name=name,phone_number=phone_number,verification_code=verification_code)
            return JsonResponse({'state':'ok'})
        elif(rolename == 'driver'):
            request_data = request.data
            request_data['user'] = user.id
            print(request_data)
            driver = DriverSerializer(data=request_data)
            if driver.is_valid():
                driver.save()
            else:
                return JsonResponse(driver.errors)
            return JsonResponse({'state':'ok'})

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).get()
        if(user == AnonymousUser or check_password(password, user.password) == False or
                (user.role.role == 'driver' and user.driver.approved_state == False)):
            raise ObjectDoesNotExist
        if (Token.objects.filter(user=user).count()):
            Token.objects.filter(user=user).delete()
        token = Token.objects.create(user=user)
        response_data = UserSerializer(user).data
        response_data['token'] = token.key
        return JsonResponse(response_data)

class BookCreateAPIView(generics.CreateAPIView):
    serializer_class = BookSerializer

    def create(self, *args, **kwargs):
        request_data = self.request.data
        id = request_data['id']
        if id != 0:
            Book.objects.filter(id=id).delete()
        request_data.pop('id')
        request_data['customer'] = self.request.user.customer
        book = Book.objects.create(customer=request_data['customer'],type=request_data['type'],state=request_data['state'],
            service=request_data['service'],storage=request_data['storage'],promo_code=request_data['promo_code'])
        items = request_data['items']
        for item in items:
            item['book'] = book
            item_data = Item.objects.create(**item)
        request_data.pop('customer')
        request_data.pop('type')
        request_data.pop('state')
        request_data.pop('service')
        request_data.pop('storage')
        request_data.pop('promo_code')
        request_data.pop('items')
        request_data['book'] = book
        if(book.type == 'home' or book.type == 'office' or book.type == 'stuff'):
            id = request_data.pop('storehouse_id')
            if(id != -1):
                storehouse = StoreHouse.objects.filter(id=id).get()
                request_data['store_house'] = storehouse
            homeofficestuff = HomeOfficeStuff.objects.create(**request_data)
        elif(book.type == 'rubbish'):
            request_data.pop('storehouse_id')
            rubbish = Rubbish.objects.create(**request_data)
        elif(book.type == 'skip_hire' or book.type == 'storage'):
            id = request_data.pop('storehouse_id')
            if(id != -1):
                storehouse = StoreHouse.objects.filter(id=id).get()
                request_data['store_house'] = storehouse
            van_hire = VanHire.objects.create(**request_data)
        return JsonResponse(BookSerializer(book).data)
