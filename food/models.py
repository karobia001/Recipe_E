from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField


# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length= 255, blank =True)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
    
class Profile(models.Model):
    bio = HTMLField()
    photo = ImageField(blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    
    def __str__(self):
        return self.bio
    
class Category(models.Model):
    category = models.CharField(max_length= 255)
    
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def get_category(cls):
        categories = cls.objects.all()
        return categories

    
    
        
class Food(models.Model):
    image_name = models.CharField(max_length=255)
    ingridients = models.TextField()
    recipe = models.TextField()
    picture = ImageField(blank = True, manual_crop = '1080x1080')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    profile_det = models.ForeignKey(Profile, on_delete=models.CASCADE)

    
    @classmethod
    def update_caption(self, caption):
        update_img = cls.objects.filter(id = id).update(caption = caption)
        return update_img

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id = id).all()
        return image

    @classmethod
    def get_profile_pic(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images

    @property
    def count_comments(self):
        comments = self.comments.count()
        return comments

    @property
    def count_likes(self):
        likes = self.likes.count()
        return likes


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']

class Comments(models.Model):
    comment = models.CharField(max_length = 300)
    pub_date = models.DateTimeField(auto_now=True)
    image = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments
    
