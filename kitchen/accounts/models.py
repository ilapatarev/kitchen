from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models




class KitchenUserManager(BaseUserManager):
	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('The Email field must be set')

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self.create_user(email, password, **extra_fields)


class KitchenUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = KitchenUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.email


class Profile(models.Model):
	user = models.OneToOneField(KitchenUser, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=30, blank=True, null=True,)
	last_name = models.CharField(max_length=30, blank=True, null=True,)
	age = models.PositiveIntegerField(default=0)
	cooking_description = models.CharField(max_length=50, blank=True, null=True,)
	image_url = models.URLField(max_length=200, blank=True, null=True)
	def __str__(self):
		return self.user.email
