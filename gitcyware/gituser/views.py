from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from models import GitUser
from django.db.models import Q
import json
import urllib
import requests
import ast


# Create your views here.
class ShowResult(APIView):
    def get(self, request):
        try:
            searchresult={}
            searchresult = requests.get('https://api.github.com/users?since=573')
            for val in json.loads(searchresult._content):
                try:
                    p, created = GitUser.objects.update_or_create(login=val['login'],user_id=val['id'],image=val['avatar_url'],followers_url=val['followers_url'],site_admin=val['site_admin'],repos_url=val['repos_url'])
                    p.save()
                except Exception as e:
                    print e
            return HttpResponse(json.loads(searchresult._content), content_type="application/json")
        except Exception as e:
            print e
            return HttpResponse('nothing...', content_type="application/json")


class SearchQuery(APIView):
    def get(self, request):
        try:
            name = request.GET['name'] if request.GET['name'] != 'None' else None
            if name:
                search = GitUser.objects.filter(Q(login__icontains=name) | Q(user_id__icontains=name)).values('login', 'image', 'user_id')
                if not search:
                    return HttpResponse('No result found... ', content_type="application/json")
                return HttpResponse(json.dumps(list(search)),content_type="application/json")
            else:
                search = GitUser.objects.values('login', 'image', 'user_id')
                return HttpResponse(json.dumps(list(search)), content_type="application/json")
        except Exception as e:
            return HttpResponse('Search Something...', content_type="application/json")