def on_forever():
    radio.set_group(150)
basic.forever(on_forever)

def on_forever2():
    radio.send_number(1)
basic.forever(on_forever2)
