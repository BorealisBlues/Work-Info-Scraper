## TODO:
## add scraping from url rather than file
## add checks for Medusa AP



## import beautiful soup 4
from bs4 import BeautifulSoup
## import regex
import re

## opens a test html file normally retrieved through a GET request
## and prints its contents
## Scrapes: PowerLevel, SSR, SNR, and Beacons
def SMScrape():
    with open('.\Test_SM.html') as website:
        smsoup = BeautifulSoup(website, 'html.parser')

        ## finds PWR by id
        powerlevel = smsoup.find(id='PowerLevelOFDM').text
        print('pwr level: ', powerlevel)
        powerlevel = int(re.sub(r'[^\d.]+', '', powerlevel))

        ## finds SSR by id
        ssr = smsoup.find(id='signalStrengthRatio').text
        print ('SSR: ', ssr)
        ssr = float(re.sub(r'[^\d.]+', '', ssr))

        ## finds SNR by id
        snr = smsoup.find(id='SignalToNoiseRatioSM').text
        print('SNR: ',snr)

        ## finds beacons by id
        beacons = smsoup.find(id='beaconsPercentReceivedGui').text
        print('Beacons: ',beacons)
        beacons = int(re.sub(r'[^\d.]+', '', beacons))

        return(powerlevel, ssr, snr, beacons)

## opens a test sugar page to pull info from
## Scrapes: Speedplan, 
def SugarScrape():
    with open('.\sugartestpage.html') as sugarpage:
        sugarsoup = BeautifulSoup(sugarpage, 'html.parser')

        ## finds Cx speedplan using tag value
        speedplan = sugarsoup.find(sugar='slot361b').text
        speedplan = int(re.sub(r'[^\d.]+', '', speedplan))
        print ('speedplan is: ',speedplan)
        return (speedplan)

## condition checker for power level
## substitutes using regex all non digits to nothing
def PowerLevelConditionCheck(powerlevel, speedplan):
    if (powerlevel >= 80):
        print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
    elif ((speedplan == 10) or (speedplan == 20)):
        if (powerlevel <= 75):
            print (f'powerlevel of -{powerlevel} in spec for speedplan {speedplan} Mbps')
        else:
            print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
    elif (speedplan == 25):
        if (powerlevel <= 73):
            print (f'powerlevel of -{powerlevel} in spec for speedplan {speedplan} Mbps')
        else:
            print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
    elif ((speedplan == 50) or (speedplan == 100)):
        if (powerlevel <= 64):
            print (f'powerlevel of -{powerlevel} in spec for speedplan {speedplan} Mbps')
        else:
            print (f'powerlevel of -{powerlevel} out of spec for speedplan {speedplan} Mbps')
    else:
        print (f'error determing speedplan: {speedplan} or power level: {powerlevel}')


## ssr condition checker
def SSRConditionCheck(ssr):
    if (ssr <= 3):
        print (f'ssr of {ssr} in spec')
    else:
        print(f'ssr of {ssr} out of spec')

## snr condition checker
def SNRConditionCheck(snr, speedplan):
    if ('/' in snr):
        listsnr = snr.split('/')
        snrv = int(re.sub(r'[^\d.]+', '', listsnr[0]))
        snrh = int(re.sub(r'[^\d.]+', '', listsnr[1]))
        snr = 999
    else:
        snr = int(re.sub(r'[^\d.]+', '', snr))
        snrv = 999
        snrh = 999
        
    if ((snrv <= 15) or (snrh <= 15) or (snr <= 15)):
        print (f'snr of {snrv}V/{snrh}H or {snr} out of spec')
    elif ((speedplan == 10) or (speedplan == 20)):
        if ((snrv >= 17) or (snrh >= 17) or (snr <= 17)):
            print(f'snr of {snrv}V/{snrh}H or {snr} in spec for speedplan {speedplan}Mbps')
        else:
            print(f'snr of {snrv}V/{snrh}H or {snr} out of spec for speedplan {speedplan}Mbps')
    elif (speedplan == 25):
        if ((snrv >= 22) or (snrh >= 22) or (snr <= 22)):
            print(f'snr of {snrv}V/{snrh}H or {snr} in spec for speedplan {speedplan}Mbps')
        else:
            print(f'snr of {snrv}V/{snrh}H or {snr} out of spec for speedplan {speedplan}Mbps')
    elif (speedplan == 50):
        if ((snrv >= 27) or (snrh >= 27) or (snr <= 27)):
            print(f'snr of {snrv}V/{snrh}H or {snr} in spec for speedplan {speedplan}Mbps')
        else:
            print(f'snr of {snrv}V/{snrh}H or {snr} out of spec for speedplan {speedplan}Mbps')
    elif (speedplan == 100):
        if ((snrv >= 30) or (snrh >= 30) or (snr <= 30)):
            print(f'snr of {snrv}V/{snrh}H or {snr} in spec for speedplan {speedplan}Mbps')
        else:
            print(f'snr of {snrv}V/{snrh}H or {snr} out of spec for speedplan {speedplan}Mbps')


## condition checkers for automatic out of spec detection
def BeaconsConditionCheck(beacons):
    if (int(beacons) < 98):
        print(f'Beacons reading of {beacons} out of spec')
    else:
        print(f'Beacons reading of {beacons} in spec')







def main():
    powerlevel, ssr, snr, beacons = SMScrape()
    speedplan = SugarScrape()
    PowerLevelConditionCheck(powerlevel, speedplan)
    SSRConditionCheck(ssr)
    SNRConditionCheck(snr, speedplan)
    BeaconsConditionCheck(beacons)


main()

