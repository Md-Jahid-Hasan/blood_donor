from django.shortcuts import render, redirect
from .forms import DonorDetailsForm, SearchDonorForm
from .models import DonorDetails, BloodDonationHistory
from users.models import User
from django.db.models import Q
import datetime


def add_donor_details(request):
    if not request.user.is_authenticated:
        return redirect('login')

    donor = DonorDetails.objects.get(user=request.user)
    print(donor)

    initial = {
        'blood_group': donor.blood_group,
        'district': donor.district,
        'permanent_address': donor.permanent_address,
        'present_address': donor.present_address,
        'specific_area': donor.specific_area,
        'phone_number': donor.phone_number,
        'last_date_of_donation': donor.last_date_of_donation,
        'organization': donor.organization,
    }

    if request.POST:
        form = DonorDetailsForm(request.POST)
        if form.is_valid():
            ldd = form.cleaned_data['last_date_of_donation']
            data = form.save(commit=False)

            if (datetime.date.today() - ldd) < datetime.timedelta(days=124):
                data.is_available = False
            data.user = request.user
            print(request.user)
            data.save()
            d = BloodDonationHistory(user=request.user, donor_details=donor, date=ldd)
            d.save()

    else:
        form = DonorDetailsForm(initial=initial)

    context = {
        'form': form,
        'donation_date': donor.last_date_of_donation,
    }
    return render(request, 'donor_details.html', context)


def search_donor(request):

    # request.session['client'] = True
    # if request.POST:
    #     form = SearchDonorForm(request.POST)
    #     if form.is_valid():
    #         blood_group = form.cleaned_data['blood_group']
    #         district = form.cleaned_data['district']
    #         specific_area = form.cleaned_data['specific_area']
    #         specific_area = form.cleaned_data['specific_area']
    #         print(blood_group, district, specific_area)
    #         return redirect('donor_list', blood_group, district, specific_area)
    #
    # else:
    form = SearchDonorForm()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)


def donor_list(request):
    donor_detail = None
    if request.POST:
        form = SearchDonorForm(request.POST)
        if form.is_valid():
            blood_group = form.cleaned_data['blood_group']
            district = form.cleaned_data['district']
            specific_area = form.cleaned_data['specific_area']
            organization = form.cleaned_data['organization']
            print(blood_group, district, specific_area, organization)
            donor_detail = DonorDetails.objects.filter(blood_group=blood_group, is_available=True)
            if district is not "":
                donor_detail = donor_detail.filter(district=district)
            if specific_area is not "":
                donor_detail = donor_detail.filter(specific_area=specific_area)
            if organization is not "":
                donor_detail = donor_detail.filter(organization=organization)

    context = {
        'details': donor_detail
    }

    return render(request, 'donors_list.html', context)


def donor_details(request, pk):
    donor = DonorDetails.objects.get(pk=pk)
    donation_history = BloodDonationHistory.objects.filter(donor_details=donor)

    context = {
        'donor': donor,
        'date': donation_history
    }
    return render(request, 'update_details.html', context)



