from .models import Lesson
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate

from .views import LessonViewSet

# Create your tests here.

User = get_user_model()

class LessonAPITest(APITestCase):

    def setUp(self, *args, **kwargs):
        self.factory = APIRequestFactory()
        self.user = self.setUp_user()


    def setUp_user(self):
        return User.objects.create_superuser('test@gmail.com', '1')


    def test_get_lesson(self):
        request = self.factory.get('/api/lessons/')
        view = LessonViewSet.as_view({'get': 'list'})
        response = view(request)

        assert response.status_code == 200


