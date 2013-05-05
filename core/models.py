from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.utils import timezone


class Present(models.Model):

    item_link = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=500)
    cost = models.FloatField(default=0.0)
    image_link = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'table_present'


class CustomUserManager(BaseUserManager):

    def create_user(self, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_staff=False, is_active=True, is_superuser=False, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('e-mail address', max_length=200, unique=True, db_index=True)
    is_staff = models.BooleanField('staff status', default=False,
        help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    tz_offset = models.IntegerField(default=0)
    facebook_id = models.CharField(max_length=200, blank=True, null=True)
    display_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'table_user'
        verbose_name = 'User'


class Birthday(models.Model):

    facebook_id = models.CharField(max_length=200)
    birthday = models.DateField()
    amount_raised = models.FloatField(default=0.0)
    amount_target = models.FloatField(default=0.0)
    shipping_address = models.TextField(blank=True, null=True)
    shipping_province_state = models.CharField(max_length=200, blank=True, null=True)
    shipping_country = models.CharField(max_length=200, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=100, blank=True, null=True)
    shipping_phone = models.CharField(max_length=100, blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.facebook_id, self.birthday)

    class Meta:
        db_table = 'table_birthday'


class BirthdayContribution(models.Model):

    birthday = models.ForeignKey(Birthday, related_name='%(class)s_birthday')
    contributor = models.ForeignKey(User, related_name='%(class)s_contributor')
    amount = models.FloatField(default=0.0)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s -> %s [%s]' % (self.birthday.id, self.contributor.id, self.amount)

    class Meta:
        db_table = 'table_birthday_contribution'
