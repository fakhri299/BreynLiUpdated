from contact.models import *
from rest_framework.serializers import ModelSerializer



class ContactSerializer(ModelSerializer):
    class Meta:
        model=Contact
        fields=['fullname','email','number','title','subject']


class ConsultantSerializer(ModelSerializer):
    class Meta:
        model=Consultant
        fields=['fullname','email','message']
