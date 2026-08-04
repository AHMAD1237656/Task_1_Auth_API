from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("user", "User"),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="user",
    )
    is_email_verified = models.BooleanField(default=False)

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username