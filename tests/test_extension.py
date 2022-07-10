import time
import unittest

import mock

from mopidy_waitforinternet import WaitForInternetExtension


class WaitForInternetExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = WaitForInternetExtension()

        config = ext.get_default_config()

        self.assertIn('[waitforinternet]', config)
        self.assertIn('enabled = true', config)

    def test_setup_realrun(self):
        registry = mock.Mock()

        ext = WaitForInternetExtension()
        t_start = time.monotonic()
        ext.setup(registry)
        t_stop = time.monotonic()

        registry.add.assert_not_called()
        self.assertGreater(t_stop - t_start, 0)
        self.assertLess(t_stop - t_start, 5)
