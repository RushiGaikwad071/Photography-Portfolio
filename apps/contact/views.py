from rest_framework import viewsets
# from .models import ContactMessage
# from .serializers import ContactMessageSerializer
from .models import Contact
from .serializers import ContactSerializer

# class ContactMessageViewSet(viewsets.ModelViewSet):
#     # queryset = ContactMessage.objects.all()
#     queryset = Contact.objects.all()
#     serializer_class = ContactMessageSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
