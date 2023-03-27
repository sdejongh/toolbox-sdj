import unittest
from toolbox_sdj.regex_patterns import network
from toolbox_sdj.regex_patterns import commercial
from toolbox_sdj.regex_patterns import hash
from toolbox_sdj.regex_patterns import numbers
from toolbox_sdj.regex_patterns import internet


class TestRegexPatterns(unittest.TestCase):
    def test_network_ipv4_address(self):
        self.assertRegex('192.168.0.1', network.IPV4_ADDRESS)
        self.assertNotRegex('392.168.0.1', network.IPV4_ADDRESS)
        self.assertRegex('255.255.255.0', network.IPV4_ADDRESS)

    def test_network_ipv6_address(self):
        self.assertRegex('FF02::1', network.IPV6_ADDRESS)
        self.assertNotRegex('2001:ABCD:123', network.IPV6_ADDRESS)
        self.assertRegex('2a02:CAFE:BEEF::1', network.IPV6_ADDRESS)

    def test_commercial_isbn10(self):
        self.assertRegex('2-7654-0912-9', commercial.ISBN10)

    def test_commercial_isbn13(self):
        self.assertRegex('978-2-212-67995-3', commercial.ISBN13)

    def test_hash_md5(self):
        self.assertRegex('5d41402abc4b2a76b9719d911017c592', hash.MD5_HASH)

    def test_hash_sha1(self):
        self.assertRegex('aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d', hash.SHA1_HASH)

    def test_hash_sha256(self):
        self.assertRegex('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', hash.SHA256_HASH)

    def test_numbers_integer_signed(self):
        self.assertRegex('95', numbers.INTEGER_SIGNED)
        self.assertRegex('+95', numbers.INTEGER_SIGNED)
        self.assertRegex('-95', numbers.INTEGER_SIGNED)
        self.assertNotRegex('9.5', numbers.INTEGER_SIGNED)
        self.assertNotRegex('+9.5', numbers.INTEGER_SIGNED)
        self.assertNotRegex('-9.5', numbers.INTEGER_SIGNED)

    def test_numbers_float_signed(self):
        self.assertRegex('95.', numbers.FLOAT_SIGNED)
        self.assertRegex('+95.', numbers.FLOAT_SIGNED)
        self.assertRegex('-95.', numbers.FLOAT_SIGNED)
        self.assertRegex('095.567', numbers.FLOAT_SIGNED)
        self.assertRegex('+095.567', numbers.FLOAT_SIGNED)
        self.assertRegex('-095.567', numbers.FLOAT_SIGNED)
        self.assertRegex('.5', numbers.FLOAT_SIGNED)
        self.assertRegex('+.5', numbers.FLOAT_SIGNED)
        self.assertRegex('-.5', numbers.FLOAT_SIGNED)
        self.assertNotRegex('9', numbers.FLOAT_SIGNED)
        self.assertNotRegex('+9', numbers.FLOAT_SIGNED)
        self.assertNotRegex('-9', numbers.FLOAT_SIGNED)

    def test_internet_email(self):
        self.assertRegex('jdoe@domain.com', internet.EMAIL)
        self.assertRegex('john.doe@domain.com', internet.EMAIL)
        self.assertRegex('john_doe@dom-ain.com', internet.EMAIL)
        self.assertNotRegex('_doe@domain.com', internet.EMAIL)
        self.assertNotRegex('john_doe@domain', internet.EMAIL)

    def test_internet_domain(self):
        self.assertRegex('www.domain.com', internet.DOMAIN)
        self.assertRegex('domain.com', internet.DOMAIN)
        self.assertRegex('su-b.www.dom-ain.com', internet.DOMAIN)


if __name__ == '__main__':
    unittest.main()