# -*- coding: utf-8 -*-
from medialog.datatablebehavior.behaviors.data_table_behavior import IDataTableBehaviorMarker
from medialog.datatablebehavior.testing import MEDIALOG_DATATABLEBEHAVIOR_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class DataTableBehaviorIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_DATATABLEBEHAVIOR_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_data_table_behavior(self):
        behavior = getUtility(IBehavior, 'medialog.datatablebehavior.data_table_behavior')
        self.assertEqual(
            behavior.marker,
            IDataTableBehaviorMarker,
        )
