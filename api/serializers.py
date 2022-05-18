from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Book, Customer, Driver, Partner, HomeOfficeStuff, Rubbish, VanHire, Item, Storage, StoreHouse

class StoreHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreHouse
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    storehouses = StoreHouseSerializer(read_only=True, many=True)
    image_url = serializers.CharField(read_only=True)
    class Meta:
        model = Storage
        fields = [
            'id',
            'name',
            'location',
            'rating',
            'image_url',
            'storehouses',
        ]

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True, source='role.role')
    profile = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'role',
            'profile',
        ]

    def get_profile(self, obj):
        request = self.context.get('request')
        if(obj.role.role == 'customer'):
            return CustomerSerializer(obj.customer).data
        if(obj.role.role == 'driver'):
            return DriverSerializer(obj.driver).data
        if(obj.role.role == 'partner'):
            return PartnerSerializer(obj.partner).data
        return {'state':'error'}

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

class HomeOfficeStuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeOfficeStuff
        fields = '__all__'

class RubbishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubbish
        fields = '__all__'

class VanHireSerializer(serializers.ModelSerializer):
    class Meta:
        model = VanHire
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField(read_only=True)
    customer_name = serializers.CharField(read_only=True,source="customer.name")
    driver_name = serializers.CharField(read_only=True,source="driver.name")
    cost = serializers.SerializerMethodField(read_only=True)
    items = ItemSerializer(read_only=True,many=True)
    class Meta:
        model = Book
        fields = [
            'id',
            'type',
            'customer_name',
            'driver_name',
            'detail',
            'state',
            'cost',
            'items',
            'storage',
        ]

    def get_cost(self, obj):
        return obj.service+obj.storage+obj.promo_code

    def get_detail(self, obj):
        if(obj.type == 'home' or obj.type == 'office' or obj.type == 'stuff'):
            return HomeOfficeStuffSerializer(obj.homeofficestuff).data
        if(obj.type == 'rubbish'):
            return RubbishSerializer(obj.rubbish).data
        if(obj.type == 'skip_hire' or obj.type == 'storage'):
            return VanHireSerializer(obj.van_hire).data
