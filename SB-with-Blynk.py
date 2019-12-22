import blynklib

BLYNK_AUTH = 'txbM-LjJOrPMp3Beh-Ts1RBYGFMJ3Ahp'

blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    if value == [u'1']:
        print("Blind Opened")
    else:
        print("Blinds Closed")


while True:
    blynk.run()