
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Course

class CourseTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.course_data = {
            'title': 'Test Course',
            'subject': 'Test Subject',

        }

# POST-запрос на конечную точку /api/courses/
    def create_course(self):
        return self.client.post('/api/courses/', self.course_data)


#проверяет функциональность создания нового курса
    def test_create_course(self):
        response = self.create_course()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().title, 'Test Course')


#проверяет функциональность получения деталей курса
    def test_retrieve_course(self):
        response = self.create_course()
        course_id = response.data['id']
        response = self.client.get(f'/api/courses/{course_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Course')

#проверяет функциональность обновления данных курса
    def test_update_course(self):
        response = self.create_course()
        course_id = response.data['id']
        updated_data = {'title': 'Updated Course Title'}
        response = self.client.put(f'/api/courses/{course_id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Course Title')


#проверяет функциональность удаления курса
    def test_delete_course(self):
        response = self.create_course()
        course_id = response.data['id']
        response = self.client.delete(f'/api/courses/{course_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


#создания курса и получаете course_id плюс фаворит
    def test_favorite_course(self):
        response = self.create_course()
        course_id = response.data['id']
        response = self.client.post(f'/api/courses/{course_id}/favorites/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('is_favorite' in response.data)
        self.assertTrue(response.data['is_favorite'])



