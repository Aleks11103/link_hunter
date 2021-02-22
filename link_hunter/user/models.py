import os
import traceback
from PIL import Image 
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import pre_delete, post_save
from django.dispatch.dispatcher import receiver


class DelQuarySet(models.query.QuerySet):
    def delete(self):
        for el in self:
            el.delete()


class DelManager(BaseUserManager):
    pass


class User(AbstractUser):
    def path_upload(self, filename):
        type_file = '.' + filename.split('.')[-1]
        return os.path.join(
            'users',
            'avatars',
            self.username + type_file,
        )
    
    phone = models.CharField(
        null=True,
        max_length=20,
        verbose_name='User phone number.'
    )
    sex = models.CharField(
        null=True,
        max_length=1,
        verbose_name='Sex.'
    )
    avatar = models.ImageField(
        upload_to=path_upload,
        null=True,
        verbose_name='Avatar',
    )
    
    def __str__(self):
        return self.username

    objects = DelManager()


@receiver(pre_delete, sender=User)
def user_delete(sender, instance, **kwargs):
    instance.avatar.delete(False)


@receiver(post_save, sender=User)
def user_delete(sender, instance, **kwargs):
    img_path = os.path.join(settings.MEDIA_ROOT, instance.avatar.path)
    image = Image.open(img_path).convert('LA')
    # image.show()


    # def delete(self):
    #     try:
    #         os.unlink(os.path.abspath(self.avatar.path))
    #     except Exception as error:
    #         traceback.print_exc()
    #     return super().delete()