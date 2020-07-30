import json

from django.forms import model_to_dict
from graphene_django.utils import GraphQLTestCase
from model_bakery import baker

from sigma.schema import schema
from users.models import Contact


class TestContacts(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = '/graphql'
    REGISTER_MUTATION = '''
    mutation($name: String!, $email: String!, $city: String!, $state: String!) {
        register(name: $name, email: $email, city: $city, state: $state) {
            contact { name }
        }
    }'''

    def test_contact_with_invalid_email_can_not_register(self):
        contact = model_to_dict(baker.prepare('users.Contact', email='q@'))
        response = self.query(self.REGISTER_MUTATION, variables=contact)
        content = json.loads(response.content)
        self.assertDictEqual({'data': {'register': {'contact': None}}}, content)
        self.assertEqual(Contact.objects.count(), 0)

    def test_contact_can_be_registered(self):
        contact_fields = baker.prepare('users.Contact', email='q@q')
        contact = model_to_dict(contact_fields, exclude=['id'])
        response = self.query(self.REGISTER_MUTATION, variables=contact)
        content = json.loads(response.content)
        expected = {'data': {'register': {'contact': {'name': contact['name']}}}}
        self.assertDictEqual(expected, content)
        self.assertTrue(Contact.objects.filter(**contact).exists())

