from django.test import TestCase
from .models import Hotels, FAQ, Company, Rooms, Reservation, PromoCode, User, Review, News, Vacancy, Contacts
from django.core.exceptions import ValidationError
from django.test import TestCase, Client
from django.contrib.auth.models import User
from unittest.mock import patch
from django.utils import timezone
from django.urls import reverse

class HotelsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Hotels.objects.create(name='Test Hotel', owner='Test Owner', location='Test Location', state='Test State', country='Test Country')

    def test_name_label(self):
        hotel = Hotels.objects.get(id=1)
        field_label = hotel._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_owner_label(self):
        hotel = Hotels.objects.get(id=1)
        field_label = hotel._meta.get_field('owner').verbose_name
        self.assertEquals(field_label, 'owner')

class FAQModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        FAQ.objects.create(question='Test Question', answer='Test Answer')

    def test_question_label(self):
        faq = FAQ.objects.get(id=1)
        field_label = faq._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'question')       

class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Company.objects.create(name='Test Company', description='This is a test company')

    def test_name_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        company = Company.objects.get(id=1)
        field_label = company._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_name_max_length(self):
        company = Company.objects.get(id=1)
        max_length = company._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_name(self):
        company = Company.objects.get(id=1)
        expected_object_name = f'{company.name}'
        self.assertEquals(expected_object_name, str(company))

class RoomsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        hotel = Hotels.objects.create(name='Test Hotel', location='Test Location')
        Rooms.objects.create(room_type='1', capacity=2, price=100, size=30, hotel=hotel, status='1', roomnumber=101)

    def test_room_type_label(self):
        room = Rooms.objects.get(id=1)
        field_label = room._meta.get_field('room_type').verbose_name
        self.assertEquals(field_label, 'room type')

    # Add similar methods for other fields

    def test_object_name_is_hotel_name(self):
        room = Rooms.objects.get(id=1)
        expected_object_name = f'{room.hotel.name}'
        self.assertEquals(expected_object_name, str(room))


class ReservationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='testuser', password='12345')
        hotel = Hotels.objects.create(name='Test Hotel', location='Test Location')
        room = Rooms.objects.create(room_type='1', capacity=2, price=100, size=30, hotel=hotel, status='1', roomnumber=101)
        Reservation.objects.create(check_in='2022-01-01', check_out='2022-01-02', room=room, guest=user, booking_id='123')

    def test_check_in_label(self):
        reservation = Reservation.objects.get(id=1)
        field_label = reservation._meta.get_field('check_in').verbose_name
        self.assertEquals(field_label, 'check in')

    # Add similar methods for other fields

    def test_object_name_is_guest_username(self):
        reservation = Reservation.objects.get(id=1)
        expected_object_name = f'{reservation.guest.username}'
        self.assertEquals(expected_object_name, str(reservation))

class PromoCodeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        PromoCode.objects.create(code='TESTCODE', discount=10, active=True, archived=False)

    def test_code_label(self):
        promo = PromoCode.objects.get(id=1)
        field_label = promo._meta.get_field('code').verbose_name
        self.assertEquals(field_label, 'code')

    # Add similar methods for other fields

    def test_object_name_is_code(self):
        promo = PromoCode.objects.get(id=1)
        expected_object_name = f'PromoCode: {promo.code}'
        self.assertEquals(expected_object_name, str(promo))

    def test_discount_range(self):
        promo = PromoCode.objects.get(id=1)
        with self.assertRaises(ValidationError):
            promo.discount = 101
            promo.full_clean()

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Review.objects.create(name='Test User', rating=3, text='This is a test review')

    def test_name_label(self):
        review = Review.objects.get(id=1)
        field_label = review._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Add similar methods for other fields

    def test_object_name_is_name(self):
        review = Review.objects.get(id=1)
        expected_object_name = f'Review by {review.name}'
        self.assertEquals(expected_object_name, str(review))

class NewsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        News.objects.create(title='Test News', text='This is a test news')

    def test_title_label(self):
        news = News.objects.get(id=1)
        field_label = news._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    # Add similar methods for other fields

    def test_object_name_is_title(self):
        news = News.objects.get(id=1)
        expected_object_name = f'{news.title}'
        self.assertEquals(expected_object_name, str(news))


class VacancyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Vacancy.objects.create(title='Test Vacancy', text='We are hiring!')

    def test_title_label(self):
        vacancy = Vacancy.objects.get(id=1)
        field_label = vacancy._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    # Add similar methods for other fields

    def test_object_name_is_title(self):
        vacancy = Vacancy.objects.get(id=1)
        expected_object_name = f'{vacancy.title}'
        self.assertEquals(expected_object_name, str(vacancy))

class ContactsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Contacts.objects.create(name='Test Contact', description='This is a test contact', phonenumber='1234567890', email='test@gmail.com')

    def test_name_label(self):
        contact = Contacts.objects.get(id=1)
        field_label = contact._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Add similar methods for other fields

    def test_object_name_is_name(self):
        contact = Contacts.objects.get(id=1)
        expected_object_name = f'{contact.name}'
        self.assertEquals(expected_object_name, str(contact))

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    @patch('requests.get')
    def test_cat_fact(self, mock_get):
        mock_get.return_value.json.return_value = {'fact': 'Cats are great'}
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/cat_fact/')
        #self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertEqual(str(messages[0]), "{'fact': 'Cats are great'}")

    def test_timer(self):
        self.client.login(username='testuser', password='12345')
        session = self.client.session
        session['django_timezone'] = 'UTC'
        session.save()
        response = self.client.get('/timer/')
        #self.assertEqual(response.status_code, 200)
        messages = list(response.context['messages'])
        self.assertIn('user_time', str(messages[0]))
        self.assertIn('utc_time', str(messages[0]))
        self.assertIn('tz', str(messages[0]))

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.hotel = Hotels.objects.create(location='Test Location')
        self.room = Rooms.objects.create(hotel=self.hotel, capacity=2)
        self.reservation = Reservation.objects.create(room=self.room, check_in='2022-01-01', check_out='2022-01-02')

    @patch('requests.get')
    def test_homepage_GET(self, mock_get):
        mock_get.return_value.json.return_value = {'fact': 'Cats are great'}
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Location')

    @patch('requests.get')
    def test_homepage_POST(self, mock_get):
        mock_get.return_value.json.return_value = {'fact': 'Cats are great'}
        response = self.client.post('/', {'search_location': self.hotel.id, 'cin': '2022-01-03', 'cout': '2022-01-04', 'capacity': 2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Location')
        self.assertContains(response, self.room.id)

    @patch('requests.get')
    def test_homepage_POST_no_rooms(self, mock_get):
        mock_get.return_value.json.return_value = {'fact': 'Cats are great'}
        response = self.client.post('/', {'search_location': self.hotel.id, 'cin': '2022-01-01', 'cout': '2022-01-02', 'capacity': 2})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Location')
        self.assertContains(response, 'Sorry No Rooms Are Available on this time period')

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.staff = User.objects.create_user(username='teststaff', password='12345', is_staff=True)

    def test_user_sign_up(self):
        response = self.client.post(reverse('user_sign_up'), {'ageCheck': 'on', 'username': 'newuser', 'password1': '12345', 'password2': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_staff_sign_up(self):
        response = self.client.post(reverse('staff_sign_up'), {'ageCheck': 'on', 'username': 'newstaff', 'password1': '12345', 'password2': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newstaff', is_staff=True).exists())

    def test_user_log_sign_page(self):
        response = self.client.post(reverse('user_log_sign_page'), {'email': 'testuser', 'pswd': '12345'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('_auth_user_id', self.client.session)
