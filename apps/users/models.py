# apps/users/models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     # Roles: admin, photographer, client
#     is_photographer = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=False)

#     phone = models.CharField(max_length=50, blank=True, null=True)
#     thumbnail = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True)

#     def __str__(self):
#         return self.get_full_name() or self.username
#     pass
# class User(AbstractUser):
#     """Custom user model."""
#     display_name = models.CharField(max_length=255, blank=True)
#     bio = models.TextField(blank=True)
#     profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)
#     website = models.URLField(blank=True)

#     def __str__(self):
#         return self.display_name or self.username


from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Roles
    is_photographer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    # Extra fields
    phone = models.CharField(max_length=50, blank=True, null=True)
    thumbnail = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True)

    # Avoid reverse accessor clashes
    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.get_full_name() or self.username
