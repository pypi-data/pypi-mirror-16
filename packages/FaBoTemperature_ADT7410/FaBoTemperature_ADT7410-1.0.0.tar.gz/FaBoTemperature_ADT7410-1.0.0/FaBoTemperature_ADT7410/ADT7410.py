# coding: utf-8
## @package FaBoTemperature_ADT7410
#  This is a library for the FaBo Temperature I2C Brick.
#
#  http://fabo.io/207.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import smbus
import time

# ADT7410 Default I2C Slave Address
SLAVE_ADDRESS     = 0x48

## Register Addresses
TEMP_MSB_REG      = 0x00
TEMP_LSB_REG      = 0x01
STATUS_REG        = 0x02
CONFIGURATION_REG = 0x03
WHO_AM_I_REG      = 0x0B

## Config Parameter
BIT13_RESOLUTION      = 0b00000000
BIT16_RESOLUTION      = 0b10000000

OP_MODE_CONTINUOUS    = 0b00000000
OP_MODE_ONESHOT       = 0b00100000
OP_MODE_SPS           = 0b01000000
OP_MODE_SHUTDOWN      = 0b01100000

INTERRUPT_MODE        = 0b00000000
COMPARATOR_MODE       = 0b00010000

INT_LOW               = 0b00000000
INT_HIGH              = 0b00001000

CT_LOW                = 0b00000000
CT_HIGH               = 0b00000100

BIT16_OP_MODE_1FAULT  = 0b00000000
BIT16_OP_MODE_2FAULT  = 0b00000001
BIT16_OP_MODE_3FAULT  = 0b00000010
BIT16_OP_MODE_4FAULT  = 0b00000011

## smbus
bus = smbus.SMBus(1)

## FaBo Temperature I2C Controll class
class ADT7410:

    ## Constructor
    #  @param [in] address ADT7410 I2C slave address default:0x48
    def __init__(self, address=SLAVE_ADDRESS):
        self.address = address
        self.configure()

    ## Configure Device
    def configure(self):
        conf = BIT16_RESOLUTION | BIT16_OP_MODE_1FAULT | CT_LOW | INT_LOW | INTERRUPT_MODE | OP_MODE_CONTINUOUS

        bus.write_byte_data(self.address, CONFIGURATION_REG, conf)

    ## Data Ready Check
    #  @retval true Data ready
    #  @retval false Data Not ready
    def checkDataReady(self):
        status = bus.read_byte_data(self.address, STATUS_REG)

        if status & 0x80:
            return False
        else:
            return True

    ## Read Temperature Data
    #  @return value Temperature Data
    def read(self):

        if self.checkDataReady():
            config = bus.read_byte_data(self.address, CONFIGURATION_REG)
            data = bus.read_i2c_block_data(self.address, TEMP_MSB_REG, 2)

            adc = (data[0] << 8) | data[1]
            val = adc

            if config & 0x80:
                # 13bit resolution
                adc >>= 3
                if adc & 0x1000:       # 符号の判定
                    val = val - 8192   # マイナスの場合
                temp = float(val / 16.0)

            else:
                # 16bit resolution
                if adc & 0x8000:       # 符号の判定
                    val = val - 65536  # マイナスの場合
                temp = float(val / 128.0)

            return temp

        else:
            return 0.0

if __name__ == "__main__":
    adt7410 = ADT7410()

    while True:
        temp = adt7410.read()
        print "Temperature = ", temp
        print
        time.sleep(1)
