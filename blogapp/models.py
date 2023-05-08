from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Users(models.Model):
    username = models.CharField(max_length=64,verbose_name="사용자이름")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    useremail = models.EmailField(max_length=128, verbose_name="이메일")
    registered_dttm = models.DateField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name ="사용자"
        verbose_name_plural = "사용자"