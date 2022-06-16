from tokenize import String
from graphene import (ObjectType, String, Int, Field, Schema, List)
"""
    class PersonType:
        email:str
        first_name:str
        last_name:str
        age:int
"""


class PersonType(ObjectType):
    email = String()
    first_name = String()
    last_name = String()
    age = Int()

    #resolvers
    def resolve_email(person, info):
        return person.email

    def resolve_first_name(person, info):
        return person.first_name

    def resolve_last_name(person, info):
        return person.last_name

    def resolve_age(person, info):
        return person.age
