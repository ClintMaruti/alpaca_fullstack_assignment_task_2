from django.contrib import admin
from fbGroup.models import Group
from fbGroup.models import User
from fbGroup.models import Comments
from fbGroup.models import Posts

# Register your models here.
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Posts)
