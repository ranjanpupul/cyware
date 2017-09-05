from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import GitUser
import json
import urllib
import requests
import ast


# Create your views here.
class ShowResult(APIView):
    def get(self, request):
        try:
            try:
                searchresult={}
                searchresult = requests.get('https://api.github.com/users')
                for val in json.loads(searchresult._content):
                	try:
                	   	p, created = GitUser.objects.get_or_create(login=val['login'],user_id=val['id'],image=val['avatar_url'],followers_url=val['followers_url'],site_admin=val['site_admin'],repos_url=val['repos_url'],updated_by=1)
                	   	p.save()
                	except Exception as e:
                		print e


                return HttpResponse(json.loads(searchresult._content), content_type="application/json")

            except Exception as e:
                print e
                return HttpResponse('nothing...', content_type="application/json")
        except Exception as e:
            return HttpResponse('search Something...', content_type="application/json")