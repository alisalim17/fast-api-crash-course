from calendar import Calendar
from ariadne.asgi import GraphQL
from ariadne import ObjectType, make_executable_schema
from ariadne import MutationType
from fastapi import FastAPI
import uvicorn

type_defs = """
    type User {
        username: String!
    }
    
    type Query {
        holidays(year: Int): String!
        hello: String!
        user: User
    }

    
    type Mutation {
        login(username: String!, password: String!): Boolean!
        logout: Boolean!
    }

    
"""
mutation = MutationType()
query = ObjectType("Query")


@mutation.field('login')
def resolve_login(_, info, username, password):
    request = info.context["request"]

    if request["is_authenticated"] and username == "Ali":
        return True
    return False


@mutation.field('logout')
def resolve_logout(_, info):
    request = info.context["request"]
    if request.is_authenticated:
        # auth.logout(request)
        # some logout process
        return True
    return False


@query.field("holidays")
def resolve_holidays(*_, year=None):
    print(year)
    return year


@query.field("user")
def resolve_user(_, info):
    return {"first_name": "Jake", "last_name": "Paul"}


user = ObjectType("User")


@user.field("username")
def resolve_username(obj, *_):
    return f'{obj["first_name"]} {obj["last_name"]}'


def get_context_value(request):
    return {'request': {"is_authenticated": True}, 'test': "TEST"}


schema = make_executable_schema(type_defs, query, mutation, user)
graphql_app = GraphQL(schema, context_value=get_context_value, debug=True)

app = FastAPI()
app.add_route("/graphql", graphql_app)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)
