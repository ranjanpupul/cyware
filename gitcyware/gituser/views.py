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
        # import ipdb; ipdb.set_trace()
        searchresult = []
        try:
            try:
                searchresult = requests.get('https://api.github.com/users')
                print searchresult
                for val in searchresult:
                    print type((val))

            except Exception as e:
                print e


            if name:
                searchvalue = EmployeeDetails.objects.filter(employeeRole__icontains=name).values('company__companyName', 'jobDetail__roleName', 'employeeName')
                if searchvalue:
                    serachresult = list(searchvalue)
                    serachresult = json.dumps(serachresult)
                    return HttpResponse(serachresult, content_type="application/json")
                else:
                    return HttpResponse('NO result Matching Your Query...', content_type="application/json")
            else:
                return HttpResponse('NO Result Found...', content_type="application/json")
        except Exception as e:
            return HttpResponse('search Something...', content_type="application/json")