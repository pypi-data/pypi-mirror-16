import re
from binascii import unhexlify
from datetime import datetime, timedelta, date
from decimal import Decimal
from email.mime.text import MIMEText
from fractions import Fraction
from uuid import UUID

import pytest

from cbor2.compat import timezone
from cbor2.encoder import dumps, CBOREncodeError, dump
from cbor2.types import CBORTag, undefined


@pytest.mark.parametrize('value, expected', [
    (0, '00'),
    (1, '01'),
    (10, '0a'),
    (23, '17'),
    (24, '1818'),
    (100, '1864'),
    (1000, '1903e8'),
    (1000000, '1a000f4240'),
    (1000000000000, '1b000000e8d4a51000'),
    (18446744073709551615, '1bffffffffffffffff'),
    (18446744073709551616, 'c249010000000000000000'),
    (-18446744073709551616, '3bffffffffffffffff'),
    (-18446744073709551617, 'c349010000000000000000'),
    (-1, '20'),
    (-10, '29'),
    (-100, '3863'),
    (-1000, '3903e7')
])
def test_integer(value, expected):
    expected = unhexlify(expected)
    assert dumps(value) == expected


@pytest.mark.parametrize('value, expected', [
    (1.1, 'fb3ff199999999999a'),
    (1.0e+300, 'fb7e37e43c8800759c'),
    (-4.1, 'fbc010666666666666'),
    (float('inf'), 'f97c00'),
    (float('nan'), 'f97e00'),
    (float('-inf'), 'f9fc00')
])
def test_float(value, expected):
    expected = unhexlify(expected)
    assert dumps(value) == expected


@pytest.mark.parametrize('value, expected', [
    (b'', '40'),
    (b'\x01\x02\x03\x04', '4401020304'),
])
def test_bytestring(value, expected):
    expected = unhexlify(expected)
    assert dumps(value) == expected


def test_bytearray():
    expected = unhexlify('4401020304')
    assert dumps(bytearray(b'\x01\x02\x03\x04')) == expected


@pytest.mark.parametrize('value, expected', [
    (u'', '60'),
    (u'a', '6161'),
    (u'IETF', '6449455446'),
    (u'"\\', '62225c'),
    (u'\u00fc', '62c3bc'),
    (u'\u6c34', '63e6b0b4')
])
def test_string(value, expected):
    expected = unhexlify(expected)
    assert dumps(value) == expected


@pytest.mark.parametrize('value, expected', [
    (False, 'f4'),
    (True, 'f5'),
    (None, 'f6'),
    (undefined, 'f7')
], ids=['false', 'true', 'null', 'undefined'])
def test_special(value, expected):
    expected = unhexlify(expected)
    assert dumps(value) == expected


#
# Tests for extension tags
#

@pytest.mark.parametrize('value, as_timestamp, expected', [
    (datetime(2013, 3, 21, 20, 4, 0, tzinfo=timezone.utc), False,
     'c074323031332d30332d32315432303a30343a30305a'),
    (datetime(2013, 3, 21, 22, 4, 0, tzinfo=timezone(timedelta(hours=2))), False,
     'c07819323031332d30332d32315432323a30343a30302b30323a3030'),
    (datetime(2013, 3, 21, 20, 4, 0), False, 'c074323031332d30332d32315432303a30343a30305a'),
    (datetime(2013, 3, 21, 20, 4, 0, tzinfo=timezone.utc), True, 'c11a514b67b0'),
    (datetime(2013, 3, 21, 22, 4, 0, tzinfo=timezone(timedelta(hours=2))), True, 'c11a514b67b0')
], ids=['datetime/utc', 'datetime/eet', 'naive', 'timestamp/utc', 'timestamp/eet'])
def test_datetime(value, as_timestamp, expected):
    expected = unhexlify(expected)
    assert dumps(value, datetime_as_timestamp=as_timestamp, timezone=timezone.utc) == expected


def test_date():
    expected = unhexlify('c074323031332d30332d32315430303a30303a30305a')
    assert dumps(date(2013, 3, 21), timezone=timezone.utc) == expected


def test_naive_datetime():
    """Test that naive datetimes are gracefully rejected when no timezone has been set."""
    exc = pytest.raises(CBOREncodeError, dumps, datetime(2013, 3, 21))
    assert str(exc.value) == 'naive datetime encountered and no default timezone has been set'


@pytest.mark.parametrize('value, expected', [
    (Decimal('14.123'), 'c4822219372b'),
    (Decimal('NaN'), 'f97e00'),
    (Decimal('Infinity'), 'f97c00'),
    (Decimal('-Infinity'), 'f9fc00')
], ids=['normal', 'nan', 'inf', 'neginf'])
def test_decimal(value, expected):
    expected = unhexlify(expected)
    assert dumps(value) == expected


def test_rational():
    expected = unhexlify('d81e820205')
    assert dumps(Fraction(2, 5)) == expected


def test_regex():
    expected = unhexlify('d8236d68656c6c6f2028776f726c6429')
    assert dumps(re.compile(u'hello (world)')) == expected


def test_mime():
    expected = unhexlify(
        'd824787b436f6e74656e742d547970653a20746578742f706c61696e3b20636861727365743d2269736f2d38'
        '3835392d3135220a4d494d452d56657273696f6e3a20312e300a436f6e74656e742d5472616e736665722d456'
        'e636f64696e673a2071756f7465642d7072696e7461626c650a0a48656c6c6f203d413475726f')
    message = MIMEText(u'Hello \u20acuro', 'plain', 'iso-8859-15')
    assert dumps(message) == expected


def test_uuid():
    expected = unhexlify('d825505eaffac8b51e480581277fdcc7842faf')
    assert dumps(UUID(hex='5eaffac8b51e480581277fdcc7842faf')) == expected


def test_custom_tag():
    expected = unhexlify('d917706548656c6c6f')
    assert dumps(CBORTag(6000, u'Hello')) == expected


def test_cyclic_array():
    """Test that an array that contains itself can be serialized with value sharing enabled."""
    expected = unhexlify('d81c81d81c81d81d00')
    a = [[]]
    a[0].append(a)
    assert dumps(a) == expected


def test_cyclic_array_nosharing():
    """Test that serializing a cyclic structure w/o value sharing will blow up gracefully."""
    a = []
    a.append(a)
    exc = pytest.raises(CBOREncodeError, dumps, a, value_sharing=False)
    assert str(exc.value) == 'cyclic data structure detected but value sharing is disabled'


def test_cyclic_map():
    """Test that a dict that contains itself can be serialized with value sharing enabled."""
    expected = unhexlify('d81ca100d81d00')
    a = {}
    a[0] = a
    assert dumps(a) == expected


def test_cyclic_map_nosharing():
    """Test that serializing a cyclic structure w/o value sharing will fail gracefully."""
    a = {}
    a[0] = a
    exc = pytest.raises(CBOREncodeError, dumps, a, value_sharing=False)
    assert str(exc.value) == 'cyclic data structure detected but value sharing is disabled'


def test_unsupported_type():
    exc = pytest.raises(CBOREncodeError, dumps, lambda: None)
    assert str(exc.value) == 'cannot serialize type function'


def test_custom_encoder():
    class MyOwnType(object):
        def __init__(self, value_a, value_b):
            self.value_a = value_a
            self.value_b = value_b

        @classmethod
        def encode(cls, encoder, instance, fp):
            encoder.encode_semantic(6000, [instance.value_a, instance.value_b], fp, True)

    expected = unhexlify('d91770820663616263')
    value = MyOwnType(6, u'abc')
    assert dumps(value, encoders={MyOwnType: MyOwnType.encode}) == expected


def test_dump_to_file(tmpdir):
    path = tmpdir.join('testdata.cbor')
    with path.open('wb') as fp:
        dump([1, 10], fp)

    assert path.read_binary() == b'\xd8\x1c\x82\x01\x0a'
