from django.contrib import admin

from store.models import Tag,Project,OrderSummary
# Register your models here.

admin.site.register(Tag)

admin.site.register(Project)

admin.site.register(OrderSummary)