from django.contrib import admin
from donors import models


admin.site.register(models.DonorDetails)
admin.site.register(models.BloodDonationHistory)
admin.site.register(models.DistrictPlaceInfo)
