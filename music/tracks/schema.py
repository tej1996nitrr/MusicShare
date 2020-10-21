import graphene
from graphene_django import DjangoObjectType
from .models import Tracks

class TrackType(DjangoObjectType):
    class Meta:
        model = Tracks

class Query(graphene.ObjectType):
    tracks = graphene.List(TrackType)
    track = graphene.Field(TrackType, id=graphene.Int(required=True))

    def resolve_tracks(self, info):
        return Tracks.objects.all()
    
    def resolve_track(self, info, id):
        return Tracks.objects.get(id=id)
    

class CreateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)
    class Arguments:
        # Defines the data you can send to the server, in this case, the title, description, url
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()

    # mutation method: it creates a link in the database using the data sent by the user,
    def mutate(self, info, title, description, url):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Log in to add a track.')

        track = Tracks(title=title, description=description, url=url, posted_by=user)
        track.save()
        return CreateTrack(track=track)

# Creates a mutation class with a field to be resolved, which points to our mutation defined befor
class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
        