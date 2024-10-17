"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import krishna.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('home', views.homepage,name="homepage"),
    path('about', views.aboutpage,name="aboutpage"),
    path('contact', views.contactpage,name="contactpage"),
    path('vacancies', views.vacancypage,name="vacancies"),
    path('policy', views.policypage,name="policypage"),
    path('faq', views.faq,name="faq"),
    path('news', views.news,name="news"),
    path('user', views.user_log_sign_page,name="userloginpage"),
    #path('user/login', views.user_log_sign_page,name="userloginpage"),
    re_path(r'^user/login$', views.user_log_sign_page,name="userloginpage"),
    path('user/bookings', views.user_bookings,name="dashboard"),
    #path('user/book-room', views.book_room_page,name="bookroompage"),
    #path('user/book-room/book', views.book_room,name="bookroom"),
    #path('user/signup', views.user_sign_up,name="usersignup"),
    re_path(r'^user/signup$', views.user_sign_up,name="usersignup"),
    path('staff/', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/login', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/signup', views.staff_sign_up,name="staffsignup"),
    path('logout', views.logoutuser,name="logout"),
    #path('staff/panel', views.panel,name="staffpanel"),
    re_path(r'^staff/panel$', views.panel,name="staffpanel"),
    #path('staff/allbookings', views.all_bookings,name="allbookigs"),
    re_path(r'^staff/allbookings$', views.all_bookings,name="allbookigs"),
    
    #path('staff/panel/add-new-location', views.add_new_location,name="addnewlocation"),
    re_path(r'^staff/panel/add-new-location$', views.add_new_location,name="addnewlocation"),
    #path('staff/panel/edit-room', views.edit_room),
    re_path(r'^staff/panel/edit-room$', views.edit_room),
    #path('staff/panel/add-new-room', views.add_new_room,name="addroom"),
    re_path(r'^staff/panel/add-new-room$', views.add_new_room,name="addroom"),
    #path('staff/panel/delete-room', views.delete_room,name="deleteroom"),
    re_path(r'^staff/panel/delete-room$', views.delete_room,name="deleteroom"),
    #path('staff/panel/edit-room/edit', views.edit_room),
    #path('staff/panel/view-room', views.view_room),
    re_path(r'^staff/panel/view-room$', views.edit_room),
    #path('staff/panel/add-new-promo', views.add_new_promo,name="addnewpromo"),
    re_path(r'^staff/panel/add-new-promo$', views.add_new_promo, name='addnewpromo'),
    #path('user/add_feedback', views.add_feedback, name="addfeedback"),
    re_path(r'^user/add_feedback$', views.add_feedback, name="addfeedback"),
    #path('staff/panel/add-new-faq', views.add_faq,name="addnewfaq"),
    re_path(r'^staff/panel/add-new-faq$', views.add_faq,name="addnewfaq"),
    path('admin/', admin.site.urls),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('promo-codes/', views.promo_code_list, name='promo_code_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    re_path(r'^staff/panel/add-news$', views.add_news, name='add_news'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('user/book-room', views.book_room_page, name='book_room_page'),
    path('user/book-room/book', views.book_room, name='book_room'),
    path('user/cart/add', views.add_to_cart, name='add_to_cart'),
    path('user/cart/add-page', views.add_to_cart_page, name='add_to_cart_page'),
    path('user/cart', views.view_cart, name='view_cart'),
    path('user/cart/finalize', views.finalize_reservation, name='finalize_reservation'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

