from django.contrib import admin
from .models import UserTbl, ItemTbl, ComparisonTbl, CommentTbl

# Register your models here.
admin.site.register(UserTbl)
admin.site.register(ItemTbl)
admin.site.register(CommentTbl)
admin.site.register(ComparisonTbl)