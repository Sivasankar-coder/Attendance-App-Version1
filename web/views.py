import sqlite3
from contextvars import Context

from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template import RequestContext

from .models import Member
import openpyxl
# Create your views here.

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(resumeid=request.POST.get('resumeid'), email=request.POST.get('email')).exists():
            member = Member.objects.get(resumeid=request.POST.get('resumeid'))
            return render(request,'web/Att.html',{'member': member})
    else:
        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

'''def home(request):
    if request.method == 'POST':
        #if Member.objects.filter(resumeid=request.POST['resumeid'], email=request.POST['email']).exists():
        #member = Member.objects.get(resumeid=request.POST['resumeid'], email=request.POST['email'])
        member.Attend = 'Present'
        member.save()
        return render(request, 'web/home.html', {'member': member})
    else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)'''

def enter(request):
    if request.method == 'POST':
        member = Member.objects.get(resumeid=request.POST.get('resumeid'))
        member.Attend = 'Present'
        member.save()
        member = Member.objects.all()
        return render(request, 'web/displays.html', {'member': member})


def report(request):
    if request.method == 'POST':
        '''if Member.objects.filter(resumeid=request.POST['resumeid'], email=request.POST['email']).exists():
            member = Member.objects.get(resumeid=request.POST['resumeid'], email=request.POST['email'], Attend=request.POST['Attend'])
            return render(request, 'web/home.html', {'member': member})'''
        member = Member.objects.get(resumeid='resumeid')
        member.Attend = 'Present'
        member.save()
        return render(request, 'web/home.html', {'member': member})


def enter1(request):
    if request.method == 'POST':
        member = Member.objects.get(resumeid='manoj12')
        member.Attend = 'Present'
        member.save()
        return render(request, 'web/marked.html')

def enter2(request):
    if request.method == 'POST':
        if Member.objects.filter(resumeid=request.POST.get('resumeid'), email=request.POST.get('email')).exists():
            member = Member.objects.get(resumeid='resumeid')
            return render(request, 'web/home.html', {'member': member})

def enter3(request):
    if request.method == 'POST':
        if Member.objects.filter(resumeid=request.POST['resumeid']).exists():
            member = Member.objects.get(resumeid=request.POST.get('resumeid'))
            member.Attend = 'Present'
            member.save()
            return render(request, 'web/home.html', {'member': member})

def displays(request):
    member = Member.objects.all()
    return render(request,'web/displays.html',{member:member})