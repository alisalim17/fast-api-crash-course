from ariadne.asgi import GraphQL
from ariadne import ObjectType, make_executable_schema

type_defs = """
    type Query {
        hello: String!
        user: User
    }

    type User {
        username: String!
    }
"""

query = ObjectType("Query")


@query.field("user")
def resolve_user(_, info):
    return {"first_name": "Jake", "last_name": "Paul"}


user = ObjectType("User")


@user.field("username")
def resolve_username(obj, *_):
    return f'{obj["first_name"]} {obj["last_name"]}'


schema = make_executable_schema(type_defs, query, user)
app = GraphQL(schema, debug=True)