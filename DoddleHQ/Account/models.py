from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(
        self, email, password=None, is_staff=False, is_active=True, is_superuser=False, **extra_fields
    ):
        """Create a user instance with the given email and password."""
        email = UserManager.normalize_email(email)
        extra_fields.pop("username", None)
        user = self.model(
            email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser ,**extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(
            email, password, is_staff=True, is_superuser=True, **extra_fields
        )
    # def users(self):
    #     return self.get_queryset().filter(
    #         Q(is_staff=False) & Q(is_superuser=False)
    #     )
class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ("email",)

    def __str__(self):
        return self.email



class Project(models.Model):
    name=models.CharField(max_length=200, blank=True)
    user=models.ManyToManyField(User)

    def __str__(self):
        return self.name



class Project_list(models.Model):
    name=models.CharField(max_length=200, blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name



class Card(models.Model):
    name=models.CharField(max_length=100, blank=True)
    project_list=models.ForeignKey(Project_list, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Checklist(models.Model):
    card=models.ForeignKey(Card, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name



class List_Table(models.Model):
    name=models.CharField(max_length=100, blank=True)
    checklist=models.ForeignKey(Checklist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name







