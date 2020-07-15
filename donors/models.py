from django.db import models
from users.models import User
from django.db.models.signals import post_save


class DonorDetails(models.Model):
    BLOOD_GROUP = [
        ('A+', 'A Positive(A+)'),
        ('A-', 'A Negative(A-)'),
        ('B+', 'B Positive(B+)'),
        ('B-', 'B Negative(B-)'),
        ('AB+', 'AB Positive(AB+)'),
        ('AB-', 'AB Negative(AB-)'),
        ('O+', 'O Positive(O+)'),
        ('O-', 'O Negative(O-)'),
    ]
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=5, null=False, choices=BLOOD_GROUP, blank=True)
    permanent_address = models.CharField(max_length=100, blank=True)
    present_address = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=20, blank=True)
    specific_area = models.CharField(max_length=30, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    last_date_of_donation = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.blood_group + " " + self.district


def create_donor_details(sender, instance, created, **kwargs):
    if created:
        DonorDetails.objects.create(user=instance)
        print("Donor details Created")
    else:
        instance.donordetails.save()
        print('Donor Details updated')


post_save.connect(create_donor_details, sender=User)


class BloodDonationHistory(models.Model):
    date = models.DateField()
    details = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email + " " + str(self.date)


class DistrictPlaceInfo(models.Model):
    district = models.CharField(max_length=20)
    specific_place = models.CharField(max_length=50)



