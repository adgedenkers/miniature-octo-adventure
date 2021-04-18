import board
import busio
from digitalio import DigitalInOut
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_requests as requests
from adafruit_esp32spi import adafruit_esp32spi

try:
    from secrets import secrets
except ImportError:
#    print("Wifi secrets are kept in the file secrets.py, please keep them there")
    raise

print("Adges SPI Webclient Test")
#print("ESP32 SPI Webclient Test")

TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
JSON_URL = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"

UV_API_URL = "https://api.openuv.io/api/v1/uv?lat=42.40324&lng=-75.56721"
ACCESS_TOK = "x-access-token: f5e00e3a83e1c33528972f2be9725648"

esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

requests.set_socket(socket, esp)

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
#    print("ESP32 found an in idle mode")
#print("firmware vers.", esp.firmware_version)
#print("MAC addr:", [hex(i) for i in esp.MAC_address])

    for ap in esp.scan_networks():
        print("\t%s\t\tRSSI: %d" % (str(ap["ssid"], "utf-8"), ap["rssi"]))

print("Connecting to Access Point...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue

    print("Connected to ", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)
    print("My IP Address is: ", esp.pretty_ip(esp.ip_address))
#    print("IP Lookup Adafruit.com: %s" % esp.pretty_ip(esp.get_host_by_name("adafruit.com")))
    #print("Ping google.com: %d ms" % esp.ping("google.com"))

    #esp._debug = True
#    print("Fetching text from ", TEXT_URL)
    r = requests.get(TEXT_URL)
    print("-" * 40)
    print(r.text)
    print("-" *40)
    r.close()

    print()
    print("Fetching JSON from: ", JSON_URL)
    r = requests.get(JSON_URL)
    print("-" * 40)
    print(r.json())
    print("-" *40)
    r.close()


#    print("DONE!")



# LED Blinking
#led = digitalio.DigitalInOut(board.D13)
#led.direction = digitalio.Direction.OUTPUT

#while True:
#    print("hello, adge!")
#    led.value = True
#    time.sleep(0.1)
#    led.value = False
#    time.sleep(0.1)