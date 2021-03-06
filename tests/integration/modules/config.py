'''
Validate the config system
'''
# Import Salt Testing libs
from salttesting.helpers import ensure_in_syspath
ensure_in_syspath('../../')

# Import bonneville libs
import integration


class ConfigTest(integration.ModuleCase):
    '''
    Test config routines
    '''
    def test_valid_file_proto(self):
        '''
        test config.valid_file_proto
        '''
        self.assertTrue(
            self.run_function('config.valid_fileproto', ['salt://']))
        self.assertTrue(
            self.run_function('config.valid_fileproto', ['http://']))
        self.assertTrue(
            self.run_function('config.valid_fileproto', ['https://']))
        self.assertTrue(
            self.run_function('config.valid_fileproto', ['ftp://']))
        self.assertFalse(
            self.run_function('config.valid_fileproto', ['cheese://']))

    def test_backup_mode(self):
        '''
        test config.backup_mode
        '''
        self.assertEqual(
            self.run_function('config.backup_mode', ['minion']), 'minion')

    def test_manage_mode(self):
        '''
        test config.manage_mode
        '''
        # This function is generally only used with cross calls, the yaml
        # interpreter is breaking it for remote calls
        self.assertEqual(
            self.run_function('config.manage_mode', ['775']), '775')
        self.assertEqual(
            self.run_function('config.manage_mode', ['1775']), '1775')
        #self.assertEqual(
        #    self.run_function('config.manage_mode', ['0775']), '775')

    def test_option(self):
        '''
        test config.option
        '''
        # Minion opt
        self.assertEqual(
                self.run_function(
                    'config.option',
                    ['master_port']),
                64506)
        # Master conf opt
        self.assertEqual(
                self.run_function(
                    'config.option',
                    ['syndic_master']),
                'localhost')
        # pillar conf opt
        self.assertEqual(
                self.run_function(
                    'config.option',
                    ['ext_spam']),
                'eggs')

    def test_get(self):
        '''
        Test option.get
        '''
        # Check pillar get
        self.assertEqual(
                self.run_function(
                    'config.get',
                    ['level1:level2']),
                'foo')
        # Check master config
        self.assertEqual(
                self.run_function(
                    'config.get',
                    ['config_opt:layer2']),
                'kosher')
        # Check minion config
        self.assertEqual(
                self.run_function(
                    'config.get',
                    ['config_test:spam']),
                'eggs')


if __name__ == '__main__':
    from integration import run_tests
    run_tests(ConfigTest)
