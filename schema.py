from graphene import (ObjectType, String, Int, Field, Schema, List)
from models import data
from person.PersonType import PersonType


class Query(ObjectType):
    all_people = List(PersonType)
    person = Field(PersonType, key=Int())

    def resolve_all_people(root, info):
        return data.values()

    def resolve_person(root, info, key):
        return data[key]


#schema
schema = Schema(query=Query)

# #query
# query_string="{allPeople{email lastName}}"

# print(schema.execute(query_string))