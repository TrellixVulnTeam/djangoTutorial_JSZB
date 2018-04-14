import tastypie
from tastypie.resources import ModelResource
from myapp.models import student
from myapp.models import Person
from myapp.models import Section
from tastypie import fields
from tastypie.authorization import Authorization

class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name= 'person'
        authorization = Authorization()
        fields = ['id', 'firstName', 'lastName']

class SectionResource(ModelResource):
    class Meta:
        queryset = Section.objects.all()
        resource_name= 'section'
        authorization = Authorization()

class StudentResource(ModelResource):
    person= fields.OneToOneField(PersonResource,'person',full=True)
    #person_id = fields.IntegerField(attribute='person_id', null=True)
    section= fields.ForeignKey(SectionResource, 'section')

    class Meta:
        queryset = student.objects.all().select_related("person")
        resource_name= 'pupil'
        authorization = Authorization()



