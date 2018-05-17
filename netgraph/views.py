#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import  Bikestatus
from django.http import HttpResponse


import os, sys, csv, json

#import simplejson
import json

#import urllib2
# 0222_ bike crawling
from bs4 import BeautifulSoup
#from urllib2 import urlopen # python 2.7
from urllib.request import urlopen #python 3.6
from django.http import JsonResponse




class MyException(Exception):
    pass
## 0222 bike crawling



def crawl(request):

    url='http://bike.gongju.go.kr/current_state/current_state.aspx'
    web = urlopen(url, timeout=3)
    #except urllib2.URLError, e:
    """
     except urllib.error.HTTPError as e:
        raise MyException("There was an error: %r" % e)

        print(e)

        # null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
    """

    web_page = BeautifulSoup(web, 'html.parser')
    box2 = web_page.find('table', {'id': 'StatusGridView'})

    stations = []
    #table = soup.find('table', attrs={'class':'lineItemsTable'})
    #table_body = table.find('tbody')

    #rows = table_body.find_all('tr')
    rows =box2.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        stations.append([ele for ele in cols if ele]) # Get rid of empty values

    # 0226 add for bikecrawl.html_for Javascript
    bikestatus_js= []
    bikestatus_json =[]
    #0226
    #Bikestatus.objects.all().delete()
    for station in stations:
        #create_bike_db_table(station[1], station[2], station[3], station[4])
        station_available_dock = int(station[3])-int(station[2])

        """
        Bikestatus.objects.update_or_create(station_number=station[0], station_name=station[1],
                                            available_bike=station[2], using_dock=station[4],
                                            available_dock=station_available_dock)
        """

        """
        print ("정거장숫자",station[0])
        print (station[1])
        print (station[2])
        print (station[3])
        print (station[4])
        print (station_available_dock)
        """
        bikestatus_js.append([station[1], station[2], station[3], station[4], str(station_available_dock)])
        # bikestatus_json.append({"station_name":station[1], "available_bike":station[2], "all_dock":station[3], "using_dock" :station[4], "available_dock":str(station_available_dock)})
        # 0401#bikestatus_json.append({"station_number":int(station[0]),"station_name": station[1], "available_bike": int(station[2]), "all_dock": int(station[3]),"available_dock": station_available_dock})
        bikestatus_json.append(
            {"station_number": int(station[0]), "station_name": station[1], "available_bike": int(station[2]),
             "available_dock": station_available_dock})

    bikestatus = Bikestatus.objects.all()
    #print ("BIKE STATUS__:   ",  bikestatus[0].station_name)
    #print ("BIKE STATUS__JS:   ",   bikestatus_js)
    #bikestatus_js2= simplejson.dumps(bikestatus_js, ensure_ascii=False)
    bikestatus_js2= json.dumps(bikestatus_js,ensure_ascii=False)
    #print ("BIKE STATUS__JS__222:   ",   bikestatus_js2)
    ## json type 0326
    bikestatus_json2 = json.dumps(bikestatus_json,ensure_ascii=False)
    #print ("BIKE STATUS__JSON__JSON:   ", bikestatus_json2)

    #return JsonResponse({'status' : 'crawled'})
    #return render(request, 'bikecrawl.html', {'station_name': stations[0][1]})
    # return JsonResponse({bikestatus_json2})#,content_type='application/json; charset=utf-8'})

    #return render(request, 'bikecrawl.html', {'bikestatus': bikestatus,'bikestatus_js': bikestatus_js2}) ## final page
    return HttpResponse(bikestatus_json2, content_type='application/json; charset=utf-8')





def swcrawl(request):

    url='https://www.bikeseoul.com/app/station/moveStationSearchView.do?currentPageNo=7&stationGrpSeq=29'
    web = urlopen(url, timeout=3)
    #except urllib2.URLError, e:
    """
     except urllib.error.HTTPError as e:
        raise MyException("There was an error: %r" % e)

        print(e)

        # null을 반환하거나, break 문을 실행하거나, 기타 다른 방법을 사용
    """

    web_page = BeautifulSoup(web, 'html.parser')
    box2 = web_page.find('table', {'class': 'psboard1'})

    stations = []
    #table = soup.find('table', attrs={'class':'lineItemsTable'})
    #table_body = table.find('tbody')

    #rows = table_body.find_all('tr')
    rows =box2.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        stations.append([ele for ele in cols if ele]) # Get rid of empty values

    # 0226 add for bikecrawl.html_for Javascript
    bikestatus_js= []
    bikestatus_json =[]
    #0226
    #Bikestatus.objects.all().delete()
    for station in stations:
        #create_bike_db_table(station[1], station[2], station[3], station[4])
        station_available_dock = int(station[3])-int(station[2])

        """
        Bikestatus.objects.update_or_create(station_number=station[0], station_name=station[1],
                                            available_bike=station[2], using_dock=station[4],
                                            available_dock=station_available_dock)
        """

        """
        print ("정거장숫자",station[0])
        print (station[1])
        print (station[2])
        print (station[3])
        print (station[4])
        print (station_available_dock)
        """
        bikestatus_js.append([station[1], station[2], station[3], station[4], str(station_available_dock)])
        # bikestatus_json.append({"station_name":station[1], "available_bike":station[2], "all_dock":station[3], "using_dock" :station[4], "available_dock":str(station_available_dock)})
        # 0401#bikestatus_json.append({"station_number":int(station[0]),"station_name": station[1], "available_bike": int(station[2]), "all_dock": int(station[3]),"available_dock": station_available_dock})
        bikestatus_json.append(
            {"station_number": int(station[0]), "station_name": station[1], "available_bike": int(station[2]),
             "available_dock": station_available_dock})

    bikestatus = Bikestatus.objects.all()
    #print ("BIKE STATUS__:   ",  bikestatus[0].station_name)
    #print ("BIKE STATUS__JS:   ",   bikestatus_js)
    #bikestatus_js2= simplejson.dumps(bikestatus_js, ensure_ascii=False)
    bikestatus_js2= json.dumps(bikestatus_js,ensure_ascii=False)
    #print ("BIKE STATUS__JS__222:   ",   bikestatus_js2)
    ## json type 0326
    bikestatus_json2 = json.dumps(bikestatus_json,ensure_ascii=False)
    #print ("BIKE STATUS__JSON__JSON:   ", bikestatus_json2)

    #return JsonResponse({'status' : 'crawled'})
    #return render(request, 'bikecrawl.html', {'station_name': stations[0][1]})
    # return JsonResponse({bikestatus_json2})#,content_type='application/json; charset=utf-8'})

    #return render(request, 'bikecrawl.html', {'bikestatus': bikestatus,'bikestatus_js': bikestatus_js2}) ## final page
    return HttpResponse(bikestatus_json2, content_type='application/json; charset=utf-8')