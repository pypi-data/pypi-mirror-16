=====
PyDMM
=====

PyDMM supports reading data from a digital multimeter (DMM).
Typical usage looks like this::

    import py_dmm.core as pd

    try:
        number = pd.read_dmm(port=myport, timeout=3)
        print(number)
    except:
        print("Error")


