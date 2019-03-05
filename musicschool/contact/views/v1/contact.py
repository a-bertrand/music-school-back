from musicschool.contact.models import Contact
from rest_framework import viewsets
from donation_service.donation.serializers.v1 import CartSerializer


# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
