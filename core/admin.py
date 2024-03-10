from django.contrib import admin
from .models import Whishlist, Applied, Interview, Offer, Rejected


# Register your models here.

admin.site.register(Whishlist)
admin.site.register(Applied)
admin.site.register(Interview)
admin.site.register(Offer)
admin.site.register(Rejected)
