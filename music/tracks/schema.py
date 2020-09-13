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
class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)
    class Arguments:
        # Defines the data you can send to the server, in this case, the title, description, url
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    # mutation method: it creates a link in the database using the data sent by the user,
    def mutate(self,info,title,description,url):
        track = Tracks(title=title,description=description,url=url)
        track.save()
        return CreateTrack(track=track)
        
# Creates a mutation class with a field to be resolved, which points to our mutation defined befor
class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
        