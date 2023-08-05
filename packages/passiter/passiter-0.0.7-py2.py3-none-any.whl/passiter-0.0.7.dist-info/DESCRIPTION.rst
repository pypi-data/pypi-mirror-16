==============================================
Passiter: A simple password generator
==============================================

Install
=========================

.. code-block:: shell

    pip install passiter

Usage
=========================

- passwords are 8 characters containing 2 uppercases, 2 number and 1 symbol by default

.. code-block:: python

    from passiter import passiter
    p = passiter()
    for _ in range(10):
        print(next(p))
    # bA2x9m,P
    # b:vOj29N
    # sN%6gCh4
    # ,khl0M5O
    # jZ3F1v{d
    # H5Atra^1
    # t$7qM4Zv
    # 7lUi6[Tj
    # Y6p5cw_E
    # Db>Qn45p


- you can change passwords length and number of uppercases, numbers, symbols

.. code-block:: python

    from passiter import passiter
    p = passiter(length=16, uppers=3, numbers=3, symbols=0)
    for _ in range(10):
        print(next(p))
    # b8DxXreiajv4A0hs
    # fcs9xitykSj7q6VO
    # gUVyi3Du7ode5kzs
    # I9wzlhedt1njV0Xr
    # wNA1lbf34geGhjcm
    # 1G6zobtlk3euiLhM
    # kh9cKuaZ2yonjH4x
    # F6KbSql4vs0gfdar
    # ojI8tqwlSzmBib09
    # hgxp6kvSwZdjVb07


