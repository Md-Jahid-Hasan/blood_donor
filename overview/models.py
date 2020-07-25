from django.db import models
from django.db.models.signals import post_save
from donors.models import BloodDonationHistory, DonorDetails
import datetime


class Total(models.Model):
    total_user = models.IntegerField(default=0)
    total_op = models.IntegerField(default=0)
    total_on = models.IntegerField(default=0)
    total_ap = models.IntegerField(default=0)
    total_an = models.IntegerField(default=0)
    total_bp = models.IntegerField(default=0)
    total_bn = models.IntegerField(default=0)
    total_abp = models.IntegerField(default=0)
    total_abn = models.IntegerField(default=0)


def update_stat(sender, instance, created, **kwargs):
    if created:
        total = Total.objects.get(pk=1)
        total.total_user = total.total_user + 1


class MonthlyTotalJoin(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    total_user = models.IntegerField(default=0)
    total_op = models.IntegerField(default=0)
    total_on = models.IntegerField(default=0)
    total_ap = models.IntegerField(default=0)
    total_an = models.IntegerField(default=0)
    total_bp = models.IntegerField(default=0)
    total_bn = models.IntegerField(default=0)
    total_abp = models.IntegerField(default=0)
    total_abn = models.IntegerField(default=0)

    def __str__(self):
        return self.month + " " + str(self.year)


def update_monthly_join(sender, instance, created, **kwargs):
    today = datetime.datetime.now()
    month = today.strftime('%B')
    year = today.year
    if created:
        d = len(MonthlyTotalJoin.objects.filter(month=month, year=year))
        if d == 0:
            data = MonthlyTotalJoin(month=month, year=year)
            data.save()
        t = MonthlyTotalJoin.objects.get(month=month, year=year)
        t.total_user = t.total_user + 1
        bg = instance.blood_group
        if bg == "AB-":
            t.total_abn = t.total_abn + 1
        elif bg == "AB+":
            t.total_abp = t.total_abp + 1
        elif bg == "B-":
            t.total_bn = t.total_bn + 1
        elif bg == "B+":
            t.total_bp = t.total_bp + 1
        elif bg == "A-":
            t.total_an = t.total_an + 1
        elif bg == "A+":
            t.total_ap = t.total_ap + 1
        elif bg == "O-":
            t.total_on = t.total_on + 1
        elif bg == "O+":
            t.total_op = t.total_op + 1
        t.save()


post_save.connect(update_monthly_join, sender=DonorDetails)


class MonthlyTotalDonate(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    total_donate = models.IntegerField(default=0)
    total_op_donate = models.IntegerField(default=0)
    total_on_donate = models.IntegerField(default=0)
    total_ap_donate = models.IntegerField(default=0)
    total_an_donate = models.IntegerField(default=0)
    total_bp_donate = models.IntegerField(default=0)
    total_bn_donate = models.IntegerField(default=0)
    total_abp_donate = models.IntegerField(default=0)
    total_abn_donate = models.IntegerField(default=0)

    def __str__(self):
        return self.month + " " + str(self.year)


def update_monthly_report(sender, instance, created, **kwargs):
    today = datetime.datetime.now()
    month = today.strftime('%B')
    year = today.year
    if created:
        d = len(MonthlyTotalDonate.objects.filter(month=month, year=year))
        if d == 0:
            data = MonthlyTotalDonate(month=month, year=year)
            data.save()
        t = MonthlyTotalDonate.objects.get(month=month, year=year)
        t.total_donate = t.total_donate + 1
        bg = instance.donor_details.blood_group
        if bg == "AB-":
            t.total_abn_donate = t.total_abn_donate + 1
        elif bg == "AB+":
            t.total_abp_donate = t.total_abp_donate + 1
        elif bg == "B-":
            t.total_bn_donate = t.total_bn_donate + 1
        elif bg == "B+":
            t.total_bp_donate = t.total_bp_donate + 1
        elif bg == "A-":
            t.total_an_donate = t.total_an_donate + 1
        elif bg == "A+":
            t.total_ap_donate = t.total_ap_donate + 1
        elif bg == "O-":
            t.total_on_donate = t.total_on_donate + 1
        elif bg == "O+":
            t.total_op_donate = t.total_op_donate + 1
        t.save()
        print(instance.donor_details.blood_group)
        print(month, " Current Month", t.total_donate)


post_save.connect(update_monthly_report, sender=BloodDonationHistory)
