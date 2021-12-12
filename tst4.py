#必要なモジュールをインポート
import RPi.GPIO as GPIO             #GPIO用のモジュールをインポート
import time                         #時間制御用のモジュールをインポート
import sys                          #sysモジュールをインポート
import random

#ポート番号の定義
Led_pin = 12                        #変数"Led_pin"に12を代入

#GPIOの設定
GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
GPIO.setup(Led_pin, GPIO.OUT)       #GPIO12を出力モードに設定

#PWMの設定
Led = GPIO.PWM(Led_pin, 50)         #GPIO.PWM(ポート番号, 周波数[Hz])

#初期化処理
Led.start(0)                        #PWM信号0%出力
bright = 0                          #変数"bright"に0を代入
x = 0

#while文で無限ループ
#LEDの明るさをデューティ比で制御
#Led.ChangeDutyCycle(デューティ比)
while True:
    try:
        Led.ChangeDutyCycle(bright)    #PWM信号出力(デューティ比は変数"bright")
        time.sleep(0.07)               #0.05秒間待つ
        x = random.random()
        bright = 100*x                  
        
            
    except KeyboardInterrupt:          #Ctrl+Cキーが押された
        Led.stop()                     #LED点灯をストップ
        GPIO.cleanup()                 #GPIOをクリーンアップ
        sys.exit()                     #プログラムを終了