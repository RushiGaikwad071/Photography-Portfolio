from rest_framework import serializers
# from .models import ContactMessage
from .models import Contact

# class ContactMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ContactMessage
#         
#         fields = ["id", "name", "email", "subject", "message", "created_at"]
#         


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'