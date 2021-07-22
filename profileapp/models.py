from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')        # 1계정당 1프로필 매칭

    image = models.ImageField(upload_to='profile/', null=True) # 꼭 넣을 필요는 없는 이미지

    nickname = models.CharField(max_length=30, unique=True)    # 고유한 닉네임

    message = models.CharField(max_length=200, null=True)      # 꼭 적을 필요는 없는 상태 메시지
