from django.urls import path
from contact.api.views import *



urlpatterns = [
    
path('contact',ContactApiView.as_view()),
path('consultant',ConsultantApiView.as_view())

]