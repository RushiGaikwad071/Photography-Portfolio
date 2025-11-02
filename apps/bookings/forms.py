from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            "client_name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "client_email": forms.EmailInput(attrs={"placeholder": "Your email"}),
            "client_phone": forms.TextInput(attrs={"placeholder": "Your phone number"}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"}),
            "package": forms.Select(attrs={"class": "form-select"}),
            "location": forms.TextInput(attrs={"placeholder": "Location"}),
            "notes": forms.Textarea(attrs={"rows": 4, "placeholder": "Any special requests?"}),
        }

