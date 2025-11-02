from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .permissions import IsAdminUser

@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})

from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

from django.http import JsonResponse
from django.views import View

class UserListView(View):
    def get(self, request):
        return JsonResponse({"message": "User API working!"})
