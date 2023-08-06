=====
PyDMM
=====

PyDMM supports reading data from a digital multimeter (DMM).
Typical usage looks like this::

    from pydmm import read_dmm

    try:
        number = read_dmm(port=myport, timeout=3)
        print(number)
    except:
        print("Error")


