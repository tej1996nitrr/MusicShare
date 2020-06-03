import graphene
from graphene_django import DjangoObjectType
from .models import Tracks

class TrackType(DjangoObjectType):
    class Meta:
        model = Tracks

class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)

    def resolve_tracks(self,info):
        return Tracks.objects.all()