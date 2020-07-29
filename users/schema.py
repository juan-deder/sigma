from django.core.exceptions import ValidationError
from graphene import Mutation, String, Field, List
from graphene_django import DjangoObjectType

from users.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class RegisterMutation(Mutation):
    class Arguments:
        name = String()
        email = String()
        city = String()
        department = String()

    user = Field(UserType)

    def mutate(self, info, **kwargs):
        user = User(**kwargs)
        try:
            user.full_clean()
        except ValidationError as e:
            user = None
        else:
            user.save()
        return RegisterMutation(user=user)


class Query(object):
    users = List(UserType)


class Mutation(object):
    register = RegisterMutation.Field()
