
from secrets import choice
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    # Creating CUSTOMER AND SHOP
    def create_user(self, full_name=None, date_of_birth=None, email=None, gender=None,
                    address=None, role=None, password=None):
        if not email:
            raise ValueError('Users must have an email address attached ')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            date_of_birth=date_of_birth,
            gender=gender,
            address=address,
            role=role
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_admin = False
        user.set_password(password)
        user.save()
        return user

    # Creating ADMIN
    def create_superuser(self,  full_name=None, date_of_birth=None, is_shop_user=False, shopname=None,
                         shopaddress=None, shopdesc=None, email=None, gender=None, address=None,
                         password=None):

        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            gender=gender,
            address=address,
            date_of_birth=date_of_birth,
        )
        user.shopname = shopname
        user.shopaddress = shopaddress
        user.shopdesc = shopdesc
        user.is_admin = True
        user.is_staff = True
        user.role = "admin"
        user.save()
        return user


# Base MODEL (Customer and Shop)
class User(AbstractBaseUser):
    genderchoices = [
        ("M", "Male"),
        ("F", "Female")
    ]
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    full_name = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=genderchoices, null=True)
    address = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=10)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    shopaddress = models.CharField(null=True, blank=True, max_length=200)
    shopname = models.CharField(null=True, blank=True, max_length=50)
    shopdesc = models.CharField(null=True, blank=True, max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
        # Returns unique email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        #    checks User Permission
        return True

    @property
    def is_staff_user(self):
        return self.is_admin
        # returns boolen if its a staff member


class Product(models.Model):
    categories = (("clothing", "clothing"),
                  ("electronics", "electronics"), ("footwear", "footwear"))
    price = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=categories, max_length=50)
    quantity = models.IntegerField()
    provider = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_available(self, required):
        if self.quantity > required:
            return True
        else:
            return False

    def price_of(self):
        return self.price