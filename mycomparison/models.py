from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserTbl(models.Model):
    UserId = models.IntegerField(primary_key=True)
    UserName = models.CharField(max_length=255)
    UserEmail = models.CharField(max_length=255)
    UserDescription = models.CharField(max_length=1000)
    # UserImage = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.UserName


class ItemTbl(models.Model):
    ItemId = models.IntegerField(primary_key=True)
    ItemName = models.CharField(max_length=255)
    ItemDescription = models.CharField(max_length=255)
    # ItemImage = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.ItemName


class ComparisonTbl(models.Model):
    ComparisonId = models.IntegerField(primary_key=True)
    FirstItemId = models.ForeignKey(ItemTbl,on_delete=models.CASCADE, related_name= 'firstitem')
    SecondItemId = models.ForeignKey(ItemTbl, on_delete=models.CASCADE, related_name='seconditem')
    Vote1 = models.IntegerField(default=0)
    Vote2 = models.IntegerField(default=0)

    def __str__(self):
        return str(self.FirstItemId.ItemName+" "+self.SecondItemId.ItemName)

class CommentTbl(models.Model):
    CommentsId = models.IntegerField(primary_key=True)
    UserId = models.ForeignKey(UserTbl,on_delete=models.CASCADE)
    ComparisonId = models.ForeignKey(ComparisonTbl, on_delete=models.CASCADE)
    Comments = models.CharField(max_length=2000)

# Create your models here.
