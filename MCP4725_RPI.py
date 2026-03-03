#import RPi.GPIO as GPIO
import smbus2
import time

MCP4725_address = 0x60
i2cbus = smbus2.SMBus(1)

def clipping(value):
    if value > 4095:
        value = 4095
    if value < 0:
        value = 0
    return value

def mcp4725_normal_write(value):
    value = clipping(value)
    i2cbus.write_i2c_block_data(MCP4725_address, 0x40, [value >> 4, (value & 0x0F)<<4])

def mcp4725_eeprom_write(value):
    value = clipping(value)
    i2cbus.write_i2c_block_data(MCP4725_address, 0x60, [value >> 4, (value & 0x0F)<<4])

try:
    while True:
        mcp4725_normal_write(0)
        time.sleep(5)
        mcp4725_normal_write(1240)
        time.sleep(5)
        mcp4725_normal_write(2482)
        time.sleep(5)
        mcp4725_normal_write(3723)
        time.sleep(5)
except KeyboardInterrupt:
    pass


mcp4725_eeprom_write(0)