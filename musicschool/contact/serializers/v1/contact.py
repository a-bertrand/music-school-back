from musicschool.contact.models import Contact
from rest_framework import serializers


class Contacterializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =  ['__all__']