from machine import Pin, ADC, I2C
import time
import dht
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# --- Pin Definitions ---
FLAME_SENSOR_PIN = 32
MQ2_SENSOR_PIN = 33
BUZZER_PIN = 13
RED_LED_PIN = 12
GREEN_LED_PIN = 14
DHT_PIN = 27

# --- Thresholds ---
flame_threshold = 300
smoke_threshold = 400

# --- Initialize Components ---
dht_sensor = dht.DHT11(Pin(DHT_PIN))

flame_sensor = ADC(Pin(FLAME_SENSOR_PIN))
flame_sensor.atten(ADC.ATTN_11DB)

mq2_sensor = ADC(Pin(MQ2_SENSOR_PIN))
mq2_sensor.atten(ADC.ATTN_11DB)

buzzer = Pin(BUZZER_PIN, Pin.OUT)
red_led = Pin(RED_LED_PIN, Pin.OUT)
green_led = Pin(GREEN_LED_PIN, Pin.OUT)

# --- I2C LCD Setup ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

lcd.putstr("Smart Fire & Env\nMonitoring Sys")
time.sleep(2)
lcd.clear()

while True:
    try:
        flame_value = flame_sensor.read()
        smoke_value = mq2_sensor.read()
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        fire_detected = flame_value < flame_threshold
        smoke_detected = smoke_value > smoke_threshold

        print("Flame:", flame_value, "| Smoke:", smoke_value,
              "| Temp:", temperature, "C | Humidity:", humidity, "%")

        lcd.move_to(0, 0)
        lcd.putstr("T:{:.1f} H:{}%    ".format(temperature, int(humidity)))

        lcd.move_to(0, 1)
        if fire_detected:
            lcd.putstr("FIRE ALERT!     ")
        elif smoke_detected:
            lcd.putstr("SMOKE DETECTED! ")
        else:
            lcd.putstr("All Normal      ")

        if fire_detected or smoke_detected:
            buzzer.on()
            red_led.on()
            green_led.off()
        else:
            buzzer.off()
            red_led.off()
            green_led.on()

    except Exception as e:
        print("Error:", e)

    time.sleep(2)
