from django.contrib import admin
from user_app.models import TwitterUser, Tweet
# Register your models here.
admin.site.register(Tweet)
admin.site.register(TwitterUser)
