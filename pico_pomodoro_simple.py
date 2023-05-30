from picozero import pico_led
from time import sleep

print('This is going to be ** minutes of pomodoro revision.\nI would suggest active revision such as creating flashcards or doing questions. ')
for i in range(0,3):
    pico_led.on()
    print('** minutes of work')
    sleep(**)#1440
    pico_led.off()
    print('ok you can have an ** minute break')
    sleep(**)#480

pico_led.on()
print('last bit now,use this time to brush up any work then you can take a long break\nOr I would suggest moving onto some less intensive revivion.')
sleep(**)#780
pico_led.off


# 25min=1500secs
#30min=1800secs
#5=300
#7=420