from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class DiaryUserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("ユーザーネームを入力してください")
        if not email:
            raise ValueError("Emailを入力して下さい")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, username, email, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("first_name", "DEFAULT_FIRST_NAME")
        extra_fields.setdefault("last_name", "DEFAULT_LAST_NAME")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("is_staff=Trueである必要があります。")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("is_superuser=Trueである必要があります。")
        return self._create_user(username, email, **extra_fields)


class DiaryUser(AbstractBaseUser, PermissionsMixin):
    class_id = models.IntegerField(null=True, unique=True)
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(
        _("first name"), max_length=50, blank=False, null=False)
    last_name = models.CharField(
        _("last name"), max_length=50, blank=False, null=False)
    email = models.EmailField(_("email address"), blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = DiaryUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class DiaryManager(models.Manager):
    pass


class Diary(models.Model):
    writer = models.ForeignKey(DiaryUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    main_text = models.TextField(max_length=2000, blank=True, null=True)
    pub_date = models.DateTimeField("作成日時")
    TEMPORARY = "T"
    UNAPPROVED = "U"
    APPROVED = "A"
    DELETED = "D"
    PUBLIC_MODE_CHOICES = [
        (TEMPORARY, "一次保存"),
        (UNAPPROVED, "公開申請"),
        (APPROVED, "公開済"),
        (DELETED, "削除"),
    ]
    public_mode = models.CharField(
        max_length=1,
        choices=PUBLIC_MODE_CHOICES,
        default=TEMPORARY,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posted_diaries"
        verbose_name_plural = "Diaries"
