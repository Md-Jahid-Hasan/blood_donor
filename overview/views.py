from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from users.models import User
from donors.models import DonorDetails
from .models import MonthlyTotalDonate, MonthlyTotalJoin
import datetime


def get_data(request):
    list_month = []
    blood_group = []
    label = []

    today = datetime.datetime.now()
    current_month = today.strftime('%B')
    current_year = today.year

    if request.method == 'POST':
        year = request.POST.get('donate_year')
        month = request.POST.get('donate_month')

        if year is not None:
            query_month = MonthlyTotalDonate.objects.filter(year=year)
            for m in query_month:
                list_month.append(m.month)

        if month is not None:
            x = MonthlyTotalDonate.objects.get(month=month, year=year)

            blood_group = [x.total_ap_donate, x.total_an_donate, x.total_bp_donate, x.total_bn_donate,
                           x.total_op_donate, x.total_on_donate, x.total_abp_donate, x.total_abn_donate]
            label = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
        d = {
            'month': list_month,
            'blood_group': blood_group,
            'label': label
        }
        return JsonResponse(d)

    total_user = len(User.objects.all())
    this_month = MonthlyTotalDonate.objects.get(month=current_month, year=current_year)
    total_op = len(DonorDetails.objects.filter(blood_group='O+'))
    total_on = len(DonorDetails.objects.filter(blood_group='O-'))
    total_ap = len(DonorDetails.objects.filter(blood_group='A+'))
    total_an = len(DonorDetails.objects.filter(blood_group='A-'))
    total_bp = len(DonorDetails.objects.filter(blood_group='B+'))
    total_bn = len(DonorDetails.objects.filter(blood_group='B-'))
    total_abp = len(DonorDetails.objects.filter(blood_group='AB+'))
    total_abn = len(DonorDetails.objects.filter(blood_group='AB-'))
    blood_group = [total_ap, total_an, total_bp, total_bn, total_op, total_on, total_abp, total_abn]
    label = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    this_month_data = [this_month.total_ap_donate, this_month.total_an_donate, this_month.total_bp_donate,
                       this_month.total_bn_donate, this_month.total_op_donate, this_month.total_on_donate,
                       this_month.total_abp_donate, this_month.total_abn_donate]

    data = {
        'label': label,
        'blood_group': blood_group,
        'monthly_data': this_month_data,

    }
    return JsonResponse(data)


def get_chart(request):
    today = datetime.datetime.now()
    month = today.strftime('%B')
    year = today.year

    donate_year = MonthlyTotalDonate.objects.all().order_by('-year').values_list('year', flat=True).distinct('year')
    join_year = MonthlyTotalJoin.objects.all().order_by('-year').values_list('year', flat=True).distinct('year')
    donate_month = MonthlyTotalDonate.objects.filter(year=year)
    join_month = MonthlyTotalJoin.objects.filter(year=year)

    context = {
        'donate_year': donate_year,
        'join_year': join_year,
        'donate_month': donate_month,
        'join_month': join_month,

    }
    return render(request, 'statistic.html', context)



