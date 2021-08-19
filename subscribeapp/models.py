from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,       # 계정이 사라지면 종속적으로 삭제됨
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    class Meta:
        unique_together = ['user', 'project']   # user가 project 한번이라도 구독했다면 저장을 두번이상 되지 않게 함
