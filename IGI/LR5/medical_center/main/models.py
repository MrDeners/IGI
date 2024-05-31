from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.

class Diagnosis(models.Model):
    name = models.CharField(max_length=30)
    medicines = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Diagnosis'
        verbose_name_plural = 'Diagnoses'


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    sphere = models.CharField(max_length=20)
    education = models.TextField()
    careerStartTime = models.DateField()
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='doctors')
    photo = models.ImageField(upload_to='photos')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class ClientCard(models.Model):
    name = models.CharField(max_length=30)
    diagnoses = models.ManyToManyField(Diagnosis)
    doctors = models.ManyToManyField(Doctor, related_name='client')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ClientCard'
        verbose_name_plural = 'ClientCards'


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('client', 'Client'),
    )
    doctorCard = models.OneToOneField(Doctor, on_delete=models.CASCADE, blank=True)
    timezone = models.CharField(max_length=32, default='UTC')
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client', blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)], blank=True, null=True,
                                      default=18)
    dateOfRegistration = models.DateField('Date of Registration', default=now)
    clientCard = models.OneToOneField(ClientCard, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=30)
    doctor = models.ManyToManyField(Doctor, related_name='services')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceSet(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    services = models.ManyToManyField(Service, related_name='serviceSets')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ServiceSer'
        verbose_name_plural = 'ServiceSet'


class Department(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'


class Appointment(models.Model):
    time = models.DateTimeField(default=now)
    services = models.ManyToManyField(Service, related_name='appointments')
    customer = models.ForeignKey(ClientCard, on_delete=models.CASCADE, related_name='appointments')
    objects = models.Manager()

    def __str__(self):
        return f"Appointment #{self.customer.name} for {self.services} on {self.time}"

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'


class Schedule(models.Model):
    monday_start = models.TimeField()
    monday_end = models.TimeField()
    tuesday_start = models.TimeField()
    tuesday_end = models.TimeField()
    wednesday_start = models.TimeField()
    wednesday_end = models.TimeField()
    thursday_start = models.TimeField()
    thursday_end = models.TimeField()
    friday_start = models.TimeField()
    friday_end = models.TimeField()

    def __str__(self):
        return 'Monday: {} - {}'.format(self.monday_start, self.monday_end)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'


class News(models.Model):
    name = models.CharField('Name', max_length=100)
    text = models.TextField('Text', )
    created_at = models.DateTimeField('Creation data', default=now)
    photo = models.ImageField(upload_to='photos')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News's"


class About(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', )
    created = models.DateTimeField('Creation data', default=now)
    photo = models.ImageField(upload_to='photos')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = "Abouts"


class Faq(models.Model):
    question = models.CharField('Question', max_length=200)
    answer = models.TextField('Answer', )
    created = models.DateTimeField('Creation data', default=now)
    objects = models.Manager()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Faq'
        verbose_name_plural = "Faqs"


class TermCondition(models.Model):
    text = models.TextField('Text', )
    objects = models.Manager()

    def __str__(self):
        return 'Term and condition'

    class Meta:
        verbose_name = 'TermCondition'
        verbose_name_plural = "TermConditions"


class Vacancy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    salary = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = "Vacancies"


class Review(models.Model):
    GRADES = ('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)
    name = models.CharField(max_length=50)
    grade = models.CharField(max_length=1, choices=GRADES, default='5')
    text = models.TextField()
    created = models.DateTimeField(default=now)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = "Reviews"


class Code(models.Model):
    STATUS = ('active', 'Active'), ('archive', 'Archive')
    code = models.CharField(max_length=10)
    status = models.CharField(max_length=10, choices=STATUS, default='active')
    objects = models.Manager()

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = "Codes"
