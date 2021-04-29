from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth, messages
from .forms import *
from .models import *
from django.contrib.auth import logout as django_logout
from difflib import SequenceMatcher
import datetime
from django.contrib.auth.decorators import login_required
import operator
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)
from django.db.models import Count
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.utils.decorators import method_decorator
from businesshub.decorators import *
from django.contrib.auth import authenticate, login as dj_login


def home(request):
    return render(request, 'general/index.html')


class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Seller'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        #p = SellerProfile.objects.get(user=self.request.user.id)
        #return redirect('customer:customer_profile', p.id)
        return redirect('seller:seller-dashboard')

class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        p = SellerProfile.objects.get(user=self.request.user.id)
        return redirect('seller:seller-dashboard')


def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if form.is_valid():
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                #dj_login(request, user)
                dj_login(request, user)

                if request.user.is_seller:
                    return redirect('seller:seller-dashboard')
                elif request.user.is_buyer:
                    return redirect('buyer:buyer-dashbooard')

        else:
            args = {'form': form}
            return render(request, 'registration/login.html', args)

    else:
        form = AuthenticationForm

    args = {'form': form}
    return render(request, 'registration/login.html', args)


def logout_user(request):
    django_logout(request)
    return redirect('account:user-login')
