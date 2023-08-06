# -*- coding: utf-8 -*-

from __future__ import unicode_literals

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import unittest
import logging
import os
import tempfile
from contextlib import contextmanager

import six

import react
from react import utils


logging.disable(logging.CRITICAL)

_global = '__global'


@contextmanager
def js_file(data):
    if isinstance(data, six.text_type):
        data = data.encode('utf-8')

    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(data)
    temp.close()

    try:
        yield temp.name
    finally:
        os.remove(temp.name)


class UtilsTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_up(self):
        """
        It should call shortcut.setup
        """
        # set_up has been called for the test suite
        # (see runtests) so there is not much that
        # can be tested
        with patch('react.utils.shortcuts.set_up', autospec=True) as s:
            utils.set_up()
            s.assert_called_once_with()

    def test_run_script(self):
        """
        It should run the script file content on V8
        """
        script = 'var %s = {foo: "foo"};' % _global

        utils.run_script(script)
        self.assertEqual('foo', utils.run_script('%s.foo' % _global))

        # Cleanup
        self.assertEqual('true', utils.run_script('delete %s.foo' % _global))

    def test_run_script_exception(self):
        """
        It should propagate V8 exceptions
        """
        script = 'fooUndefined()'
        self.assertRaises(react.excepts.V8Error, utils.run_script, script)

    def test_load_libs(self):
        """
        It should load the lib into the V8 context
        """
        script = 'var %s = {foo: "foo"};' % _global

        with js_file(script) as path:
            utils.load_libs([path])

        self.assertEqual('foo', utils.run_script('%s.foo' % _global))
        self.assertEqual('true', utils.run_script('delete %s.foo' % _global))
