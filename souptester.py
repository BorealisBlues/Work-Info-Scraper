## TODO:
## add scraping from url rather than file
## add checks for Medusa AP



## import beautiful soup 4
from bs4 import BeautifulSoup
## import regex
import re

## opens a test html file normally retrieved through a GET request
## and prints its contents
with open('.\Test_SM.html') as website:
    smsoup = BeautifulSoup(website, 'html.parser').text

    ## finds PWR by id
    powerlevel = smsoup.find(id='PowerLevelOFDM').text
    print('pwr level: ', powerlevel)

    ## finds SSR by id
    ssr = smsoup.find(id='signalStrengthRatio').text
    print ('SSR: ', ssr)

    ## finds SNR by id
    snr = smsoup.find(id='SignalToNoiseRatioSM').text
    print('SNR: ',snr)

    ## finds beacons by id
    beacons = smsoup.find(id='beaconsPercentReceivedGui').text
    print('Beacons: ',beacons)

## opens a test sugar page to pull info from
with open('.\sugartestpage.html') as sugarpage:
    sugarsoup = BeautifulSoup(sugarpage, 'html.parser')

    ## finds Cx speedplan using tag value
    speedplan = sugarsoup.find(sugar='slot361b').text
    speedplan = int(re.sub(r'[^\d.]+', '', powerlevel))

## condition checkers for automatic out of spec detection
if (int(beacons) < 98):
    print('Beacons out of spec')

## condition checker for power level
## substitutes using regex all non digits to nothing
powerlevel = int(re.sub(r'[^\d.]+', '', powerlevel))
if (powerlevel >= 80):
    print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
elif ((speedplan == 10) or (speedplan == 20)):
    if (powelevel <= 75):
        print (f'powerlevel of -{powerlevel} in spec for speedplan {speedplan} Mbps')
    else:
        print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
elif (speedplan == 25):
    if (powelevel <= 73):
        print (f'powerlevel of -{powerlevel} in spec for speedplan {speedplan} Mbps')
    else:
        print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
elif ((speedplan == 50) or (speedplan == 100)):
    if (powelevel <= 64):
        print (f'powerlevel of -{powerlevel} in spec for speedplan {speedplan} Mbps')
    else:
        print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
else:
    print (f'error determing speedplan: {speedplan} or power level: {powerlevel}')

## ssr condition checker
ssr = float(re.sub(r'[^\d.]+', '', ssr))
if (ssr <= 3):
    print (f'ssr of {ssr} in spec')
else:
    print(f'ssr of {ssr} out of spec')

## snr condition checker
if ('/' in snr):
    listsnr = snr.split('/')
    snrv = int(re.sub(r'[^\d.]+', '', listsnr[0]))
    snrh = int(re.sub(r'[^\d.]+', '', listsnr[1]))
    if ((snrv >= 15) or (snrh >= 15)):
        print ('snr in spec')
    else:
        print ('snr out of spec')
else:
    snr = int(re.sub(r'[^\d.]+', '', snr))
