from django.shortcuts import render
from django.http import HttpResponse


def show(response):
   print("response",response)
   return  HttpResponse("<h1>This is from show</h1>")