import calendar
from django.shortcuts import render ,redirect, get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from .models import Hotels, Rooms, Reservation, PromoCode, FAQ, Company, News, Review, Tag, Cart, Contacts, Vacancy, Partner
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
import logging
import requests
# Create your views here.

logger = logging.getLogger(__name__)

@login_required(login_url='/staff')
def cat_fact(request):
    response = requests.get('https://catfact.ninja/fact')
    facts = response.json()
    fact_text = f"Cat Fact: {facts['fact']}"
    messages.info(request, fact_text)

def timer(request):
    logger.info('Timezone: %s', timezone.get_current_timezone())
    user_time = timezone.localtime(timezone.now())
    utc_time = timezone.now()
    tz = timezone.get_current_timezone()
    time_text = (
        f"User Time: {user_time.strftime('%d-%m-%Y %H:%M:%S')}, "
        f"UTC Time: {utc_time.strftime('%d-%m-%Y %H:%M:%S')}, "
        f"Timezone: {tz}"
    )
    messages.info(request, time_text)

#homepage
def homepage(request):
    all_location = Hotels.objects.values_list('location','id').distinct().order_by()
    partners = Partner.objects.all()
    #cat_fact(request)
    timer(request)
    if request.method =="POST":
        try:
            print(request.POST)
            hotel = Hotels.objects.all().get(id=int(request.POST['search_location']))
            rr = []

            #for finding the reserved rooms on this time period for excluding from the query set
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.check_in) < str(request.POST['cin']) and str(each_reservation.check_out) < str(request.POST['cout']):
                    pass
                elif str(each_reservation.check_in) > str(request.POST['cin']) and str(each_reservation.check_out) > str(request.POST['cout']):
                    pass
                else:
                    rr.append(each_reservation.room.id)
                
            room = Rooms.objects.all().filter(hotel=hotel,capacity__gte = int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(request,"Sorry No Rooms Are Available on this time period")
            data = {'rooms':room,'all_location':all_location,'flag':True, 'partners': partners}
            user_time = timezone.localtime(timezone.now())
            month_calendar = calendar.month(user_time.year, user_time.month)
            response = render(request,'index.html',data, {'month_calendar': month_calendar})
        except Exception as e:
            logger.error('Exception occurred', exc_info=True)
            messages.error(request,e)
            response = render(request,'index.html',{'all_location':all_location})


    else:
        data = {'all_location':all_location, 'partners': partners}
        print(partners,"partners2")
        response = render(request,'index.html',data)
    return HttpResponse(response)

#about
def aboutpage(request):
    timer(request)
    logger.info('About page visited')
    company = Company.objects.first()  # or get the company instance however you need
    logger.info('Company details: %s', company)
    return render(request, 'about.html', {'company': company})

#contact page
def contactpage(request):
    timer(request)
    logger.info('Contact page visited')
    contacts = Contacts.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})

#policypage
def policypage(request):
    timer(request)
    logger.info('Policy page visited')
    return HttpResponse(render(request,'policy.html'))

def vacancypage(request):
    timer(request)
    logger.info('Vacancy page visited')
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancy.html', {'vacancies': vacancies})

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy.html', context)

#user sign up
def user_sign_up(request):
    timer(request)
    if request.method =="POST":
        user_name = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_number = request.POST['phonenumber']
        age_check = datetime.datetime.strptime(request.POST['agecheck'], "%Y-%m-%d")  # assuming ageCheck is in 'YYYY-MM-DD' format
        print(age_check)
        if age_check > datetime.datetime.now() - datetime.timedelta(days=18*365):
            messages.warning(request, "You must be at least 18 years old to register")
            return redirect('userloginpage')

        if password1 != password2:
            messages.warning(request,"Password didn't matched")
            return redirect('userloginpage')
        
        try:
            if User.objects.all().get(username=user_name):
                messages.warning(request,"Username Not Available")
                return redirect('userloginpage')
        except:
            logger.error('Exception occurred', exc_info=True)
            pass
            

        new_user = User.objects.create_user(username=user_name,password=password1, phonenumber=phone_number)
        new_user.is_superuser=False
        new_user.is_staff=False
        new_user.save()
        messages.success(request,"Registration Successfull")
        return redirect("userloginpage")
    return HttpResponse('Access Denied')
#staff sign up
def staff_sign_up(request):
    timer(request)
    if request.method =="POST":
        user_name = request.POST['username']
        
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone_number = request.POST['phonenumber']
        age_check = datetime.datetime.strptime(request.POST['agecheck'], "%Y-%m-%d")  # assuming ageCheck is in 'YYYY-MM-DD' format
        print(age_check)
        if age_check > datetime.datetime.now() - datetime.timedelta(days=18*365):
            messages.warning(request, "You must be at least 18 years old to register")
            return redirect('staffloginpage')
        if password1 != password2:
            messages.success(request,"Password didn't Matched")
            return redirect('staffloginpage')
        try:
            if User.objects.all().get(username=user_name):
                messages.warning(request,"Username Already Exist")
                return redirect("staffloginpage")
        except:
            logger.error('Exception occurred', exc_info=True)
            pass
        
        new_user = User.objects.create_user(username=user_name,password=password1, phonenumber=phone_number)
        new_user.is_superuser=False
        new_user.is_staff=True
        new_user.save()
        messages.success(request," Staff Registration Successfull")
        return redirect("staffloginpage")
    else:

        return HttpResponse('Access Denied')
#user login and signup page
def user_log_sign_page(request):
    timer(request)
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pswd']

        user = authenticate(username=email,password=password)
        try:
            if user.is_staff:
                messages.error(request,"Incorrect username or Password")
                return redirect('staffloginpage')
        except:
            logger.error('Exception occurred', exc_info=True)
            pass
        
        if user is not None:
            login(request,user)
            messages.success(request,"successful logged in")
            print("Login successfull")
            return redirect('homepage')
        else:
            messages.warning(request,"Incorrect username or password")
            return redirect('userloginpage')

    response = render(request,'user/userlogsign.html')
    return HttpResponse(response)

#logout for admin and user 
def logoutuser(request):
    if request.method =='GET':
        logout(request)
        messages.success(request,"Logged out successfully")
        print("Logged out successfully")
        return redirect('homepage')
    else:
        print("logout unsuccessfull")
        return redirect('userloginpage')

#staff login and signup page
def staff_log_sign_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user.is_staff:
            login(request,user)
            return redirect('staffpanel')
        else:
            messages.success(request,"Incorrect username or password")
            return redirect('staffloginpage')
    response = render(request,'staff/stafflogsign.html')
    return HttpResponse(response)

def joker(request):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke = response.json()
    data = {'joke': joke}
    messages.info(request, data)

#staff panel page
@login_required(login_url='/staff')
def panel(request):
    #joker(request)
    timer(request)
    if request.user.is_staff == False:
        return HttpResponse('Access Denied')
    search_term = request.GET.get('search', '')
    sort_by_price = request.GET.get('sort_by_price', '')
    rooms = Rooms.objects.filter(price__icontains=search_term)
    #rooms = Rooms.objects.all()
    if sort_by_price:
        rooms = rooms.order_by('price')
    total_rooms = len(rooms)
    available_rooms = len(Rooms.objects.all().filter(status='1'))
    unavailable_rooms = len(Rooms.objects.all().filter(status='2'))
    reserved = len(Reservation.objects.all())

    hotel = Hotels.objects.values_list('location','id').distinct().order_by()
    user_time = timezone.localtime(timezone.now())
    month_calendar = calendar.month(user_time.year, user_time.month)
    response = render(request,'staff/panel.html',{'location':hotel,'reserved':reserved,'rooms':rooms,'total_rooms':total_rooms,'available':available_rooms,'unavailable':unavailable_rooms,'month_calendar': month_calendar})
    return HttpResponse(response)

#for editing room information
@login_required(login_url='/staff')
def edit_room(request):
    timer(request)
    if request.user.is_staff == False:   
        return HttpResponse('Access Denied')
    if request.method == 'POST' and request.user.is_staff:
        print(request.POST)
        old_room = Rooms.objects.all().get(id= int(request.POST['roomid']))
        hotel = Hotels.objects.all().get(id=int(request.POST['hotel']))
        old_room.room_type  = request.POST['roomtype']
        old_room.capacity   =int(request.POST['capacity'])
        old_room.price      = int(request.POST['price'])
        old_room.size       = int(request.POST['size'])
        old_room.hotel      = hotel
        old_room.status     = request.POST['status']
        old_room.room_number=int(request.POST['roomnumber'])

        old_room.save()
        messages.success(request,"Room Details Updated Successfully")
        return redirect('staffpanel')
    else:
    
        room_id = request.GET['roomid']
        room = Rooms.objects.all().get(id=room_id)
        response = render(request,'staff/editroom.html',{'room':room})
        return HttpResponse(response)


#for deleting room
@login_required(login_url='/staff')
def delete_room(request):
    timer(request)
    if request.user.is_staff == False:
        return HttpResponse('Access Denied')
    if request.method == "GET":
        room_id = request.GET['roomid']
        try:
            room = Rooms.objects.get(id=room_id)
            room.delete()
            messages.success(request,"New Room Added Successfully")
        except Rooms.DoesNotExist:
            messages.error("Room does not exist")
    else:
        return HttpResponse('Invalid request')
    
#for adding room
@login_required(login_url='/staff')
def add_new_room(request):
    timer(request)
    if request.user.is_staff == False:
        return HttpResponse('Access Denied')
    if request.method == "POST":
        total_rooms = len(Rooms.objects.all())
        new_room = Rooms()
        hotel = Hotels.objects.all().get(id = int(request.POST['hotel']))
        print(f"id={hotel.id}")
        print(f"name={hotel.name}")


        new_room.roomnumber = total_rooms + 1
        new_room.room_type  = request.POST['roomtype']
        new_room.capacity   = int(request.POST['capacity'])
        new_room.size       = int(request.POST['size'])
        new_room.capacity   = int(request.POST['capacity'])
        new_room.hotel      = hotel
        new_room.status     = request.POST['status']
        new_room.price      = request.POST['price']

        new_room.save()
        messages.success(request,"New Room Added Successfully")
    
    return redirect('staffpanel')

#booking room page
@login_required(login_url='/user')
def book_room_page(request):
    timer(request)
    room = Rooms.objects.all().get(id=int(request.GET['roomid']))
    return HttpResponse(render(request,'user/bookroom.html',{'room':room}))

#For booking the room
@login_required(login_url='/user')
def book_room(request):
    timer(request)
    if request.method == "POST":
        room_id = request.POST['room_id']
        room = Rooms.objects.all().get(id=room_id)
        for each_reservation in Reservation.objects.all().filter(room=room):
            if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
                pass
            elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
                pass
            else:
                messages.warning(request, "Sorry This Room is unavailable for Booking")
                return redirect("homepage")

        current_user = request.user
        total_person = int(request.POST['person'])
        booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        room_object = Rooms.objects.all().get(id=room_id)
        room_object.status = '2'
        reservation.has_child = 'child' in request.POST
        user_object = User.objects.all().get(username=current_user)

        reservation.guest = user_object
        reservation.room = room_object
        person = total_person
        reservation.check_in = request.POST['check_in']
        reservation.check_out = request.POST['check_out']

        reservation.save()

        messages.success(request, "Congratulations! Booking Successfull")
        return redirect("homepage")
    else:
        return HttpResponse('Access Denied')

def handler404(request):
    return render(request, '404.html', status=404)

@login_required(login_url='/staff')   
def view_room(request):
    timer(request)
    room_id = request.GET['roomid']
    room = Rooms.objects.all().get(id=room_id)

    reservation = Reservation.objects.all().filter(room=room)
    return HttpResponse(render(request,'staff/viewroom.html',{'room':room,'reservations':reservation}))

@login_required(login_url='/user')
def user_bookings(request):
    timer(request)
    if request.user.is_authenticated == False:
        return redirect('userloginpage')
    user = User.objects.all().get(id=request.user.id)
    print(f"request user id ={request.user.id}")
    bookings = Reservation.objects.all().filter(guest=user)
    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'user/mybookings.html',{'bookings':bookings}))

@login_required(login_url='/staff')
def add_new_location(request):
    timer(request)
    if request.method == "POST" and request.user.is_staff:
        owner = request.POST['new_owner']
        location = request.POST['new_city']
        state = request.POST['new_state']
        country = request.POST['new_country']
        
        hotels = Hotels.objects.all().filter(location = location , state = state)
        if hotels:
            messages.warning(request,"Sorry City at this Location already exist")
            return redirect("staffpanel")
        else:
            new_hotel = Hotels()
            new_hotel.owner = owner
            new_hotel.location = location
            new_hotel.state = state
            new_hotel.country = country
            new_hotel.save()
            messages.success(request,"New Location Has been Added Successfully")
            return redirect("staffpanel")

    else:
        return HttpResponse("Not Allowed")
    
#for showing all bookings to staff
@login_required(login_url='/staff')
def all_bookings(request):
    timer(request)
    #calculate revenue for each location
    hotels = Hotels.objects.all()
    revenues = []
    locations = []
    for hotel in hotels:
        revenue = 0
        for reservation in Reservation.objects.all().filter(room__hotel__location=hotel.location):
            revenue += reservation.room.price
        revenues.append(revenue)
        locations.append(hotel.location)
    bookings = Reservation.objects.all()
    print(revenues)
    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'staff/allbookings.html',{'bookings':bookings, 'revenues': revenues, 'locations': locations}))

@login_required(login_url='/staff')
def add_new_promo(request):
    timer(request)
    if request.method == 'POST':
        try:
            code = request.POST.get('code')
            discount = request.POST.get('discount')
            active = request.POST.get('active') == 'True'
            archived = request.POST.get('archived') == 'True'
            
            # Проверка на уникальность кода
            if PromoCode.objects.filter(code=code).exists():
                messages.error(request, "Promo Code already exists")
                return redirect('addnewpromo')

            # Проверка на пустые значения
            if not code or not discount:
                messages.error(request, "Code and Discount are required")
                return redirect('addnewpromo')

            promo_code = PromoCode(code=code, discount=discount, active=active, archived=archived)
            promo_code.save()
            messages.success(request, "New Promo Code Added Successfully")
            return redirect('staffpanel')
        except Exception as e:
            logger.error(f"Error adding promo code: {e}")
            messages.error(request, "An error occurred while adding the promo code")
            return redirect('addnewpromo')
    return render(request, 'staff/add_promo.html')

def promo_code_list(request):
    try:
        promo_codes = PromoCode.objects.all()
        context = {'promo_codes': promo_codes}
        return render(request, 'staff/promo_code_list.html', context)
    except Exception as e:
        logger.error(f"Error fetching promo codes: {e}")
        return render(request, '404.html', status=500)
    
@login_required(login_url='/user')
def add_feedback(request):
    timer(request)
    feedback_list = Review.objects.all()
    context = {'feedback_list': feedback_list}
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        review = Review(name=name, rating=rating, text=text)
        review.save()
        messages.success(request,"Feedback Added Successfully")
    return HttpResponse(render(request,'user/add_feedback.html', context))

def view_feedback(request):
    feedback_list = Review.objects.all()
    context = {'feedback_list': feedback_list}
    return render(request, 'view_feedback.html', context)

@login_required(login_url='/staff')
def add_faq(request):
    timer(request)
    if request.method == 'POST':
        question = request.POST['new_question']
        answer = request.POST['new_answer']

        new_faq = FAQ(question=question, answer=answer)
        new_faq.save()

        messages.success(request, "New FAQ Added Successfully")
        return redirect('staffpanel')

    else:
        return HttpResponse('Access Denied')

def faq(request):
    timer(request)
    faqs = FAQ.objects.all()
    # Передача данных в контекст шаблона
    context = {'faqs': faqs}
    # Отображение шаблона с переданным контекстом
    return render(request, 'faq.html', context)

def news(request):
    news_list = News.objects.all()
    context = {'news_list': news_list}
    print(news_list)
    return render(request, 'news.html', context)

@login_required(login_url='/staff')
def add_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        text = request.POST.get('text')
        img = request.FILES.get('img')
        tag_names = request.POST.get('tags').split(',')

        if not title or not text:
            messages.error(request, "Title and Text are required")
            return redirect('add_news')

        news = News(title=title, summary=summary, text=text, img=img)
        news.save()

        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip())
            news.tags.add(tag)

        messages.success(request, "New News Added Successfully")
        return redirect('staffpanel')
    return render(request, 'staff/add_news.html')
    
def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    context = {'news': news}
    return render(request, 'news_detail.html', context)

def book_room_page(request):
    timer(request)
    try:
        room_id = int(request.GET['roomid'])
        room = Rooms.objects.get(id=room_id)
        return HttpResponse(render(request, 'user/bookroom.html', {'room': room}))
    except Rooms.DoesNotExist:
        messages.error(request, "Room does not exist")
        return redirect('homepage')
    except ValueError:
        messages.error(request, "Invalid room ID")
        return redirect('homepage')
    
def add_to_cart(request):
    timer(request)
    if request.method == "POST":
        try:
            room_id = request.POST['room_id']
            room = Rooms.objects.get(id=room_id)
            for each_reservation in Cart.objects.filter(room=room):
                if str(each_reservation.check_in) < str(request.POST['check_in']) and str(each_reservation.check_out) < str(request.POST['check_out']):
                    pass
                elif str(each_reservation.check_in) > str(request.POST['check_in']) and str(each_reservation.check_out) > str(request.POST['check_out']):
                    pass
                else:
                    messages.warning(request, "Sorry This Room is unavailable for Adding to Cart")
                    return redirect("homepage")

            current_user = request.user
            total_person = int(request.POST['person'])
            booking_id = str(room_id) + str(datetime.datetime.now())

            cart = Cart()
            room_object = Rooms.objects.get(id=room_id)
            room_object.status = '2'
            cart.has_child = 'child' in request.POST
            user_object = User.objects.get(username=current_user)

            cart.user = user_object
            cart.room = room_object
            cart.check_in = request.POST['check_in']
            cart.check_out = request.POST['check_out']

            cart.save()

            messages.success(request, "Congratulations! Adding to Cart Successful")
            return redirect("homepage")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect("homepage")
    else:
        return HttpResponse('Access Denied')

@login_required(login_url='/user')
def view_cart(request):
    timer(request)
    try:
        cart_items = Cart.objects.filter(user=request.user)
        logger.info(f"Cart items for user {request.user}: {cart_items}")
        return render(request, 'user/cart.html', {'cart_items': cart_items})
    except Exception as e:
        logger.error(f"Error in view_cart: {e}")
        return HttpResponse('Internal Server Error', status=500)

def finalize_reservation(request):
    timer(request)
    if request.method == "POST":
        cart_items = Cart.objects.filter(user=request.user)
        for item in cart_items:
            reservation = Reservation(
                check_in=item.check_in,
                check_out=item.check_out,
                room=item.room,
                guest=request.user,
                has_child=item.has_child,
                booking_id=str(item.room.id) + str(datetime.datetime.now())
            )
            reservation.save()
            item.room.status = '2'
            item.room.save()
        cart_items.delete()
        messages.success(request, "Reservation finalized successfully")
        return redirect('homepage')
    else:
        return HttpResponse('Invalid request')

def add_to_cart_page(request):
    timer(request)
    room = Rooms.objects.all().get(id=int(request.GET['roomid']))
    return HttpResponse(render(request,'user/add_to_cart.html',{'room':room}))