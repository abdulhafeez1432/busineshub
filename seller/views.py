from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.forms import PasswordChangeForm
from businesshub.decorators import *
from .forms import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
import random
import string
from decimal import Decimal
from django.http import JsonResponse, HttpResponse
import json
import logging


def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


@login_required
@seller_required
def SellerDashboard(request):
    return render(request, 'seller/dashboard.html')


def SellerProfile(request, pk):
    template_name = 'customer/editprofile.html'
    customer = get_object_or_404(SellerProfile, pk=pk)
    form = SellerProfileForm(request.POST or None,
                             request.FILES or None, instance=customer)
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            messages.success(
                request, "Your Profile Was Updated Successfully...")
            return redirect('customer:dashboard')
    return render(request, template_name, {'form': form})


""" def AddNewBusiness(request):
    template_name = 'seller/addbusiness.html'

    form = AddBusinessForm()
    if request.method == 'POST':
        form = AddBusinessForm(request.POST or None)
        if form.is_valid():

            business = form.save(commit=False)
            user = request.user
            business.user = user
            business.save()
            b = Business.objects.get(pk=business.pk)
            about = AboutBusiness.objects.create(business=b)
            return redirect('seller:about-business', pk=about.id)

    return render(request, template_name, {'form': form}) """


def AddBusinessDocument(request, pk):
    template_name = 'seller/adddocumentbusiness.html'
    document = get_object_or_404(BusinessDocument, pk=pk)
    form = DocumentBusinessForm(
        request.POST or None, request.FILES or None, instance=document)
    if request.method == "POST":
        if form.is_valid():
            document = form.save(commit=False)
            user = request.user
            document.user = user
            document.save()
            # d = BusinessTarget.objects.get(pk=target.pk)
            # document = BusinessDocument.objects.create(business=d)
            return redirect('seller:seller-dashboard')

    return render(request, template_name, {'form': form})


def SellerProfile(request, pk):
    template_name = 'seller/sellerprofile.html'
    seller = get_object_or_404(ProfileCustomer, pk=pk)
    form = SellerProfileForm(
        request.POST or None, request.FILES or None, instance=seller)
    if request.method == 'POST':
        if form.is_valid():
            p = form.save(commit=False)
            p.save()
            messages.success(
                request, "Your Profile Was Updated Successfully...")
            return redirect('seller:dashboard')
    return render(request, template_name, {'form': form})


def ContactUs(request):
    form = ContactForm()
    user = request.user
    b = Business.objects.filter(user=user).first()
    # about = AboutBusiness.objects.create(business=b)
    print(b.id)
    if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            user = request.user

            b = Business.objects.filter(user=user).first()
            # about = AboutBusiness.objects.create(business=b)
            user = b.id
            print(user)
            name = form.cleaned_data['name']
            form.save()
            return JsonResponse({"name": name, "user": user}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "seller/addcontact.html", {"form": form})


def SellBusiness(request):
    form = AddBusinessForm()

    if request.method == "POST" and request.is_ajax():
        form = AddBusinessForm(request.POST or None)
        if form.is_valid():
            business = form.save(commit=False)
            user = request.user
            business.user = user
            business.save()
            b = Business.objects.get(pk=business.pk)
            about = AboutBusiness.objects.create(business=b)

            return JsonResponse({"about": about.id}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, "seller/sellbusiness.html", {"form": form})


@seller_required
@login_required
def AddAboutBusiness(request, pk):
    template_name = 'seller/addaboutbusiness.html'
    about = get_object_or_404(AboutBusiness, pk=pk)
    form = AboutBusinessForm(
        request.POST or None, instance=about)

    if request.method == "POST" and request.is_ajax():
        if form.is_valid():
            business = form.save()

            b = Business.objects.get(pk=business.business)
            print(b.id)
            staff, created = BusinesStaff.objects.get_or_create(business=b)
            if created:
                return JsonResponse({"about": b.id}, status=200)

            else:
                return JsonResponse({"about": b.id}, status=200)

        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, template_name, {'form': form, 'about': about})


@seller_required
@login_required
def AddStaffBusiness(request, pk):
    template_name = 'seller/addstaffbusiness.html'
    staff = get_object_or_404(BusinesStaff, pk=pk)

    # print(b.id)
    form = StaffBusinessForm(
        request.POST or None, instance=staff)

    if request.method == "POST" and request.is_ajax():
        if form.is_valid():
            staff = form.save()
            b = Business.objects.get(pk=staff.business.pk)

            financial, created = BusinessFinancial.objects.get_or_create(
                business=b)
            if created:
                return JsonResponse({"about": b.id}, status=200)

            else:
                return JsonResponse({"about": b.id}, status=200)

        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, template_name, {'form': form, 'staff': staff})


@seller_required
@login_required
def AddFinancialBusiness(request, pk):
    template_name = 'seller/addfinancialbusiness.html'
    financial = get_object_or_404(BusinessFinancial, pk=pk)

    form = FinancialBusinessForm(
        request.POST or None, request.FILES or None, instance=financial)

    if request.method == "POST" and request.is_ajax():
        if form.is_valid():
            financial = form.save()
            b = Business.objects.get(pk=financial.business.pk)

            target, created = BusinessTarget.objects.get_or_create(
                business=b)
            if created:
                return JsonResponse({"about": b.id}, status=200)

            else:
                return JsonResponse({"about": b.id}, status=200)

        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, template_name, {'form': form, 'financial': financial})


@seller_required
@login_required
def AddTargetBusiness(request, pk):
    template_name = 'seller/addtargetbusiness.html'
    target = get_object_or_404(BusinessTarget, pk=pk)
    form = TargetBusinessForm(
        request.POST or None, request.FILES or None, instance=target)
    if request.method == "POST" and request.is_ajax():

        if form.is_valid():
            target = form.save()
            b = Business.objects.get(pk=target.business.pk)

            target, created = BusinessDocument.objects.get_or_create(
                business=b)
            print(b.id)
            if created:
                return JsonResponse({"about": b.id}, status=200)

            else:
                return JsonResponse({"about": b.id}, status=200)

        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)

    return render(request, template_name, {'form': form, 'target': target})
