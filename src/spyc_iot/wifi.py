import network

station = network.WLAN(network.STA_IF)

def connect_wifi(ssid, pw):
    if station.isconnected():
        print(f'Already connected on {station.ifconfig()}, skipping')
        return
    
    print('Initializing WLAN')
    station.active(True)
    print('Initialization of WLAN completed')

    print('Connecting WiFi')
    station.connect(ssid, pw)
    while not station.isconnected():
        print('.', end = '')
    print(f'\nWiFi Connected on {station.ifconfig()}')
