import ephem
import unittest

METHODS = (
    ephem.Observer.previous_rising,
    ephem.Observer.previous_setting,
    ephem.Observer.next_rising,
    ephem.Observer.next_setting,
)

class RiseSetTests(unittest.TestCase):
    maxDiff = 10000

    def test_sun(self):
        s = ephem.Sun()
        o = ephem.Observer()
        o.lat = '36.4072'
        o.lon = '-105.5734'
        o.date = '2021/11/24'
        expected = """\
0.0 0.0 False
2021/11/23 13:51:09 previous_rising
2021/11/23 23:46:11 previous_setting
2021/11/24 13:52:08 next_rising
2021/11/24 23:45:47 next_setting

0.0 0.0 True
2021/11/23 13:52:38 previous_rising
2021/11/23 23:44:41 previous_setting
2021/11/24 13:53:38 next_rising
2021/11/24 23:44:17 next_setting

0.0 1010.0 False
2021/11/23 13:47:44 previous_rising
2021/11/23 23:49:36 previous_setting
2021/11/24 13:48:43 next_rising
2021/11/24 23:49:12 next_setting

0.0 1010.0 True
2021/11/23 13:49:33 previous_rising
2021/11/23 23:47:46 previous_setting
2021/11/24 13:50:32 next_rising
2021/11/24 23:47:22 next_setting

-0.8333 0.0 False
2021/11/23 13:46:34 previous_rising
2021/11/23 23:50:46 previous_setting
2021/11/24 13:47:33 next_rising
2021/11/24 23:50:22 next_setting

-0.8333 0.0 True
2021/11/23 13:48:03 previous_rising
2021/11/23 23:49:17 previous_setting
2021/11/24 13:49:02 next_rising
2021/11/24 23:48:53 next_setting

-0.8333 1010.0 False
2021/11/23 13:41:44 previous_rising
2021/11/23 23:55:36 previous_setting
2021/11/24 13:42:42 next_rising
2021/11/24 23:55:13 next_setting

-0.8333 1010.0 True
2021/11/23 13:43:44 previous_rising
2021/11/23 23:53:35 previous_setting
2021/11/24 13:44:43 next_rising
2021/11/24 23:53:12 next_setting
"""
        expected = expected.splitlines()
        actual = self._generate_report(o, s)
        for n, (expected, actual) in enumerate(zip(expected, actual), 1):
            self.assertEqual(expected, actual, 'Line {}'.format(n))

    def test_moon(self):
        m = ephem.Moon()
        o = ephem.Observer()
        o.lat = '36.4072'
        o.lon = '-105.5734'
        o.date = '2021/11/24'
        expected = """\
0.0 0.0 False
2021/11/23 02:21:39 previous_rising
2021/11/23 17:34:47 previous_setting
2021/11/24 03:15:45 next_rising
2021/11/24 18:18:46 next_setting

0.0 0.0 True
2021/11/23 02:23:09 previous_rising
2021/11/23 17:33:17 previous_setting
2021/11/24 03:17:15 next_rising
2021/11/24 18:17:18 next_setting

0.0 1010.0 False
2021/11/23 02:17:52 previous_rising
2021/11/23 17:38:32 previous_setting
2021/11/24 03:12:00 next_rising
2021/11/24 18:22:25 next_setting

0.0 1010.0 True
2021/11/23 02:19:43 previous_rising
2021/11/23 17:36:41 previous_setting
2021/11/24 03:13:51 next_rising
2021/11/24 18:20:36 next_setting

-0.8333 0.0 False
2021/11/23 02:16:31 previous_rising
2021/11/23 17:39:52 previous_setting
2021/11/24 03:10:40 next_rising
2021/11/24 18:23:43 next_setting

-0.8333 0.0 True
2021/11/23 02:18:02 previous_rising
2021/11/23 17:38:21 previous_setting
2021/11/24 03:12:11 next_rising
2021/11/24 18:22:14 next_setting

-0.8333 1010.0 False
2021/11/23 02:11:04 previous_rising
2021/11/23 17:45:16 previous_setting
2021/11/24 03:05:16 next_rising
2021/11/24 18:28:58 next_setting

-0.8333 1010.0 True
2021/11/23 02:13:10 previous_rising
2021/11/23 17:43:11 previous_setting
2021/11/24 03:07:21 next_rising
2021/11/24 18:26:56 next_setting
"""
        expected = expected.splitlines()
        actual = self._generate_report(o, m)
        for n, (expected, actual) in enumerate(zip(expected, actual), 1):
            self.assertEqual(expected, actual, 'Line {}'.format(n))

    def _generate_report(self, o, body):
        for horizon in 0.0, '-0.8333':
            for pressure in 0.0, 1010.0:
                for use_center in False, True:
                    o.horizon = horizon
                    o.pressure = pressure
                    yield '{} {} {}'.format(horizon, pressure, use_center)
                    for method in METHODS:
                        d = method(o, body, use_center=use_center)
                        yield '{} {}'.format(d, method.__name__)
                    yield ''
