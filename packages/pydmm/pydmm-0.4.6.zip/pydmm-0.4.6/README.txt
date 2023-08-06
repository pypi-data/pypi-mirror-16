=================================
Python Digital Multimeter (PyDMM)
=================================

**PyDMM** facilitates reading data from a digital multimeter (DMM). 
It works for example with *HP-90EPC*.
Typical usage looks like this::

    import pydmm.pydmm as pd

    try:
        number = pd.read_dmm(port=myport, timeout=3)
        print(number)
    except:
        print("Error")

Preparations
------------
- install pyserial
- install pydmm (this module)
- connect the DMM to the usb-port of your computer 
- find out, which COM-port the device uses
- use the port number *myport* (COM3 has number 2) when calling read_dmm()
