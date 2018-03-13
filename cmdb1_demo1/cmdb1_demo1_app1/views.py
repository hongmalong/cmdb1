#coding:utf8
from django.shortcuts import render,HttpResponseRedirect,render_to_response
from django.http import HttpResponse
import time

# Create your views here.
def HelloWorld ( request ) :
    return HttpResponse ( 'hello world!' )





