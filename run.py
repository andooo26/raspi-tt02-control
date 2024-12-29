# import 
import cwiid, time
import Adafruit_PCA9685

# pwm関連初期化
pwm = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)
pwm.set_pwm_freq(60)

# wiiリモコンペアリング
print ('Please press buttons 1 + 2 on your Wiimote now ...')
time.sleep(1)
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print ("Cannot connect to your Wiimote. Run again and make sure you are holding buttons 1 + 2!")
  quit()
print ('Wiimote connection established!\n')
time.sleep(1)
wii.rpt_mode = cwiid.RPT_BTN

# pwmセット
button_delay = 0.1
pwm.set_pwm(0, 0, 450)
pwm.set_pwm(1, 0, 400)

while True:
  buttons = wii.state['buttons']

  # Detects whether + and - are held down and if they are it quits the program
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print('\nClosing connection ...')
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_UP):
    print ('Up pressed')
    pwm.set_pwm(1, 0, 350)

  elif (buttons & cwiid.BTN_DOWN):
    print ('Down pressed')
    pwm.set_pwm(1, 0, 450)
    
  elif (buttons & cwiid.BTN_2):
    print ('Button 2 pressed')
    pwm.set_pwm(0, 0, 380)
  else:
    pwm.set_pwm(0, 0, 450)
    pwm.set_pwm(1, 0, 400)

#   if (buttons & cwiid.BTN_1):
#     print ('Button 1 pressed')
#     time.sleep(button_delay)

#   if (buttons & cwiid.BTN_B):
#     print ('Button B pressed')
#     time.sleep(button_delay)

#   if (buttons & cwiid.BTN_HOME):
#     wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
#     check = 0
#     while check == 0:
#       print(wii.state['acc'])
#       time.sleep(0.01)
#       check = (buttons & cwiid.BTN_HOME)
#     time.sleep(button_delay)

#   if (buttons & cwiid.BTN_MINUS):
#     print ('Minus Button pressed')
#     time.sleep(button_delay)

#   if (buttons & cwiid.BTN_PLUS):
#     print ('Plus Button pressed')
#     time.sleep(button_delay)