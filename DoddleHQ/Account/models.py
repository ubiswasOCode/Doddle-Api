from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     password=models.CharField(max_length=200, blank=True)
#     phone_no=models.IntegerField( blank=True)
#     is_active = models.BooleanField(_('active'), default=True)
#     is_staff = models.BooleanField(_('staff'), default=False)


#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


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


class Project_list(models.Model):
    name=models.CharField(max_length=200, blank=True)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100, blank=True)

class Card(models.Model):
    name=models.CharField(max_length=100, blank=True)
    project_list=models.ForeignKey(Project_list, on_delete=models.CASCADE)


class Checklist(models.Model):
    card=models.ForeignKey(Card, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, blank=True)

class List_Table(models.Model):
    name=models.CharField(max_length=100, blank=True)
    checklist=models.ForeignKey(Checklist, on_delete=models.CASCADE)







