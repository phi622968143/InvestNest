# Generated by Django 4.2.8 on 2024-06-12 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("user_balance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Account",
            fields=[
                ("acc_id", models.AutoField(primary_key=True, serialize=False)),
                ("acc_balance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("bank_name", models.CharField(max_length=100)),
                ("open_date", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Dividend",
            fields=[
                ("dividend_id", models.AutoField(primary_key=True, serialize=False)),
                ("stock_name", models.CharField(max_length=100)),
                ("ex_date", models.DateField()),
                ("pay_date", models.DateField()),
                (
                    "dividend_per_share",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                ("trade_id", models.AutoField(primary_key=True, serialize=False)),
                ("stock_name", models.CharField(max_length=100)),
                ("stock_code", models.CharField(max_length=10)),
                ("action", models.CharField(max_length=10)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.IntegerField()),
                ("date", models.DateField()),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.account"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Receive",
            fields=[
                ("receive_id", models.AutoField(primary_key=True, serialize=False)),
                ("stock_name", models.CharField(max_length=100)),
                (
                    "receive_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("receive_date", models.DateField()),
                ("quantity", models.IntegerField()),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.account"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Distribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stock_name", models.CharField(max_length=100)),
                (
                    "dividend",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.dividend"
                    ),
                ),
            ],
        ),
    ]
