from django.contrib import admin
from .models import Total, MonthlyTotalDonate, MonthlyTotalJoin

admin.site.register(Total)
admin.site.register(MonthlyTotalJoin)
admin.site.register(MonthlyTotalDonate)
