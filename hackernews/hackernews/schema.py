import graphene

import links.schema
import links.schema_relay
import users.schema
import graphql_jwt

class Query(links.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    users.schema.Mutation, 
    links.schema_relay.RelayMutation, 
    links.schema.Mutation, 
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(
    users.schema.Query,
    links.schema.Query,
    links.schema_relay.RelayQuery,
    graphene.ObjectType,
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)