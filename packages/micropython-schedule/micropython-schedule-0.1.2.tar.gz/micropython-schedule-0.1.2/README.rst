schedule
========


.. image:: https://api.travis-ci.org/rguillon/schedule.svg?branch=nodatetime
        :target: https://travis-ci.org/rguillon/schedule

.. image:: https://coveralls.io/repos/rguillon/schedule/badge.svg?branch=nodatetime
        :target: https://coveralls.io/r/rguillon/schedule

.. image:: https://img.shields.io/pypi/v/micropython-schedule.svg
        :target: https://pypi.python.org/pypi/micropython-schedule

.. image:: https://img.shields.io/pypi/dm/micropython-schedule.svg
        :target: https://pypi.python.org/pypi/micropython-schedule

Python job scheduling for humans.

An in-process scheduler for periodic jobs that uses the builder pattern
for configuration. Schedule lets you run Python functions (or any other
callable) periodically at pre-determined intervals using a simple,
human-friendly syntax.

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <http://adam.heroku.com/past/2010/4/13/rethinking_cron/>`_ (`Google cache <http://webcache.googleusercontent.com/search?q=cache:F14k7BNcufsJ:adam.heroku.com/past/2010/4/13/rethinking_cron/+&cd=1&hl=de&ct=clnk&gl=de>`_) and the `clockwork <https://github.com/tomykaira/clockwork>`_ Ruby module.

Features
--------
- A simple to use API for scheduling jobs.
- Very lightweight and no external dependencies.
- Excellent test coverage.
- Tested on Python 2.7 and 3.4

Usage
-----

.. code-block:: bash

    $ pip install schedule

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

FAQ
---

In lieu of a full documentation (coming soon) check out this set of `frequently asked questions <https://github.com/dbader/schedule/blob/master/FAQ.rst>`_ for solutions to some common questions.

Meta
----

Daniel Bader - `@dbader_org <https://twitter.com/dbader_org>`_ - mail@dbader.org

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

https://github.com/dbader/schedule
