from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30,default="krishna")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50,default="ca")
    country = models.CharField(max_length=50,default="us")
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50, default="Lab company")
    description = models.TextField(default="This is a company")
    def __str__(self):
        return self.name
    
class Rooms(models.Model):
    ROOM_STATUS = ( 
    ("1", "available"), 
    ("2", "not available"),    
    ) 

    ROOM_TYPE = ( 
    ("1", "premium"), 
    ("2", "deluxe"),
    ("3","basic"),    
    ) 

    #type,no_of_rooms,capacity,prices,Hotel
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    has_child = models.BooleanField(default=False)
    booking_id = models.CharField(max_length=100,default="null")
    def __str__(self):
        return self.guest.username


class PromoCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    active = models.BooleanField(default=True)
    archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = "promocode"
        verbose_name_plural = "promocodes"

    def __str__(self):
        return f"PromoCode: {self.code}"
    

class Review(models.Model):
    RATINGS = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )

    name = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RATINGS)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='news', blank=True)
    tags = models.ManyToManyField(Tag, related_name='news')

    def __str__(self):
        return self.title
    
class Vacancy(models.Model):
    title = models.CharField(max_length=200, default="Vacancy")
    text = models.TextField(default="We are hiring!")

    def __str__(self):
        return self.title
    
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="This is a contact")
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(default="defalt@gmail.com")
    img = models.ImageField(upload_to='contacts', blank=True)

    def __str__(self):
        return self.name