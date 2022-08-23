import unittest

from django.shortcuts import render, redirect

from validation2app.forms import linkform
from validation2app.models import link
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import http.client as httplib

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def index(request):
    context = {}
    form = linkform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context['form'] = form
    return render(request, 'index.html', context)

# def index(request):
    # append_str ="https://"
    # records = link.objects.all()
    # list_rec =[records]
    # list=[]
    #
    # for i in list_rec:
    #     if "https" in i:
    #         req = Request(i)
    #         try:
    #             response = urlopen(req)
    #         except HTTPError as e:
    #             list.append("fail")
    #         except URLError as e:
    #             list.append("fail")
    #         else:
    #             list.append("success")
    #     # else:
    #     #     conn = httplib.HTTPConnection(i)
    #     #     conn.request("HEAD", "/")
    #     #     r1 = conn.getresponse()
    #     #     print(i)
    #     #     print(r1.status, r1.reason)
    #     #
    #     #     if r1.status == 200:
    #     #         print("success")
    #     #     else:
    #     #         print("fail")
    # return render(request, 'index.html', {'records': records, 'list': list})


