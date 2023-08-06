schedule
========


.. image:: https://api.travis-ci.org/rguillon/schedule.svg
        :target: https://travis-ci.org/rguillon/schedule

.. image:: https://coveralls.io/repos/rguillon/schedule/badge.svg
        :target: https://coveralls.io/r/rguillon/schedule

.. image:: https://img.shields.io/pypi/v/micropython-schedule.svg
        :target: https://pypi.python.org/pypi/micropython-schedule

.. image:: https://img.shields.io/pypi/dm/micropython-schedule.svg
        :target: https://pypi.python.org/pypi/micropython-schedule

MicroPython job scheduling for humans.

A micronized port of <https://github.com/dbader/schedule>

The implementation uses timestamps and time tuple instead of datetime, saving a few kilobytes of RAM. 


Usage
-----

.. code-block:: bash

    $ micropython -m upip install micropython-schedule

.. code-block:: python

    import schedule
    import time

    def job():
        print("I'm working...")

    schedule.every(10).minutes.do(job)
    schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

Meta
----

Renaud Guillon - - renaud.guillon@gmail.com

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

https://github.com/rguillon/schedule
