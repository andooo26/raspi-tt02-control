import time
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)
pwm.set_pwm_freq(60)

pwm.set_pwm(0, 0, 450)
pwm.set_pwm(1, 0, 450)
time.sleep(1)
pwm.set_pwm(1, 0, 350)
time.sleep(1)
pwm.set_pwm(1, 0, 400)
time.sleep(1)
pwm.set_pwm(0, 0, 380)
time.sleep(1)
pwm.set_pwm(0, 0, 450)
