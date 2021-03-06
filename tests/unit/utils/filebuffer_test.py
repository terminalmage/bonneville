# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2012-2013 by the SaltStack Team, see AUTHORS for more details
    :license: Apache 2.0, see LICENSE for more details.


    tests.unit.utils.filebuffer_test
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Import Salt Testing libs
from salttesting import TestCase
from salttesting.helpers import ensure_in_syspath
ensure_in_syspath('../../')

# Import bonneville libs
from salt.utils.filebuffer import BufferedReader, InvalidFileMode


class TestFileBuffer(TestCase):
    def test_read_only_mode(self):
        with self.assertRaises(InvalidFileMode):
            BufferedReader('/tmp/foo', mode='a')

        with self.assertRaises(InvalidFileMode):
            BufferedReader('/tmp/foo', mode='ab')

        with self.assertRaises(InvalidFileMode):
            BufferedReader('/tmp/foo', mode='w')

        with self.assertRaises(InvalidFileMode):
            BufferedReader('/tmp/foo', mode='wb')


if __name__ == '__main__':
    from integration import run_tests
    run_tests(TestFileBuffer, needs_daemon=False)
