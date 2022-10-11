from django.db import models
import os


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    # %Y 2022, %y 22
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 추후 author 작성

    def __str__(self):
        return f'[{self.pk}]{self.title} : {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name) #basename: 파일 이름만 출력하는 함수

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] #주어진 배열에서 가장 마지막 원소 -1
        # a.txt -> a txt
        # b.docx -> b docx
        # c.xlsx -> c xlsx
        # a.b.c.txt -> a b c txt

