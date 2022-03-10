
# from secrets import choice
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, full_name=None, date_of_birth=None, email=None, gender=None,
                    address=None, role=None, password=None, is_admin=False, shopname=None, shopdesc=None, shopaddress=None):

        if not email:
            raise ValueError('Users must have an email address attached ')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name
        )
        user.set_password(password)
        user.role = role
        user.full_name = full_name
        user.date_of_birth = date_of_birth
        user.gender = gender
        user.address = address
        user.is_active = True
        user.is_staff = False
        user.set_password(password)
        user.shopname = shopname
        user.shopaddress = shopaddress
        user.shopdesc = shopdesc
        user.save()
        return user

    def create_superuser(
        self,  full_name=None, date_of_birth=None,
        shopname=None, shopaddress=None, role="admin", shopdesc=None, email=None,
        gender=None, address=None,
        password=None
    ):
        # Admin creation
        user = self.create_user(
            email=email,
            password=password,
            full_name=full_name,
            gender=gender,
            address=address,
            date_of_birth=date_of_birth,
            role=role,
        )
        user.shopname = shopname
        user.shopaddress = shopaddress
        user.shopdesc = shopdesc
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


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
    role = models.CharField(max_length=10, default="customer")
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    shopaddress = models.CharField(null=True, blank=True, max_length=200)
    shopname = models.CharField(null=True, blank=True, max_length=50)
    shopdesc = models.CharField(null=True, blank=True, max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.role == "shopowner":
            return self.shopname
        return self.email

    def has_perm(self, obj=None):
        print(self, obj)
        return True

    def has_module_perms(self, app_label):
        print(self)
        return True

    @property
    def is_staff_user(self):
        return self.is_admin


class Category(models.Model):

    name = models.CharField(max_length=50)


class Brand(models.Model):

    name = models.CharField(max_length=50)


class Product(models.Model):
    """Model for products listed by shops"""
    categories = (
        ("clothing", "clothing"), ("electronics",
                                   "electronics"), ("footwear", "footwear"),

    )
    price = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default=None)
    color = models.CharField(max_length=20, null=True, blank=True)
    material = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def price_of(self):
        return self.price

    def is_available(self, required):
        # Checks availability of products
        return self.quantity > required


class rating(models.Model):

    value = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    rated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(default=None, null=True, blank=True)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Order(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()
    status = models.CharField(max_length=10)


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()
    status = models.CharField(max_length=50, default='Waiting for delivery')
