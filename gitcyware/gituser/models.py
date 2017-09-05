from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User

# Create your models here.
class GitUser(models.Model):
	created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
	created_by = models.ForeignKey(User, related_name='%(class)s_created_by',  default=1)
	updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
	updated_by = models.ForeignKey(User, related_name='%(class)s_updated_by', blank=True, null=True,  default=1)
	login = models.CharField(max_length=50, verbose_name='Login Name')
	image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
	user_id = models.IntegerField(verbose_name='Gitid', unique=True)
	followers_url = models.TextField(validators=[URLValidator()])
	site_admin = models.BooleanField(verbose_name='Siteadmin')
	repos_url = models.TextField(validators=[URLValidator()])



