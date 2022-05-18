from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

ROLE_CHOICES = (
    (u'admin', u'Admin'),
    (u'customer', u'Customer'),
    (u'driver', u'Driver'),
    (u'partner', u'Partner'),
)
TYPE_CHOICES = (
    (u'storage', u'Storage'),
    (u'van_hire', u'Van hire'),
    (u'equipment_hire', u'Equipment hire'),
    (u'other', u'Other'),
)
BOOK_TYPE_CHOICES = (
    (u'home', u'Home'),
    (u'office', u'Office'),
    (u'stuff', u'Stuff'),
    (u'rubbish', u'Rubbish'),
    (u'skip_hire', u'Skip hire'),
    (u'storage', u'Storage'),
)
STATE_CHOICES = (
    (u'waiting', u'Waiting'),
    (u'in_progress', u'In progress'),
    (u'completed', u'Completed'),
)
VAN_HIRE_CHOICES = (
    (u'general', u'General'),
    (u'plasterboard', u'Plasterboard'),
)

class Role(models.Model):
    user = models.OneToOneField(User, related_name="role", on_delete=models.CASCADE)
    role = models.CharField(_('Role'), max_length=15, choices=ROLE_CHOICES, default='customer')

    @property
    def is_admin(self):
        return self.role == 'admin'
    def is_customer(self):
        return self.role == 'customer'
    def is_driver(self):
        return self.role == 'driver'
    def is_partner(self):
        return self.role == 'partner'

class Customer(models.Model):
    user = models.OneToOneField(User, related_name="customer", on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=100)
    phone_number = models.CharField(_('Phone number'), max_length=20)
    verification_code = models.CharField(_('Verification code'), max_length=10)
    # promo_code = models.CharField(_('Promo code'), max_length=100, default='', blank=True)

class Driver(models.Model):
    user = models.OneToOneField(User, related_name="driver", on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=100)
    has_license = models.CharField(_('Has license'), max_length=30, blank=True, null=True)
    insurance_policy = models.CharField(_('Insurance policy'), max_length=30, blank=True, null=True)
    taxi_license = models.CharField(_('Taxi license'), max_length=30, blank=True, null=True)
    own_car = models.CharField(_('Own car'), max_length=30, blank=True, null=True)
    proficiency = models.CharField(_('Proficiency'), max_length=30, blank=True, null=True)
    currently_drive_for_other = models.CharField(_('Currently drive for other'), max_length=30, blank=True, null=True)
    date_of_birth = models.CharField(_('Date of birth'), max_length=30, blank=True, null=True)
    national_insurance_number = models.CharField(_('National insurance number'), max_length=30, blank=True, null=True)
    ethnicity = models.CharField(_('Ethnicity'), max_length=30, blank=True, null=True)
    disability = models.CharField(_('Disability'), max_length=30, blank=True, null=True)
    gender = models.CharField(_('Gender'), max_length=30, blank=True, null=True)
    street_name = models.CharField(_('Street name'), max_length=30, blank=True, null=True)
    current_address = models.CharField(_('Current address'), max_length=30, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=30, blank=True, null=True)
    city = models.CharField(_('City'), max_length=30, blank=True, null=True)
    post_code = models.CharField(_('Post code'), max_length=30, blank=True, null=True)
    driving_category = models.CharField(_('Driving category'), max_length=30, blank=True, null=True)
    category = models.CharField(_('Category'), max_length=30, blank=True, null=True)
    vehicle_type = models.CharField(_('Vehicle type'), max_length=30, blank=True, null=True)
    vehicle_model = models.CharField(_('Vehicle model'), max_length=30, blank=True, null=True)
    year = models.CharField(_('Year'), max_length=30, blank=True, null=True)
    seater = models.CharField(_('Seater'), max_length=30, blank=True, null=True)
    colour = models.CharField(_('Colour'), max_length=30, blank=True, null=True)
    license_plate_number = models.CharField(_('License plate number'), max_length=30, blank=True, null=True)
    approved_state = models.BooleanField(_('Approve'), default=False)

class Storage(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    location = models.CharField(_('Location'), max_length=100)
    rating = models.FloatField(_('raiting'))
    image = models.FileField(upload_to='static/uploads/storage/')

    @property
    def image_url(self):
        if len(self.image.name) == 0:
            return ""
        else:
            return self.image.url

class StoreHouse(models.Model):
    storage = models.ForeignKey(Storage, related_name="storehouses", on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=100)
    description = models.CharField(_('Description'), max_length=200)
    image = models.FileField(upload_to='static/uploads/storehouse/', blank=True)
    size = models.IntegerField(_('Size'))
    time = models.IntegerField(_('Time'))
    cost = models.IntegerField(_('Cost'))

class PromoCode(models.Model):
    code = models.CharField(_('Code'), max_length=100)
    times = models.IntegerField(_('Times'))
    percent = models.FloatField(_('Percent'), default=10)

class Partner(models.Model):
    user = models.OneToOneField(User, related_name="partner", on_delete=models.CASCADE)
    name= models.CharField(_('Name'), max_length=100)
    company= models.CharField(_('Company'), max_length=100)
    industry= models.CharField(_('Industry'), max_length=100)
    telephone= models.CharField(_('Telephone'), max_length=20)
    business_email= models.EmailField(_('Business email'), max_length=20, default="partner@test.com")
    website= models.CharField(_('Website'), max_length=30)
    short_bio= models.TextField(_('Short bio'))
    type = models.CharField(_('Type'), max_length=15, choices=TYPE_CHOICES, default='storage')

class Book(models.Model):
    customer = models.ForeignKey(Customer, related_name="books", on_delete=models.CASCADE)
    type = models.CharField(_('Type'), max_length=15, choices=BOOK_TYPE_CHOICES, default='home')
    driver = models.ForeignKey(Driver, related_name="books", on_delete=models.CASCADE, blank=True, null=True)
    state = models.CharField(_('State'), max_length=15, choices=STATE_CHOICES, default='home')
    # partner = models.ForeignKey(Partner, related_name="books", on_delete=models.CASCADE, blank=True, null=True)
    service = models.FloatField(_('Service'), default=0.0)
    storage = models.FloatField(_('Storage'), default=0.0)
    promo_code = models.FloatField(_('Promo state'), default=0.0)

class HomeOfficeStuff(models.Model):
    book = models.OneToOneField(Book, related_name="homeofficestuff", on_delete=models.CASCADE)
    pickup_address = models.CharField(_('Pickup address'), max_length=100)
    destination_address= models.CharField(_('Destination address'), max_length=100)
    store_house = models.ForeignKey(StoreHouse, related_name="books", on_delete=models.CASCADE, blank=True, null=True)
    date= models.DateField(_('Date'))
    time= models.TimeField(_('Time'))
    floor = models.CharField(_('Floor'), max_length=20)
    number_of_rooms = models.IntegerField(_('Number of rooms'))
    lift = models.BooleanField(_('Is there a lift'))
    detail = models.TextField(_('Detail'))

class Rubbish(models.Model):
    book = models.OneToOneField(Book, related_name="rubbish", on_delete=models.CASCADE)
    pickup_address = models.CharField(_('Pickup address'), max_length=100)
    date= models.DateField(_('Date'))
    time= models.TimeField(_('Time'))

class VanHire(models.Model):
    book = models.OneToOneField(Book, related_name="van_hire", on_delete=models.CASCADE)
    pickup_address = models.CharField(_('Pickup address'), max_length=100)
    from_datetime = models.DateTimeField(_('From'))
    until_datetime = models.DateTimeField(_('Until'))
    type_of_waste = models.CharField(_('Type of waste'), max_length=15, choices=VAN_HIRE_CHOICES, default='home')
    store_house = models.ForeignKey(StoreHouse, related_name="books1", on_delete=models.CASCADE, blank=True, null=True)

class Item(models.Model):
    book = models.ForeignKey(Book, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=100)
    amount = models.IntegerField(_('Amount'))

class Picture(models.Model):
    book = models.ForeignKey(Book, related_name="pictures", on_delete=models.CASCADE)
    url = models.CharField(_('Url'), max_length=100)
