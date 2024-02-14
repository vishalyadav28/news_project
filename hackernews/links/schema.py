import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from graphql_jwt.decorators import login_required
import graphql_jwt
from django.db.models import Q

from .models import Link, Vote


class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    links = graphene.List(LinkType, search=graphene.String(), first=graphene.Int(),
        skip=graphene.Int(),)
    votes = graphene.List(VoteType)

    def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
        if search:
            filter = (
                Q(url__icontains=search) |
                Q(description__icontains= search) 
                )
            qs = Link.objects.filter(filter)
            if skip:
                qs = qs[skip:]
            if first:
                qs = qs[:first]
            return qs
        return Link.objects.all()
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()



class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        user = info.context.user

        if user.is_anonymous:
            user = None

        link = Link(
            url=url,
            description=description,
            posted_by=user,
        )
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            posted_by=link.posted_by,
        )


class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    link = graphene.Field(LinkType)

    class Arguments:
        link_id = graphene.Int()
        
    @login_required
    def mutate(self, info, link_id):
        user = info.context.user
        
        if user.is_anonymous:
            raise Exception('You must be logged in to vote!')
        link = Link.objects.filter(id=link_id).first()
        if not link:
            raise Exception('Invalid Link!')

        Vote.objects.create(
            user=user,
            link=link,
        )

        return CreateVote(user=user, link=link)

#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_vote = CreateVote.Field()

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
