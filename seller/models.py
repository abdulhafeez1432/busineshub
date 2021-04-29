from django.db import models
from account.models import User
from businesshub.validators import validate_file_size, validate_file_extension, validate_file_extension02
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class SellerProfile(models.Model):

    SEX = (
        ('1', 'Male'),
        ('2', 'Female')
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phonenumber = models.CharField("Phone Number", max_length=50)
    passport = models.ImageField("Passport Photography", upload_to='seller/', validators=[
                                 validate_file_size, validate_file_extension02], null=True)

    address = models.CharField('Contact Address', max_length=250)
    country = models.CharField('Country', max_length=50)
    dob = models.DateField("Date of Birth", default="2019-06-04")
    age = models.IntegerField(validators=[
        MaxValueValidator(70),
        MinValueValidator(18)
    ], default=18)
    occupation = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX, default="Male", max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Seller Profile"
        verbose_name_plural = "Seller Profiles"

    def __str__(self):
        return self.user.username + ' - ' + self.phonenumber

    '''
    def get_absolute_url(self):
        return reverse("Seller-details", kwargs={"pk": self.pk})
    '''

    def business(self):
        return self.business.all()


class Business(models.Model):

    FLIP_TYPE = (
        ('1', 'Buy Out'),
        ('2', 'Partnership')
    )

    TYPE = (
        ('1', 'Business Name'),
        ('2', 'Sole Proprietorship'),
        ('3', 'Partnerships'),
        ('4', 'Limited Partnership'),
        ('5', 'Corporation'),
        ('6', 'Limited Liability Company'),
        ('7', 'Nonprofit Organization'),
        ('8', 'Cooperative')
    )

    user = models.ForeignKey(
        User, related_name='business', on_delete=models.CASCADE)
    flip = models.CharField(
        "Type of Flipping", max_length=150, choices=FLIP_TYPE)

    name = models.CharField('Busniess Name', max_length=50)

    """ status = models.CharField('Registration Status',
                            max_length=50, choices=STATUS) """
    status = models.BooleanField("Regsitration Status", default=False)

    registration = models.CharField(
        'Regsitraion Number', max_length=25, blank=True, null=True)
    t_business = models.CharField(
        "Business Type", max_length=120, choices=TYPE)
    approval = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # TODO: Define fields here

    class Meta:
        """Meta definition for Business."""

        verbose_name = 'Business'
        verbose_name_plural = 'Businesss'

    def __str__(self):
        """Unicode representation of Business."""
        return f'{self.user.username} + {self.name}'


class Industry(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        """Unicode representation of AboutBUsiness."""
        return f'{self.name}'

    def get_about_business(self):
        return self.aboutbusines_set.all()


class AboutBusiness(models.Model):

    """Model definition for AboutBUsiness."""
    business = models.OneToOneField(
        Business, related_name="about", on_delete=models.CASCADE)
    founder = models.CharField(
        "OwnerShip Name", help_text="Seperate the name with comma", max_length=500)
    found = models.IntegerField(
        ("When Found"), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    about = models.TextField("About The Business")
    #industry = models.CharField(max_length=150)
    industry = models.ManyToManyField(Industry)
    location = models.CharField("Business Location", max_length=120)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for AboutBUsiness."""

        verbose_name = 'AboutBusiness'
        verbose_name_plural = 'AboutBusinesss'

    def __str__(self):
        """Unicode representation of AboutBUsiness."""
        return f'{self.business.name}'


class BusinessTarget(models.Model):
    """Model definition for BusinessTarget."""

    business = models.OneToOneField(
        Business, related_name="target", on_delete=models.CASCADE)
    demographic = models.CharField(max_length=150)
    psychographic = models.CharField(max_length=150)
    behavioral = models.CharField(max_length=150)
    geographic = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    '''

    Demographic segmentation: age, gender, education, marital status, race, religion, etc.
    Psychographic segmentation: values, beliefs, interests, personality, lifestyle, etc.
    Behavioral segmentation: purchasing or spending habits, user status, brand interactions, etc.
    Geographic Areas: neighborhood, area code, city, region, country, etc.

    '''

    # TODO: Define fields here

    class Meta:
        """Meta definition for BusinessTarget."""

        verbose_name = 'BusinessTarget'
        verbose_name_plural = 'BusinessTargets'

    def __str__(self):
        """Unicode representation of BusinessTarget."""
        return f'{self.business.name}'


class BusinesStaff(models.Model):
    CURRENCY = (
        ('1', 'EUR'),
        ('2', 'USD'),
        ('3', 'NAR'),
        ('4', 'GBP')
    )
    """Model definition for BusinesStaff."""
    business = models.OneToOneField(
        Business, related_name='staff', on_delete=models.CASCADE)
    howmany = models.IntegerField("How Many Staff", default=1)
    paying = models.IntegerField("How many Paying  Staff", default=1)
    nonpaying = models.IntegerField("How many Non-Paying Staff", default=1)
    currency = models.CharField(
        "Payment Currency", max_length=50, choices=CURRENCY)
    maxpayment = models.FloatField(
        "Maximum Paid Staff per Month", default=00.00)
    minpayment = models.FloatField(
        "Minimum Paid Staff per Month", default=00.00)
    total = models.FloatField("Total Salary Paid per Month", default=00.00)

    year = models.FloatField("Total Salary Paid per Year", default=00.00)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BusinesStaff."""

        verbose_name = 'BusinesStaff'
        verbose_name_plural = 'BusinesStaffs'

    def __str__(self):
        """Unicode representationheight_field=None, width_field=None, of BusinesStaff."""
        return f'{self.business.name}'


class BusinessFinancial(models.Model):
    """Model definition for BusinessFinancial."""
    business = models.ForeignKey(
        Business, related_name='financial', on_delete=models.CASCADE)
    bestyear = models.FloatField("Total Best Income For Year", default=00.00)
    badtyear = models.FloatField("Total Worst Income For Year", default=00.00)
    averageyear = models.FloatField("Average Income Per Year", default=00.00)
    avaragemonth = models.FloatField("Average Income Per Month", default=00.00)
    moneyhand = models.FloatField("Money At Hand or Bank", default=00.00)
    debt = models.FloatField("Debt", default=00.00)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BusinessFinancial."""

        verbose_name = 'BusinessFinancial'
        verbose_name_plural = 'BusinessFinancials'

    def __str__(self):
        """Unicode representation of BusinessFinancial."""
        return f'{self.business.name}'


class BusinessDocument(models.Model):
    """Model definition for BusinessDocument."""
    business = models.ForeignKey(
        Business, related_name='document', on_delete=models.CASCADE)
    document = models.ImageField("Passport Phpassotography", upload_to='documents/', validators=[
                                 validate_file_size, validate_file_extension02], null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for BusinessDocument."""

        verbose_name = 'BusinessDocument'
        verbose_name_plural = 'BusinessDocuments'

    def __str__(self):
        """Unicode representation of BusinessDocument."""
        return f'{self.business.name}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
