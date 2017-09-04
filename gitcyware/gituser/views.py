from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse ,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import json
import urllib
import requests
import ast


# Create your views here.
class ShowResult(APIView):
    def get(self, request):
        try:
            try:
                jljljl= []
                searchresult={}
                searchresult = requests.get('https://api.github.com/users')
                for val in searchresult:
                    jljljl.append(val)

                return HttpResponse(jljljl, content_type="application/json")

            except Exception as e:
                print e
                return HttpResponse('nothing...', content_type="application/json")
        except Exception as e:
            return HttpResponse('search Something...', content_type="application/json")