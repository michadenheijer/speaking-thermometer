import time
import math
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

ohm25 = 470
beta = 2000

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


def get_temp():
    input = mcp.read_adc(0)
    volt = input*(3.3/1024.0)
    ohm= (3.3-volt)*(2200/volt)
    temp= (1.0/((math.log(ohm/ohm25)/beta)+(1/298.15)))-273.15
    return temp

#####################################################################
# Main program loop.                                                #
#while True:                                                        #
#    input = mcp.read_adc(0)                                        #
#    volt = input*(3.3/1024.0)                                      #
#    ohm= (3.3-volt)*(2200/volt)                                    #
#    temp= (1.0/((math.log(ohm/ohm25)/beta)+(1/298.15)))-273.15     #
#    print (str(volt) + "volt, " + str(ohm) + "ohm")                #
#    print (str(temp) + "C")                                        #
#    time.sleep(0.5)                                                #
#####################################################################
