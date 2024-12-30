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
  
  # 傾き
  wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
  check = 0
  steering = -2 * (wii.state['acc'])[1] + 650
  print(steering)
  pwm.set_pwm(1, 0, steering)
  time.sleep(0.1)
  check = (buttons & cwiid.BTN_HOME)
  
  # 前進
  if (buttons & cwiid.BTN_2):
    print ('Button 2 pressed')
    pwm.set_pwm(0, 0, 380)
    # 傾き
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    check = 0
    steering = -2 * (wii.state['acc'])[1] + 650
    print(steering)
    pwm.set_pwm(1, 0, steering)
    time.sleep(0.01)
    check = (buttons & cwiid.BTN_HOME)
  
  # 停止, スロットル初期化
  else:
    pwm.set_pwm(0, 0, 450)
    pwm.set_pwm(1, 0, 400)