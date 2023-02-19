from rest_framework.generics import CreateAPIView,RetrieveAPIView,ListAPIView
from.serialziers import *
from rest_framework.response import Response
from rest_framework import status



class ContactApiView(CreateAPIView):
    serializer_class=ContactSerializer
    queryset=Contact.objects.all()

    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers=self.get_success_headers(data=serializer.data)   
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)

    


class ConsultantApiView(CreateAPIView):
    serializer_class=ConsultantSerializer
    queryset=Consultant.objects.all()


    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers=self.get_success_headers(data=serializer.data)   
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)

    
    