from musicschool.contact.models import Contact
from rest_framework import viewsets
from musicschool.contact.serializers.v1 import ContactSerializer


# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
