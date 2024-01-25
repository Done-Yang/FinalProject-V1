from django.shortcuts import render, redirect
import socket
# from django.contrib import messages
import requests

# Create your views here.
def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def get_ip_info(request):
    search_detial = request.GET.get('search')
    if search_detial != '':
        if request.method == 'GET':
            try:
                response = requests.get(f'http://ip-api.com/json/{search_detial}')
                data = response.json()
                rg_name = data['regionName']
                rg = data['region']
                        
                country = data['country']
                country_code = data["countryCode"]
                city = data["city"]
                latitude = data["lat"]
                longitude = data["lon"]
                time_zone = data['timezone']
                isp = data["isp"]
                ip_address = data["query"]
                org = data['org']

                context = {
                        "search_detial": search_detial,
                        "ip_address":ip_address,
                        "region": rg,
                        "country": country,
                        "country_code": country_code,
                        "city": city,
                        "latitude": latitude,
                        "longitude": longitude,
                        "isp": isp,
                        "org": org, 
                        "time_zone":time_zone,
                        "rg_name":rg_name,
                        }
                return render(request, 'search_result.html', context=context)
            except:
                context = {
                        "search_detial": search_detial,
                        "ip_address":"N/A",
                        "local_host": "N/A",
                        "region": 'N/A',
                        "country": 'N/A',
                        "country_code": 'N/A',
                        "city": 'N/A',
                        "latitude": 'N/A',
                        "longitude": 'N/A',
                        "isp": 'N/A',
                        "org": 'N/A',
                        "rg_name": 'N/A'
                    }
                return render(request, 'search_result.html', context=context)
        else:
            print('method was wrong!')
    else: 
        return render(request, 'index.html')