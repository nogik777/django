from api.models import CourseRecource, CategoryResource
from tastypie.api import Api
from django.urls import path, include

api = Api(api_name='v1')
api.register(CourseRecource())
api.register(CategoryResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
