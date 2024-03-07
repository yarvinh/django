from django.shortcuts import render
from django.http import HttpResponse



def index(response):
    return  HttpResponse("<h1>tech with tim</h1>")

def test(response):
    return  HttpResponse("<h1>This is from test</h1>")


