import graphene
from .models import Resume

class UploadResume(graphene.Mutation):
    class Arguments:
        file = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file):
        # Lógica de upload
        Resume.objects.create(file=file)
        return UploadResume(success=True)

class Mutation(graphene.ObjectType):
    upload_resume = UploadResume.Field()

schema = graphene.Schema(mutation=Mutation)
