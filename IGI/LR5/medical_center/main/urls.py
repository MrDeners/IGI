"""
URL configuration for medical_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import logout
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='home'),
    re_path(r'^register/$', views.SignUpView.as_view(), name='sign_up'),
    re_path(r'^login/$', views.SignInView.as_view(), name='sign_in'),
    re_path(r'^sign_out/$', views.signout, name='sign_out'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^news/$', views.NewsView.as_view(), name='news'),
    re_path(r'^faq/$', views.FAQView.as_view(), name='faq'),
    re_path(r'^contacts/$', views.ContactsView.as_view(), name='contacts'),
    re_path(r'^term_condition/$', views.TermConditionView.as_view(), name='term_condition'),
    re_path(r'^vacancies/$', views.VacancyView.as_view(), name='vacancies'),
    re_path(r'^reviews/$', views.ReviewsView.as_view(), name='reviews'),
    re_path(r'^codes_and_coupons/$', views.CodesAndCouponsView.as_view(), name='codes_and_coupons'),
    re_path(r'^create_review/$', views.CreateReviewView.as_view(), name='create_review'),
    re_path(r'^services/$', views.ServicesView.as_view(), name='services'),
    re_path(r'^appointments/$', views.AppointmentsView.as_view(), name='appointments'),
    re_path(r'^statistics/$', views.StatisticView.as_view(), name='statistics'),
    re_path(r'^contacts/(?P<pk>\d+)/$', views.DoctorPageView.as_view(), name='doctor_page'),
    re_path(r'^news/(?P<pk>\d+)/$', views.NewsDetailPageView.as_view(), name='news_detail_page'),
    re_path(r'^services/(?P<pk>\d+)/$', views.ServiceDetailPageView.as_view(), name='service_detail_page'),
    re_path(r'^faqs/(?P<pk>\d+)/$', views.FAQDetailPageView.as_view(), name='faq_detail_page'),
    re_path(r'^clients$', views.client_page, name='clients'),
    re_path(r'^api_requests/$', views.api_requests, name='api_requests'),
    re_path(r'^diagram/$', views.clients_age_diagram, name='diagram'),
    re_path(r'^cart/$', views.CartPageView.as_view(), name='cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('transaction/', views.transaction_page, name='transaction_page'),
    path('success/', views.success_page, name='success_page'),
    re_path(r'^appointments/(?P<pk>\d+)/update/$', views.AppointmentUpdateView.as_view(), name='update_appointment'),
    re_path(r'^appointments/(?P<pk>\d+)/delete/$', views.AppointmentDeleteView.as_view(), name='delete_appointment'),
]

