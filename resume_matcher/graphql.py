import graphene
from graphene_django.types import DjangoObjectType
from .models import JobPosting, MatchResult

class JobPostingType(DjangoObjectType):
    class Meta:
        model = JobPosting

class Query(graphene.ObjectType):
    job_postings = graphene.List(JobPostingType)

    def resolve_job_postings(self, info, **kwargs):
        return JobPosting.objects.all()

schema = graphene.Schema(query=Query)
