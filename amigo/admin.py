from django.contrib import admin
from amigo.models import UserProfile, Status, Friends
# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    readonly_fields = ('pubDate',)
    list_display = ('user', 'subject', 'body', 'like', 'disLike')

class FriendsAdmin(admin.ModelAdmin):
    readonly_fields = ('timeStamp',)
    list_display = ('user1', 'user2', 'active')

admin.site.register(UserProfile)
admin.site.register(Status, StatusAdmin)
admin.site.register(Friends, FriendsAdmin)