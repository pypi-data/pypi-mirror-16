# -*- coding: utf-8 -*-
import unittest
from khayyam import JalaliDatetime, teh_tz
from datetime import datetime, timedelta
from khayyam.timezones import TehranTimezone
from khayyam.jalali_date import JalaliDate
__author__ = 'vahid'


class TestJalaliDateTime(unittest.TestCase):
    
    def setUp(self):
        self.leap_year = 1375
        self.naive_jdt = JalaliDatetime(self.leap_year, 12, 30, 10, 2, 1, 3)
        self.aware_jdt = JalaliDatetime(self.leap_year, 12, 30, 10, 2, 1, 3, TehranTimezone())

    def test_instantiate(self):

        jalali_time = JalaliDatetime(1376, 10, 9, 8, 7, 6, 5)
        self.assertFalse(jalali_time is None)

        self.assertEqual(JalaliDatetime(jalali_time.todatetime()), jalali_time)
        self.assertEqual(JalaliDatetime(jalali_time), jalali_time)
        self.assertEqual(JalaliDatetime(jalali_time.date()).date(), jalali_time.date())
        self.assertEqual(JalaliDatetime(julian_day=2450674), JalaliDatetime(1376, 5, 23))

    def test_to_from_datetime(self):
        # Naive
        jalali_time1 = JalaliDatetime(self.naive_jdt.todatetime())
        self.assertEqual(self.naive_jdt, jalali_time1)
        
        # Aware
        jalali_time2 = JalaliDatetime(self.aware_jdt.todatetime())
        self.assertEqual(self.aware_jdt, jalali_time2)
        
    def test_today(self):
        dt = datetime.now().date()
        jdt = JalaliDatetime.today().date()
        self.assertEqual(jdt, JalaliDate(dt))
        
    def test_now(self):
        self.assertIsNotNone(JalaliDatetime.now())
        self.assertIsNone(JalaliDatetime.now().tzinfo)
        self.assertIsNotNone(JalaliDatetime.now(TehranTimezone()).tzinfo)
        
    def test_utcnow(self):
        jalali_utcnow = JalaliDatetime.utcnow()
        datetime_utcnow = jalali_utcnow.todatetime()
        self.assertEqual(jalali_utcnow.time(), datetime_utcnow.time())
    
    def test_strftime_strptime(self):
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assertEqual(d1.strftime('%Q'), 'Panjshanbeh 23 Esfand 1375 12:03:45 PM')
        self.assertEqual(
            d1.strptime('Panjshanbeh 23 Esfand 1375 12:03:45 PM', '%Q'),
            d1 - timedelta(microseconds=34567))

        self.assertEqual(d1.isoformat(), '%s-12-23T12:03:45.034567' % self.leap_year)
        tz_datetime = d1.astimezone(teh_tz)
        self.assertEqual(tz_datetime.strftime('%Z'), 'Iran/Tehran')

    def test_iso_format(self):
        jalali_time = JalaliDatetime(self.leap_year, 12, 23)
        self.assertEqual(jalali_time.isoformat(), '%s-12-23T00:00:00.000000' % self.leap_year)
        jalali_time = JalaliDatetime(self.leap_year, 12, 23, tzinfo=teh_tz)
        self.assertEqual(jalali_time.isoformat(), '%s-12-23T00:00:00.000000+03:30' % self.leap_year)

    def test_algorithm(self):
        min_date = datetime(1900, 1, 1, 1, 1, 1)
        max_days = 5000  # 3000 years !
        days = 0
        while True:
            dt = min_date + timedelta(days=days)
            jd = JalaliDatetime(dt)
            # print('Processing day: %s' % jd.year)
            dt2 = jd.todatetime()
            self.assertEqual(dt, dt2)
            days += 1
            if days > max_days:
                break

    def test_add(self):
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23)
        jalali_tme2 = jalali_time1 + timedelta(10)
        self.assertEqual(jalali_tme2, JalaliDatetime(self.leap_year + 1, 1, 3))
        
    def test_sub(self):
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23)
        jalali_time2 = jalali_time1 - timedelta(10)
        self.assertEqual(jalali_time2, JalaliDatetime(self.leap_year, 12, 13))
        difference = jalali_time1 - JalaliDatetime(self.leap_year - 1, 12, 1)
        self.assertEqual(difference, timedelta(387))
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23, 4, 2, 10, 7)
        self.assertEqual(jalali_time1 - jalali_time1.date(), timedelta(hours=4, minutes=2, seconds=10, microseconds=7))

    def test_lt_gt_le_ge_ne_eg(self):
        jalali_time1 = JalaliDatetime(self.leap_year, 12, 23)
        jalali_time2 = JalaliDatetime(self.leap_year, 12, 24)
        jalali_time3 = JalaliDatetime(self.leap_year, 12, 24)
        
        self.assertTrue(jalali_time1 <= jalali_time2)
        self.assertTrue(jalali_time1 != jalali_time2)
        self.assertFalse(jalali_time1 > jalali_time2)
        self.assertTrue(jalali_time2 == jalali_time3)

    def test_replace(self):
        d1 = JalaliDatetime(1391, 12, 30)
        self.assertEqual(d1.replace(year=1395), JalaliDatetime(1395, 12, 30))
        self.assertEqual(d1.replace(month=1),   JalaliDatetime(1391, 1, 30))
        self.assertEqual(d1.replace(day=1),     JalaliDatetime(1391, 12, 1))
        self.assertRaises(ValueError, d1.replace, year=1392)

    def test_repr(self):
        d1 = JalaliDatetime(self.leap_year, 12, 23, 12, 3, 45, 34567)
        self.assertEqual(repr(d1), 'khayyam.JalaliDatetime(1375, 12, 23, 12, 3, 45, 34567, Panjshanbeh)')

if __name__ == '__main__':
    unittest.main()
