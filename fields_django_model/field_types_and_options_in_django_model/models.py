from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField      # pip install django-phonenumber-field, pip install django-phonenumbers


# blank=True affects form validation and allows the field to be left empty in forms.
# null=True affects the database and allows the field to have a NULL value.

# blank=False: makes field required in forms
# null=False: makes field required in Database
# NOTE: by default both are set to false


my_choices = (
    ('one', 'number one'),
    ('two', 'number two'),
    ('three', 'number three'),
    ('four', 'number four')
)


class TestModel(models.Model):
    boolean = models.BooleanField(default=True, verbose_name="this is a boolean field")
    char = models.CharField(max_length=220, unique=True, help_text="added help text", verbose_name="new Name")
    date = models.DateField(default=timezone.now)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=200)
    file = models.FileField(upload_to='uploads', blank=True)        # blank=True will make these fields optional. When saving the model instance, if no file is provided for the field, it will be stored as an empty value in the database. The field will not be set to NULL, but rather an empty string ('').
    image = models.FileField(upload_to='uploads', blank=True)       # The blank=True parameter affects form validation, indicating that the field is not required.
    integer = models.IntegerField()     # -2147483648 to 2147483648
    positive_integer = models.PositiveIntegerField()        # 0 to 2147483648
    positive_small_int = models.PositiveSmallIntegerField()     # 0 to 32767
    slug = models.SlugField(blank=True)
    text = models.TextField()
    url = models.URLField(max_length=200)
    uuid1 = models.UUIDField(default=uuid.uuid4)
    uuid2 = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    updated = models.DateTimeField(auto_now=True)       # auto_now: makes this field editable=False: Sets itself as now() whenever model is updated
    created = models.DateTimeField(auto_now_add=True)       # auto_now_add: makes this field editable=False: sets itself to date time when instance created
    date_and_time = models.DateTimeField()
    choice = models.CharField(max_length=10, choices=my_choices)
    phone_number = PhoneNumberField
    user = models.ForeignKey(User, models.CASCADE, null=True)
    new_field2 = models.CharField(max_length=20, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text[:30])
        super(TestModel, self).save(*args, **kwargs)