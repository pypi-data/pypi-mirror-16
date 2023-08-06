==============
timezonefinder
==============

.. image:: https://img.shields.io/travis/MrMinimal64/timezonefinder.svg?branch=master
    :target: https://travis-ci.org/MrMinimal64/timezonefinder

.. image:: https://img.shields.io/pypi/wheel/timezonefinder.svg
    :target: https://pypi.python.org/pypi/timezonefinder

.. image:: https://img.shields.io/pypi/v/timezonefinder.svg
    :target: https://pypi.python.org/pypi/timezonefinder


This is a fast and lightweight python project for looking up the corresponding
timezone for a given lat/lng on earth entirely offline.

This project is derived from and has been successfully tested against
`pytzwhere <https://pypi.python.org/pypi/tzwhere>`__
(`github <https://github.com/pegler/pytzwhere>`__), but aims at providing
improved performance and usability.


The underlying timezone data is based on work done by `Eric
Muller <http://efele.net/maps/tz/world/>`__.

Timezones at sea and Antarctica are not yet supported (because somewhat
special rules apply there).

`timezone_finder <https://github.com/gunyarakun/timezone_finder>`__ is a ruby port of this package.


Also see: `GitHub <https://github.com/MrMinimal64/timezonefinder>`__ `PyPI <https://pypi.python.org/pypi/timezonefinder/>`__


Dependencies
============

(``python``, ``math``, ``struct``, ``os``)

``numpy``


**Optional:**


``Numba`` (https://github.com/numba/numba) and its Requirement `llvmlite <http://llvmlite.pydata.org/en/latest/install/index.html>`_


This is only for precompiling the time critical algorithms. When you only look up a
few points once in a while, the compilation time is probably outweighing
the benefits. When using ``certain_timezone_at()`` and especially
``closest_timezone_at()`` however, I highly recommend using ``numba``
(see speed comparison below)! The amount of shortcuts used in the
``.bin`` is also only optimized for the use with ``numba``.

Installation
============

(install the dependencies)

in your terminal simply:

::

    pip install timezonefinder

(you might need to run this command as administrator)



Usage
=====

Basics:
-------

::

    from timezonefinder import TimezoneFinder

    tf = TimezoneFinder()


for testing if numba is being used:
(if the import of the optimized algorithms worked)

::

    TimezoneFinder.using_numba()   # this is a static method returning True or False


**timezone_at():**

This is the default function to check which timezone a point lies within (similar to tzwheres ``tzNameAt()``).
If no timezone has been found, ``None`` is being returned.

**PLEASE NOTE:** This approach is optimized for speed and the common case to only query points within a timezone.
The last possible timezone in proximity is always returned (without checking if the point is really included).
So results might be misleading for points outside of any timezone.


::

    longitude = 13.358
    latitude = 52.5061
    tf.timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Berlin'


**certain_timezone_at():**

This function is for making sure a point is really inside a timezone. It is slower, because all polygons (with shortcuts in that area)
are checked until one polygon is matched.

::

    tf.certain_timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Berlin'


**Proximity algorithm:**

Only use this when the point is not inside a polygon, because the approach otherwise makes no sense.
This returns the closest timezone of all polygons within +-1 degree lng and +-1 degree lat (or None).

::

    longitude = 12.773955
    latitude = 55.578595
    tf.closest_timezone_at(lng=longitude, lat=latitude) # returns 'Europe/Copenhagen'

**Other options:**

To increase search radius even more, use the ``delta_degree``-option:

::

    tf.closest_timezone_at(lng=longitude, lat=latitude, delta_degree=3)


This checks all the polygons within +-3 degree lng and +-3 degree lat.
I recommend only slowly increasing the search radius, since computation time increases quite quickly
(with the amount of polygons which need to be evaluated) and there might be many polygons within a couple degrees. When you want to use this feature a lot,
consider using ``Numba`` to save computing time.


Also keep in mind that x degrees lat are not the same distance apart than x degree lng (earth is a sphere)!
So to really make sure you got the closest timezone increase the search radius until you get a result,
then increase the radius once more and take this result (should only make a difference in really rare cases).


With ``exact_computation=True`` the distance to every polygon edge is computed (way more complicated), instead of just evaluating the distances to all the vertices.
 This only makes a real difference when polygons are very close.


With ``return_distances=True`` the output looks like this:

( 'tz_name_of_the_closest_polygon',[ distances to every polygon in km], [tz_names of every polygon])

Note that some polygons might not be tested (for example when a zone is found to be the closest already).
To prevent this use ``force_evaluation=True``.

::

    longitude = 42.1052479
    latitude = -16.622686
    tf.closest_timezone_at(lng=longitude, lat=latitude, delta_degree=2,
                                        exact_computation=True, return_distances=True, force_evaluation=True)
    '''
    returns ('uninhabited',
    [80.66907784731714, 217.10924866254518, 293.5467252349301, 304.5274937839159, 238.18462606485667, 267.918674688949, 207.43831938964408, 209.6790144988553, 228.42135641542546],
    ['uninhabited', 'Indian/Antananarivo', 'Indian/Antananarivo', 'Indian/Antananarivo', 'Africa/Maputo', 'Africa/Maputo', 'Africa/Maputo', 'Africa/Maputo', 'Africa/Maputo'])
    '''

Further application:
--------------------

**To maximize the chances of getting a result in a** ``Django`` **view it might look like:**

::

    def find_timezone(request, lat, lng):
        lat = float(lat)
        lng = float(lng)

        try:
            timezone_name = tf.timezone_at(lng=lng, lat=lat)
            if timezone_name is None:
                timezone_name = tf.closest_timezone_at(lng=lng, lat=lat)
                # maybe even increase the search radius when it is still None

        except ValueError:
            # the coordinates were out of bounds
            # {handle error}

        # ... do something with timezone_name ...

**To get an aware datetime object from the timezone name:**

::

    # first pip install pytz
    from pytz import timezone, utc
    from pytz.exceptions import UnknownTimeZoneError

    # tzinfo has to be None (means naive)
    naive_datetime = YOUR_NAIVE_DATETIME

    try:
        tz = timezone(timezone_name)
        aware_datetime = naive_datetime.replace(tzinfo=tz)
        aware_datetime_in_utc = aware_datetime.astimezone(utc)

        naive_datetime_as_utc_converted_to_tz = tz.localize(naive_datetime)

    except UnknownTimeZoneError:
        # ... handle the error ...

also see the `pytz Doc <http://pytz.sourceforge.net/>`__.

**Using the conversion tool:**

Make sure you installed the GDAL framework (that`s for converting .shp shapefiles into .json)
Change to the directory of the timezonefinder package (location of ``file_converter.py``) in your terminal and then:

::

    wget http://efele.net/maps/tz/world/tz_world.zip
    # on mac: curl "http://efele.net/maps/tz/world/tz_world.zip" -o "tz_world.zip"
    unzip tz_world
    ogr2ogr -f GeoJSON -t_srs crs:84 tz_world.json ./world/tz_world.shp
    rm ./world/ -r
    rm tz_world.zip


There should be a tz_world.json (of approx. 100MB) in the folder together with the ``file_converter.py`` now.
Then run the converter by:

::

    python file_converter.py


This converts the .json into the needed ``.bin`` (overwriting the old version!) and also updates the ``timezone_names.py``.

**Please note:** Neither tests nor the file\_converter.py are optimized or
really beautiful. Sorry for that. If you have questions just write me (s. section 'Contact' below)

Comparison to pytzwhere
=======================

In comparison to
`pytzwhere <https://pypi.python.org/pypi/tzwhere/2.2>`__ most notably initialisation time and memory usage are
significantly reduced, while the algorithms yield the same results and are as fast or even faster
(depending on the dependencies used, s. test results below).
In some cases ``pytzwhere``
even does not find anything and ``timezonefinder`` does, for example
when only one timezone is close to the point.

**Similarities:**

-  results

-  data being used


**Differences:**

-  highly decreased memory usage

-  highly reduced start up time

-  the data is now stored in a memory friendly 18MB ``.bin`` and needed
   data is directly being read on the fly (instead of reading, converting and KEEPING the 76MB ``.csv``
   -mostly floats stored as strings!- into
   memory every time a class is created).

-  precomputed shortcuts are stored in the ``.bin`` to quickly look up
   which polygons have to be checked (instead of computing and storing the shortcuts
   on every startup)

-  introduced proximity algorithm

-  use of ``numba`` for precompilation (almost reaching the speed of tzwhere with shapely on and keeping the hole data in the memory)

**test results**\*:

::


    test correctness:
    Results:
    LOCATION             | EXPECTED             | COMPUTED             | Status
    ====================================================================
    Arlington, TN        | America/Chicago      | America/Chicago      | OK
    Memphis, TN          | America/Chicago      | America/Chicago      | OK
    Anchorage, AK        | America/Anchorage    | America/Anchorage    | OK
    Eugene, OR           | America/Los_Angeles  | America/Los_Angeles  | OK
    Albany, NY           | America/New_York     | America/New_York     | OK
    Moscow               | Europe/Moscow        | Europe/Moscow        | OK
    Los Angeles          | America/Los_Angeles  | America/Los_Angeles  | OK
    Moscow               | Europe/Moscow        | Europe/Moscow        | OK
    Aspen, Colorado      | America/Denver       | America/Denver       | OK
    Kiev                 | Europe/Kiev          | Europe/Kiev          | OK
    Jogupalya            | Asia/Kolkata         | Asia/Kolkata         | OK
    Washington DC        | America/New_York     | America/New_York     | OK
    St Petersburg        | Europe/Moscow        | Europe/Moscow        | OK
    Blagoveshchensk      | Asia/Yakutsk         | Asia/Yakutsk         | OK
    Boston               | America/New_York     | America/New_York     | OK
    Chicago              | America/Chicago      | America/Chicago      | OK
    Orlando              | America/New_York     | America/New_York     | OK
    Seattle              | America/Los_Angeles  | America/Los_Angeles  | OK
    London               | Europe/London        | Europe/London        | OK
    Church Crookham      | Europe/London        | Europe/London        | OK
    Fleet                | Europe/London        | Europe/London        | OK
    Paris                | Europe/Paris         | Europe/Paris         | OK
    Macau                | Asia/Macau           | Asia/Macau           | OK
    Russia               | Asia/Yekaterinburg   | Asia/Yekaterinburg   | OK
    Salo                 | Europe/Helsinki      | Europe/Helsinki      | OK
    Staffordshire        | Europe/London        | Europe/London        | OK
    Muara                | Asia/Brunei          | Asia/Brunei          | OK
    Puerto Montt seaport | America/Santiago     | America/Santiago     | OK
    Akrotiri seaport     | Asia/Nicosia         | Asia/Nicosia         | OK
    Inchon seaport       | Asia/Seoul           | Asia/Seoul           | OK
    Nakhodka seaport     | Asia/Vladivostok     | Asia/Vladivostok     | OK
    Truro                | Europe/London        | Europe/London        | OK
    Aserbaid. Enklave    | Asia/Baku            | Asia/Baku            | OK
    Tajikistani Enklave  | Asia/Dushanbe        | Asia/Dushanbe        | OK
    Busingen Ger         | Europe/Busingen      | Europe/Busingen      | OK
    Genf                 | Europe/Zurich        | Europe/Zurich        | OK
    Lesotho              | Africa/Maseru        | Africa/Maseru        | OK
    usbekish enclave     | Asia/Tashkent        | Asia/Tashkent        | OK
    usbekish enclave     | Asia/Tashkent        | Asia/Tashkent        | OK
    Arizona Desert 1     | America/Denver       | America/Denver       | OK
    Arizona Desert 2     | America/Phoenix      | America/Phoenix      | OK
    Arizona Desert 3     | America/Phoenix      | America/Phoenix      | OK
    Far off Cornwall     | None                 | None                 | OK

    closest_timezone_at():
    LOCATION             | EXPECTED             | COMPUTED             | Status
    ====================================================================
    Arlington, TN        | America/Chicago      | America/Chicago      | OK
    Memphis, TN          | America/Chicago      | America/Chicago      | OK
    Anchorage, AK        | America/Anchorage    | America/Anchorage    | OK
    Shore Lake Michigan  | America/New_York     | America/New_York     | OK
    English Channel1     | Europe/London        | Europe/London        | OK
    English Channel2     | Europe/Paris         | Europe/Paris         | OK
    Oresund Bridge1      | Europe/Stockholm     | Europe/Stockholm     | OK
    Oresund Bridge2      | Europe/Copenhagen    | Europe/Copenhagen    | OK

    testing 10000 realistic points
    [These tests dont make sense at the moment because tzwhere is still using old data]
    testing 1000 realistic points
    MISMATCHES:
    Point                                    | timezone_at()        | certain_timezone_at() | tzwhere
    =========================================================================

    in 1000 tries 0 mismatches were made

    testing 1000 random points
    MISMATCHES:
    Point                                    | timezone_at()        | certain_timezone_at() | tzwhere
    =========================================================================
    (57.71985093778474, 50.93465824884237)   | Europe/Kirov         | Europe/Kirov          | Europe/Volgograd
    (56.993217193375955, -123.66721983141636) | America/Dawson_Creek | America/Dawson_Creek  | America/Vancouver


    shapely: OFF (tzwhere)
    Numba: OFF (timezonefinder)

    TIMES for  1000 realistic points
    tzwhere: 0:00:05.990420
    timezonefinder: 0:00:00.075704
    78.13 times faster


    TIMES for  1000 random points
    tzwhere: 0:00:08.626960
    timezonefinder: 0:00:01.242737
    5.94 times faster

    Startup times:
    tzwhere: 0:00:08.548387
    timezonefinder: 0:00:00.000122
    70068.75 times faster


    shapely: OFF (tzwhere)
    Numba: ON (timezonefinder)


    TIMES for  10000 realistic points
    tzwhere: 0:00:54.239579
    timezonefinder: 0:00:00.395794
    137.04 times faster


    TIMES for  10000 random points
    tzwhere: 0:01:30.232851
    timezonefinder: 0:00:00.518453
    174.04 times faster

    Startup times:
    tzwhere: 0:00:08.328661
    timezonefinder: 0:00:00.000297
    28042.63 times faster

    shapely: ON (tzwhere)
    Numba: OFF (timezonefinder)


    TIMES for  10000 realistic points
    tzwhere: 0:00:00.429949
    timezonefinder: 0:00:01.366008
    0.31 times faster


    TIMES for  10000 random points
    tzwhere: 0:00:00.566208
    timezonefinder: 0:00:11.725017
    0.05 times faster


    shapely: ON (tzwhere)
    Numba: ON (timezonefinder)


    TIMES for  10000 realistic points
    tzwhere: 0:00:00.376166
    timezonefinder: 0:00:00.489993
    0.3 times slower


    TIMES for  10000 random points
    tzwhere: 0:00:00.587144
    timezonefinder: 0:00:00.613341
    0.04 times slower


    Startup times:
    tzwhere: 0:00:38.335302
    timezonefinder: 0:00:00.000143
    268079.03 times faster


\* System: MacBookPro 2,4GHz i5 (2014) 4GB RAM SSD pytzwhere with numpy active

\*\*mismatch: pytzwhere finds something and then timezonefinder finds
something else

\*\*\*realistic queries: just points within a timezone (= pytzwhere
yields result)

\*\*\*\*random queries: random points on earth


Known Issues
============

I ran tests for approx. 5M points and these are no mistakes I found.


Contact
=======

This is the first public python project I did, so most certainly there is stuff I missed,
things I could have optimized even further etc. That's why I would be really glad to get some feedback on my code.


If you notice that the tz data is outdated, encounter any bugs, have
suggestions, criticism, etc. feel free to **open an Issue**, **add a Pull Requests** on Git or ...

contact me: *python at michelfe dot it*


Credits
=======

Thanks to:

`Adam <https://github.com/adamchainz>`__ for adding organisational features to the project and for helping me with publishing and testing routines.

`cstich <https://github.com/cstich>`__ for the little conversion script (.shp to .json)

License
=======

``timezonefinder`` is distributed under the terms of the MIT license
(see LICENSE.txt).


Changelog
=========


1.5.7 (2016-07-21)
------------------

* fixed a little bug with too many arguments in a @jit function
* clarified usage of the API in the Readme
* all functions are now keyword-args only (to prevent lng lat mix-up errors)
* prepared the usage of the ahead of time compilation functionality of Numba. It is not enabled yet.
* sorting the polygons to check in the order of how often their zones appear gives a speed bonus


1.5.6 (2016-06-16)
------------------

* using little endian encoding now
* introduced test for checking the proper functionality of the helper functions
* wrote tests for proximity algorithms
* improved proximity algorithms: introduced exact_computation, return_distances and force_evaluation functionality (s. Readme or documentation for more info)

1.5.5 (2016-06-03)
------------------

* using the newest version (2016d, May 2016) of the `tz world data`_
* holes in the polygons which are stored in the tz_world data are now correctly stored and handled
* rewrote the file_converter for storing the holes at the end of the timezone_data.bin
* added specific test cases for hole handling
* made some optimizations in the algorithms

1.5.4 (2016-04-26)
------------------

* using the newest version (2016b) of the `tz world data`_
* rewrote the file_converter for parsing a .json created from the tz_worlds .shp
* had to temporarily fix one polygon manually which had the invalid TZID: 'America/Monterey' (should be 'America/Monterrey')
* had to make tests less strict because tzwhere still used the old data at the time and some results were simply different now


1.5.3 (2016-04-23)
------------------

* using 32-bit ints for storing the polygons now (instead of 64-bit): I calculated that the minimum accuracy (at the equator) is 1cm with the encoding being used. Tests passed.
* Benefits: 18MB file instead of 35MB, another 10-30% speed boost (depending on your hardware)


1.5.2 (2016-04-20)
------------------

* added python 2.7.6 support: replaced strings in unpack (unsupported by python 2.7.6 or earlier) with byte strings
* timezone names are now loaded from a separate file for better modularity


1.5.1 (2016-04-18)
------------------

* added python 2.7.8+ support:
    Therefore I had to change the tests a little bit (some operations were not supported). This only affects output.
    I also had to replace one part of the algorithms to prevent overflow in Python 2.7


1.5.0 (2016-04-12)
------------------

* automatically using optimized algorithms now (when numba is installed)
* added TimezoneFinder.using_numba() function to check if the import worked


1.4.0 (2016-04-07)
------------------

* Added the ``file_converter.py`` to the repository: It converts the .csv from pytzwhere to another ``.csv`` and this one into the used ``.bin``.
    Especially the shortcut computation and the boundary storage in there save a lot of reading and computation time, when deciding which timezone the coordinates are in.
    It will help to keep the package up to date, even when the timezone data should change in the future.


    .. _tz world data: <http://efele.net/maps/tz/world/>


