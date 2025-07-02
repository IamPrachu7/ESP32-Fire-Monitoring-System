
# ESP32 Fire & Environmental Monitoring System 🔥🌡️

A smart fire and air quality monitoring system using ESP32, MicroPython, MQ2 Gas Sensor, Flame Sensor, and DHT11.

## 🔧 Components Used
- ESP32
- MQ2 Smoke Sensor
- Flame Sensor
- DHT11 Temperature & Humidity Sensor
- 16x2 LCD (I2C)
- Buzzer, Red and Green LEDs
- Breadboard and jumper wires

## 🧠 Features
- Detects smoke, flame, temperature, and humidity
- Alerts with buzzer and LEDs
- Displays real-time data on LCD
- Written in MicroPython, runs on ESP32

## 📁 Project Files
- `main.py`: Core logic to read sensors and trigger alarms
- `lcd_api.py` & `i2c_lcd.py`: LCD helper libraries

## 🛠️ Setup Instructions
1. Flash MicroPython firmware to ESP32
2. Use Thonny IDE or uPyCraft to upload `.py` files
3. Connect sensors and components as per `main.py`
4. Power the ESP32 and observe output on LCD and Serial

## 📷 Screenshot / Diagram
*Add circuit diagram or photo here*

## 📜 License
This project is open-source under the MIT License.
