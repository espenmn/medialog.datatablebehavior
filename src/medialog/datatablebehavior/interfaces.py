# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from z3c.form import interfaces
from zope import schema
#from plone.autoform.directives import form
from zope.interface import alsoProvides
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from plone.registry import field
from persistent import Persistent
#from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform.directives import widget




from collective.z3cform.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow

from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.datatablebehavior')

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IMedialogDatatablebehaviorLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IPageSizePair(model.Schema):
    menu_name = schema.ASCIILine(
        title=_(u'name', 'Name'),
        required=False,
    )

    pagesize = schema.Int(
        title=_(u'pagesize', 'Page Size'),
        required=False,
    )




class ITableBehaviorSettings(model.Schema):
    """Adds settings to medialog.controlpanel """

    fieldset(
        'extra',
        label=_(u'Datatable'),
        fields=[
            'page_size',
            'page_sizes',
            'delimeter',
            ],
    )

    page_size = schema.Int(
        title=_(u'Default Page Length'),
        default=25,
        min=5,
    )

    widget(page_sizes=DataGridFieldFactory)
    page_sizes = schema.List(
        title = _(u"Page sizes"),
        value_type=DictRow(schema=IPageSizePair),
    )

    delimeter = schema.ASCIILine(
        title=_(u'Delimiter'),
        default=';',
        required = True,
    )

alsoProvides(ITableBehaviorSettings, IMedialogControlpanelSettingsProvider)
