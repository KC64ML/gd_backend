from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.


class Communicatewithpeople(models.Model):
    chattinghistory = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    user_pk_userid = models.OneToOneField(
        'User', models.DO_NOTHING, db_column='User_pk_userid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'communicatewithpeople'


class Diary(models.Model):
    password = models.CharField(max_length=20)
    date = models.CharField(max_length=10)
    contents = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    user_pk_userid = models.OneToOneField(
        'User', models.DO_NOTHING, db_column='User_pk_userid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'diary'


class Drugnotification(models.Model):
    approximately_time_remaining = models.CharField(
        max_length=20, blank=True, null=True)
    drug_name = models.CharField(max_length=20, blank=True, null=True)
    # Field name made lowercase.
    user_pk_userid = models.OneToOneField(
        'User', models.DO_NOTHING, db_column='User_pk_userid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'drugnotification'


class Game(models.Model):
    gamerecord = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    user_pk_userid = models.OneToOneField(
        'User', models.DO_NOTHING, db_column='User_pk_userid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'game'


class Location(models.Model):
    rarea = models.CharField(max_length=20)
    # Field name made lowercase.
    locationcol = models.CharField(db_column='Locationcol', max_length=45)
    # Field name made lowercase.
    user_pk_userid = models.OneToOneField(
        'User', models.DO_NOTHING, db_column='User_pk_userid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'location'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    pk_userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=45)
    phonenumber = models.CharField(max_length=12)
    email = models.CharField(
        unique=True,
        max_length=64
    )
    familyname = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    dateofonesbirth = models.CharField(max_length=6)

    # login을 위한 소스
    # is_staff, is_active
    # date_joined
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('username')
        verbose_name_plural = _('username')

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email
