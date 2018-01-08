#!/usr/bin/env python

import json
import urllib
import urllib.parse
import urllib.request
import os


def main():
    try:
        with open(os.path.join(
                os.path.expanduser("~"),
                '.config',
                'polybar',
                'city')) as f:
            city = f.readline().strip()
        with open(os.path.join(
                os.path.expanduser("~"),
                '.config',
                'polybar',
                'weather.json')) as f:
            api_key = json.load(f)['api_key']
    except:
        return ''

    try:
        data = urllib.parse.urlencode({'id': city, 'appid': api_key})
        weather = json.loads(urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?' + data)
            .read())
        desc = weather['weather'][0]['description'].capitalize()
        ID = int(float(weather["weather"][0]["id"]))
        temp = int(float(weather['main']['temp']) - 272.15)
        if ID >= 200 and ID <= 232:
            ICON = ""
        elif ID >= 310 and ID <= 531:
            ICON = ""
        elif ID >= 600 and ID <= 622:
            ICON = ""
        elif ID >= 701 and ID <= 761:
            ICON = ""
        elif ID >= 801 and ID <= 804:
            if HOUR >= 6 and HOUR <= 19:
                ICON = ""
            else:
                ICON = ""
        elif ID >= 900 and ID <= 902 or ID >= 957 and ID <= 962:
            ICON = ""
        elif ID == 903 or ID == 906:
            ICON = ""
        elif ID == 904:
            ICON = "" 
        elif ID == 905 or ID >= 951 and ID <= 956:
            ICON = ""
        else:
            if HOUR >= 6 and HOUR <= 19:
                ICON = ""
            else:
                ICON = ""
        return '{} | {} | {}°C'.format(ICON,desc, temp)
    except:
        return 'cant '


if __name__ == "__main__":
    print(main())
