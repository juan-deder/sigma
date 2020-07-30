from django.core.exceptions import ValidationError
from graphene import Mutation, String, Field, List
from graphene_django import DjangoObjectType

from users.models import Contact


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact


class RegisterMutation(Mutation):
    class Arguments:
        name = String()
        email = String()
        city = String()
        state = String()

    contact = Field(ContactType)

    def mutate(self, info, **kwargs):
        contact = Contact(**kwargs)
        try:
            contact.full_clean()
        except ValidationError as e:
            contact = None
        else:
            contact.save()
        return RegisterMutation(contact=contact)


class Query(object):
    contacts = List(ContactType)


class Mutation(object):
    register = RegisterMutation.Field()
