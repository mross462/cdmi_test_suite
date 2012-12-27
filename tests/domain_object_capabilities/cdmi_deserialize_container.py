#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from . import CDMICapabilitiesTestCase

import unittest2 as unittest


class testcase(CDMICapabilitiesTestCase):

    def setUp(self):
        super(testcase, self).setUp()

        self.exists = False
        try:
            self.exists = self.system_wide_capabilities.get('banana')
        except KeyError:
            pass
        try:
            self.exists = self.storage_system_capabilities.get('banana')
        except KeyError:
            pass
        try:
            self.exists = self.data_system_capabilites.get('banana')
        except KeyError:
            pass
        try:
            self.exists = self.data_object_capabilies.get('banana')
        except KeyError:
            pass
        try:
            self.exists = self.container_object_capabilies.get('banana')
        except KeyError:
            pass
        try:
            self.exists = self.domain_object_capabilities.get('banana')
        except KeyError:
            pass
        try:
            self.exists = self.queue_object_capabilities.get('banana')
        except KeyError:
            pass

    def tearDown(self):
        print 'Test Completed'

    '''
    If the cdmi_capability is found and true run a positive test
    '''
    @unittest.skipIf(not exists, 'Capability Not Found, Skipping')
    def testPositive(self):
        print 'Test Started'

    '''
    If the cdmi_capability is not found or set to false run a negative test
    '''
    @unittest.skipUnless(exists)
    def testPositive(self):
        print 'Test Started'
