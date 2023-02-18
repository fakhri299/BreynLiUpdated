from django.urls import path
from contact.api.views import *

path('contact',ContactApiView.as_view()),
path('consultant',ConsultantApiView.as_view())
