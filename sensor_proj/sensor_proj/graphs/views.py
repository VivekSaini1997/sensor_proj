# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import json

# Create your views here.

def something(request):
    # parse and get labels from directory
    temp_labels = open_file_and_parse('/home/savi/temp_labels')
    fan_labels = open_file_and_parse('/home/savi/fan_labels')
    context = {
         "temp_labels": temp_labels,
         "fan_labels": fan_labels,
    }
    # return render
    return render(request, "index.html", context)

def open_file_and_parse(directory):
    with open(directory) as f:
        list_file = f.readlines()
    list_file = [x.strip() for x in list_file]
    return list_file

def get_minute_data(request):
    temps = open_file_and_parse('/home/savi/temp_readings')
    fans = open_file_and_parse('/home/savi/fan_readings')
    context = {
        "temps": temps,
  	    "fans": fans,
    }
    return JsonResponse(context)

def get_second_data(request):
    temps = open_file_and_parse('/home/savi/temp_readings_recent')
    fans = open_file_and_parse('/home/savi/fan_readings_recent')
    context = {
        "temps": temps,
  	    "fans": fans,
    }
    return JsonResponse(context)

def something_else(request):
    ip = request.GET.get('ip', None)
    if ip is None or ip == '':
        return render(request, "goto.html")
    else:
        try:
            temp_url = '/home/savi/readings/' + ip + '/temp_labels'
            fan_url = '/home/savi/readings/' + ip + '/fan_labels'
            temp_labels = open_file_and_parse(temp_url)
            fan_labels = open_file_and_parse(fan_url)
        except IOError:
            messages.info(request, "select a valid ip")
            return render(request, "goto.html")
        context = {
             "temp_labels": temp_labels,
             "fan_labels": fan_labels,
             "ip": ip,
        }
        return render(request, "index2.html", context)

def get_alt(request):
    ip = request.GET['ip']
    temp_url = '/home/savi/readings/' + ip + '/temp_readings'
    fan_url = '/home/savi/readings/' + ip + '/fan_readings'
    temps = open_file_and_parse(temp_url)
    fans = open_file_and_parse(fan_url)
    context = {
        "temps": temps,
  	    "fans": fans,
    }
    return JsonResponse(context)

def get_latest_alt(request):
    ip = request.GET['ip']
    temp_url = '/home/savi/readings/' + ip + '/temp_readings_recent'
    fan_url = '/home/savi/readings/' + ip + '/fan_readings_recent'
    temps = open_file_and_parse(temp_url)
    fans = open_file_and_parse(fan_url)
    context = {
        "temps": temps,
  	    "fans": fans,
    }
    return JsonResponse(context)

def get_x_data(request, count):
    ip = request.GET['ip']
    temp_url = '/home/savi/readings/' + ip + '/temp_readings'
    fan_url = '/home/savi/readings/' + ip + '/fan_readings'
    temps = open_file_and_parse(temp_url)
    fans = open_file_and_parse(fan_url)
    context = {
        "temps": temps[len(fans)-int(count):len(temps)],
  	    "fans": fans[len(fans)-int(count):len(fans)],
    }
    return JsonResponse(context)
