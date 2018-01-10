import pigpio
from enum import Enum

class L6470(Enum):
    ABS_POS = 0x01
    EL_POS = 0x02
    MARK = 0x03
    SPEED = 0x04
    ACC = 0x05
    DEC = 0x06
    MAX_SPEED = 0x07
    MIN_SPEED = 0x08
    FS_SPD = 0x15
    KVAL_HOLD = 0x09
    KVAL_RUN = 0x0a
    KVAL_ACC = 0x0b
    KVAL_DEC = 0x0c
    INT_SPD = 0x0d
    ST_SLP = 0x0e
    FN_SLP_ACC = 0x0f
    FN_SLP_DEC = 0x10
    K_THERM = 0x11
    ADC_OUT = 0x12
    OCD_TH = 0x13
    STALL_TH = 0x14
    STEP_MODE = 0x16
    ALARM_EN = 0x17
    CONFIG = 0x18
    STATUS = 0x19
    RUN = 0x50
    RUN_R = 0x51
    MOVE = 0x40
    MOVE_R = 0x41
    GOTO = 0x60
    GOTO_DIR = 0x68
    GOTO_DIR_R = 0x69

    def __init__(self,pi,spi_channel):
        self.pi = pi
        self.h = pi.spi_open(spi_channel,1000000,0)

    def setParam(self,address,value):
        length, buf = paramSpliter(address, value)
        self.writeParam(self.address, buf)

    def writeParam(self,address,value):
        self.pi.spi_write(self.h,address.value )
        for i in value:
            self.pi.spi_write(self.h,value[-1-i])

    def getParam(self, param):
        length, buf = paramSpliter(address, value)
        self.pi.spi_write(self.h,self.address.value | 0x20 )
        return self.readParam(length)

    def readParam(self, length):
        for i in range(length):
            c,raw = self.pi.spi_read(self.h,1)
            data += raw[0] << ((length - i) * 8)
        return data

    def paramSpliter(self, address, value): #MSBfirst
        dataArray =[]
        if address == ABS_POS
        or address == MARK
        or address == SPEED
            splitnum = 3
        
        elif address == EL_POS
        or address == ACC
        or address == DEC
        or address == MAX_SPEED
        or address == MIN_SPEED
        or address == INT_SPD
        or address == FS_SPD
        or address == CONFIG
        or address == STATUS :
            splitnum = 2
        
        else:
            splitnum = 1

        return data2array(value, splitnum)

    def data2array(self, value, splitnum):
        for i in range(splitnum):
            dataArray[i] = (value >> (i * 8) ) & 0x0f
        return splitnum, dataArray


