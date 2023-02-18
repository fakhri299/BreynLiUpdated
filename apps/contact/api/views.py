from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView
from.serialziers import *


class ContactApiView(CreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()
    


class ConsultantApiView(CreateAPIView):
    serializer_class=ConsultantSerializer
    queryset=Consultant.objects.all()
    