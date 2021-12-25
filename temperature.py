import requests
import url
import sys

#get location for the weather 
def getLocation():
    if len(sys.argv) > 2:
        print("Invalid number of Arguments, (takes only one argument city name)")
        exit(1)
    if len(sys.argv) == 2:
        city=sys.argv[1]
    else:
        city="Chicago"
    return city

def processOutput(json):
    print('\x1b[7;33;40m' + ' City ' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+city +" "+ '\x1b[0m' )
    print('\x1b[7;33;40m' + ' Temp ' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+str(int(json["main"]["temp"] - 273.15))+u"\N{DEGREE SIGN}C"  + '\x1b[0m' )
    print('\x1b[7;33;40m' + ' Feels ' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+str(int(json["main"]["feels_like"] - 273.15))+u"\N{DEGREE SIGN}C"  + '\x1b[0m' )
    print('\x1b[7;33;40m' + ' Min_temp' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+str(int(json["main"]["temp_min"] - 273.15))+u"\N{DEGREE SIGN}C"  + '\x1b[0m' )
    print('\x1b[7;33;40m' + ' Max_temp ' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+str(int(json["main"]["temp_max"] - 273.15))+u"\N{DEGREE SIGN}C"  + '\x1b[0m' )
    print('\x1b[7;33;40m' + ' Pressure ' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+str(json["main"]["pressure"])+"hPa"+ '\x1b[0m' )
    print('\x1b[7;33;40m' + ' Humidity ' + '\x1b[0m' +'\x1b[6;33;47m' + '  ' + '\x1b[0m'+'\x1b[7;36;43m' + " "+str(json["main"]["humidity"])+ '\x1b[0m' )


#MAIN
city=getLocation();
res = requests.get(url.URL(city))
processOutput(res.json())
