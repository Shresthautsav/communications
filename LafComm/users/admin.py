from django.contrib import admin
from .models import User,Department,NewsletterSection

admin.site.register(User)
admin.site.register(Department)
admin.site.register(NewsletterSection)