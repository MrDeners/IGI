from django.contrib import admin
from .models import Diagnosis, Doctor, ClientCard, CustomUser, Service, ServiceSet, Schedule, Department, News, \
    About, Faq, TermCondition, Vacancy, Review, Code, Appointment, ShopCart, Partner, History, Prop

# Register your models here.

admin.site.register(Diagnosis)
admin.site.register(About)
admin.site.register(Faq)
admin.site.register(TermCondition)
admin.site.register(Vacancy)
admin.site.register(Doctor)
admin.site.register(ClientCard)
admin.site.register(CustomUser)
admin.site.register(Service)
admin.site.register(ServiceSet)
admin.site.register(Schedule)
admin.site.register(Department)
admin.site.register(News)
admin.site.register(Review)
admin.site.register(Code)
admin.site.register(Appointment)
admin.site.register(ShopCart)
admin.site.register(Partner)
admin.site.register(Prop)
admin.site.register(History)
