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

class UpdateTrack(graphene.Mutation):
    track = graphene.Field(TrackType)

    class Arguments:
        track_id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
    
    def mutate(self, info, track_id, title, description, url):
        user = info.context.user
        track=Tracks.objects.get(id=track_id)

        if track.posted_by != user:
            raise Exception('Not permitted to update this track.')

        track.title = title
        track.description = description
        track.url = url
        track.save()
        return UpdateTrack(track=track)

class DeleteTrack(graphene.Mutation):
    track_id = graphene.Int()

    class Arguments:
        track_id = graphene.Int(required=True)
    
    def mutate(self,info, track_id):
        user = info.context.user
        track = Tracks.objects.get(id=track_id)

        if track.posted_by != user:
            raise Exception('Not permitted to delete this track.')

        track.delete()

        return DeleteTrack(track_id=track_id)
# Creates a mutation class with a field to be resolved, which points to our mutation defined before
class Mutation(graphene.ObjectType):
    create_track = CreateTrack.Field()
    update_track = UpdateTrack.Field()
    delete_track = DeleteTrack.Field()
        