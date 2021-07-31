import VersatileDeciMT64 as VDCM
import VersatileDeciConverter as VDC
def main(TargetNum, dimension, option):
    if option == 1:
        return VDCM.versatileDeci(0, TargetNum, dimension)
    else:
        if dimension <= 64:
            return VDC.versatileDeci(0, TargetNum, dimension)
        else:
            return VDCM.versatileDeci(0, TargetNum, dimension)
if __name__ == '__main__':
    main()