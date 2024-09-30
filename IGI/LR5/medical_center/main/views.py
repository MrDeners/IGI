import json
from datetime import datetime

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.sites import requests
from django.db.models import Avg, Q
from django.forms import ModelForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, TemplateView, FormView, DetailView, UpdateView, DeleteView, ListView
import plotly.graph_objs as go

from .forms import SignUpForm, SignInForm, ReviewForm
from .models import News, Doctor, About, Faq, TermCondition, Vacancy, Review, Code, ServiceSet, Service, \
    CustomUser, Department, ClientCard, Appointment, ShopCart, Partner, History, Prop
from django.db import models
import requests


# Create your views here.

def index(request):
    news = News.objects.latest('created_at')
    services = ServiceSet.objects.all()
    partners = Partner.objects.all()
    return render(request,
                  'main/main_page.html', {'news': news, 'services': services, 'partners': partners})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'main/signup.html'


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'main/signin.html'

    def get_success_url(self):
        return reverse_lazy('home')


class AboutView(TemplateView):
    template_name = 'main/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        about = About.objects.first()
        history = History.objects.all()
        props = Prop.objects.all()
        context['about'] = about
        context['history'] = history
        context['props'] = props
        return context


class NewsView(TemplateView):
    template_name = 'main/news_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.all()
        context['news'] = news
        return context


class FAQView(TemplateView):
    template_name = 'main/faq_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        faqs = Faq.objects.all()
        context['faqs'] = faqs
        return context


class ContactsView(TemplateView):
    template_name = 'main/contacts_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = Doctor.objects.all()
        context['contacts'] = contacts
        return context


class TermConditionView(TemplateView):
    template_name = 'main/term_condition_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        term_condition = TermCondition.objects.first()
        context['term_condition'] = term_condition
        return context


class VacancyView(TemplateView):
    template_name = 'main/vacancies_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancies = Vacancy.objects.all()
        context['vacancies'] = vacancies
        return context


class ReviewsView(TemplateView):
    template_name = 'main/reviews_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context['reviews'] = reviews
        return context


class CreateReviewView(FormView):
    form_class = ReviewForm
    template_name = 'main/create_review.html'

    def form_valid(self, form):
        form.save()
        return redirect('reviews')


class CodesAndCouponsView(TemplateView):
    template_name = 'main/codes_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        codes = Code.objects.all()
        context['codes'] = codes
        return context


class ServicesView(TemplateView):
    template_name = 'main/services_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = ServiceSet.objects.all()
        context['services'] = services
        return context

    def post(self, request, *args, **kwargs):
        selected_services = request.POST.getlist('services')
        appointment = Appointment()
        appointment.customer = request.user.clientCard
        appointment.save()
        appointment.services.set(selected_services)
        return redirect('services')


class AppointmentUpdateView(UpdateView):
    template_name = 'main/update_appointment.html'
    model = Appointment
    fields = ['services']
    success_url = reverse_lazy('appointments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = ServiceSet.objects.all()
        context['services'] = services
        return context

    def form_valid(self, form):
        appointment = form.save(commit=False)
        appointment.customer = self.request.user.clientCard
        appointment.save()
        return super().form_valid(form)


class AppointmentDeleteView(DeleteView):
    template_name = 'main/confirm.html'
    model = Appointment
    success_url = reverse_lazy('appointments')


class AppointmentsView(TemplateView):
    template_name = 'main/appointments_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_card = self.request.user.clientCard
        appointments = client_card.appointments.all() if client_card else None
        context['appointments'] = appointments
        context['now_utc'] = timezone.now()
        context['user_timezone'] = self.request.user.timezone
        return context


def create_appointment(request):
    if request.method == 'POST':
        selected_services = request.POST.getlist('services')
        appointment = Appointment(time=datetime.now())
        appointment.services.set(selected_services)
        appointment.save()
        return redirect('services')
    else:
        services = Service.objects.all()
        context = {'services': services}
        return render(request, 'create_appointment.html', context)


def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'PUT':
        selected_services = request.POST.getlist('services')
        appointment.services.set(selected_services)
        appointment.save()
        return redirect('services')
    else:
        services = Service.objects.all()
        context = {'appointment': appointment, 'services': services}
        return render(request, 'update_appointment.html', context)


def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'DELETE':
        appointment.delete()
        return redirect('services')
    else:
        return render(request, 'delete_appointment.html', {'appointment': appointment})


def clients_age_diagram(request):
    age_groups = [
        (19, 35),
        (36, 60),
        (61, 100)
    ]

    clients = CustomUser.objects.filter(clientCard__isnull=False)

    clients_in_group = [clients.filter(age__range=(18, 35)).count(), clients.filter(age__range=(36, 60)).count(),
                        clients.filter(age__range=(61, 100)).count()]
    # for lower_bound, upper_bound in age_groups:
    #     count = CustomUser.objects.filter(Q(clientCard__isnull=False), age__range=(lower_bound, upper_bound)).count()
    #     clients_in_group.append(count)

    labels = ['Tanagers(19-35)', 'Adults(36-60)', 'Elders(61-100)']
    values = clients_in_group

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(title='Clients Age Distribution')

    chart = fig.to_html(full_html=False)
    return HttpResponse(chart)


class StatisticView(TemplateView):
    template_name = 'main/statistic_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.count()
        context['clientsAmount'] = CustomUser.objects.filter(role='client').count()
        context['clients'] = CustomUser.objects.filter(role='client').all()
        context['doctorsAmount'] = CustomUser.objects.filter(role='doctor').count()
        context['doctors'] = CustomUser.objects.filter(role='doctor').all()
        context['planned_profit'] = '12500'
        context['clientsMiddleAge'] = CustomUser.objects.filter(role='client').aggregate(avg_age=Avg('age'))['avg_age']
        context['doctorsMiddleAge'] = CustomUser.objects.filter(role='doctor').aggregate(avg_age=Avg('age'))['avg_age']
        context['departmentAmount'] = Department.objects.count()

        return context


class DoctorPageView(DetailView):
    model = Doctor
    template_name = 'main/doctor_page.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class NewsDetailPageView(DetailView):
    model = News
    template_name = 'main/news_detail_page.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ServiceDetailPageView(DetailView):
    model = Service
    template_name = 'main/service_detail_page.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class FAQDetailPageView(DetailView):
    model = Faq
    template_name = 'main/faq_detail_page.html'
    context_object_name = 'faq'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class CartPageView(ListView):
    model = ShopCart
    template_name = 'main/cart_page.html'
    context_object_name = 'items'

    def get_queryset(self):
        print(self.request.user.clientCard)
        return ShopCart.objects.filter(customer=self.request.user.clientCard)


@require_POST
def update_cart(request):
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')

    shop_cart_item = get_object_or_404(ShopCart, id=item_id, customer=request.user.clientCard)

    if action == 'increase':
        shop_cart_item.amount += 1
    elif action == 'decrease':
        if shop_cart_item.amount > 1:
            shop_cart_item.amount -= 1
        else:
            shop_cart_item.delete()
            return redirect('cart')
    elif action == 'delete':
        shop_cart_item.delete()
        return redirect('cart')

    shop_cart_item.save()

    return redirect('cart')


@login_required
def transaction_page(request):
    cart_items = ShopCart.objects.filter(customer=request.user.clientCard)

    total_amount = 0
    for item in cart_items:
        try:
            price = float(item.service.price)
        except ValueError:
            price = 0

        total_amount += price * item.amount

    if request.method == 'POST':
        if 'success' in request.POST:
            cart_items.delete()
            return redirect('success_page')

    return render(request, 'main/transaction_page.html', {'total_amount': total_amount})


def success_page(request):
    return render(request, 'main/success_page.html')


@login_required
def client_page(request):
    doctor = request.user.doctorCard
    return render(request, 'main/clients_page.html', {'doctor': doctor})


def api_requests(request):
    cat_fact_response = requests.get("https://catfact.ninja/fact")
    dog_response = requests.get("https://dog.ceo/api/breeds/image/random")

    if cat_fact_response.status_code == 200 and dog_response.status_code == 200:
        cat_fact = cat_fact_response.json()["fact"]
        dog_image = dog_response.json()["message"]
        return render(request, "main/api_page.html", {"cat_fact": cat_fact, "dog_image": dog_image})
    else:
        return HttpResponse("Error API", status=500)
