from django.urls import path
from rest_framework import routers
from .views import *
router=routers.SimpleRouter()


router.register(r'student',StudentViewSet,basename='student')


urlpatterns =router.urls+ [

]