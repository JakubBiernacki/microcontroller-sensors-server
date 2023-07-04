from display.display import DisplayView


def create_wifi_view(wifi_config):

    wifi_view = DisplayView('WiFi DATA')

    wifi_view.add_row('IP address:')
    print(wifi_config.ip)
    wifi_view.add_row('[%v%]', wifi_config, 'ip')

    return wifi_view
