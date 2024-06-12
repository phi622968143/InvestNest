# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
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
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    user_balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

class Account(models.Model):
    acc_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    acc_balance = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=100)
    open_date = models.DateField()

class Trade(models.Model):
    trade_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    stock_code = models.CharField(max_length=10)
    action = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()

class Dividend(models.Model):
    dividend_id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=100)
    ex_date = models.DateField()
    pay_date = models.DateField()
    dividend_per_share = models.DecimalField(max_digits=10, decimal_places=2)

class Receive(models.Model):
    receive_id = models.AutoField(primary_key=True)
    stock_name = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    receive_amount = models.DecimalField(max_digits=10, decimal_places=2)
    receive_date = models.DateField()
    quantity = models.IntegerField()  # 新增的字段

class Distribute(models.Model):
    stock_name = models.CharField(max_length=100)
    dividend = models.ForeignKey(Dividend, on_delete=models.CASCADE)
