import json

from django.forms import model_to_dict
from graphene_django.utils import GraphQLTestCase
from model_bakery import baker

from sigma.schema import schema
from users.models import User


class TestUsers(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = '/graphql'
    REGISTER_MUTATION = '''
    mutation($name: String!, $email: String!, $city: String!, $department: String!) {
        register(name: $name, email: $email, city: $city, department: $department) {
            user { name }
        }
    }'''

    def test_user_with_invalid_email_can_not_register(self):
        user = model_to_dict(baker.prepare('users.User', email='q@q.q'))
        response = self.query(self.REGISTER_MUTATION, variables=user)
        content = json.loads(response.content)
        self.assertDictEqual({'data': {'register': {'user': None}}}, content)
        self.assertEqual(User.objects.count(), 0)

    def test_user_can_be_registered(self):
        user = model_to_dict(baker.prepare('users.User'), exclude=['id'])
        response = self.query(self.REGISTER_MUTATION, variables=user)
        content = json.loads(response.content)
        expected = {'data': {'register': {'user': {'name': user['name']}}}}
        self.assertDictEqual(expected, content)
        self.assertTrue(User.objects.filter(**user).exists())

