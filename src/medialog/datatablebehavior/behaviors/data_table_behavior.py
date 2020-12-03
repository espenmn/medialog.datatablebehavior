# -*- coding: utf-8 -*-

from plone import api
from medialog.datatablebehavior import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
#from plone.autoform.directives import widget
from plone.autoform import directives
from plone.supermodel.directives import fieldset
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface

from plone.namedfile.field import NamedBlobFile


from medialog.datatablebehavior.widgets.widget import DataTableFieldWidget


#for the csv import
import StringIO
import csv
from plone.namedfile.field import NamedFile
from plone.i18n.normalizer import idnormalizer


class IDataTableBehaviorMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IDataTableBehavior(model.Schema):
    """
    """

    #fieldset('Settings',
    #    fields=['pagelenght',
    #            'pagelenghts',
    #            'table']
    #)

    csv_file = NamedFile(
        title=_(u"Please upload CSV file"),
        required=True,
    )

    #pagelenght = schema.Int(
    #    title=_(u'Page Length'),
    #    default=25,
    #    min=5,
    #)

    #pagelenghts = schema.Text(
    #    title=_(u'Page Length'),
    #
    #)

    directives.widget(table=DataTableFieldWidget)
    #directives.mode(table='hidden')
    table = schema.TextLine(
        title=_(u"List items"),
        required=False,
    )


@implementer(IDataTableBehavior)
@adapter(IDataTableBehaviorMarker)
class DataTableBehavior(object):
    def __init__(self, context):
        self.context = context

    @property
    def csv_file(self):
        if hasattr(self.context, 'csv_file'):
            return self.context.csv_file
        return None

    @csv_file.setter
    def csv_file(self, value):
        self.context.table = self.to_dict(value)   
        self.context.csv_file = value


    #@property
    #def pagelenght(self):
    #    if hasattr(self.context, 'pagelenght'):
    #        return self.context.pagelenght
    #    return None

    #@pagelenght.setter
    #def pagelenght(self, value):
    #    self.context.pagelenght = value


    #@property
    #def pagelenghts(self):
    #    if hasattr(self.context, 'pagelenghts'):
    #        return self.context.pagelenghts
    #    return None

    #@pagelenghts.setter
    #def pagelenghts(self, value):
    #    self.context.pagelenghts = value

    def pagelenght(self):
        return api.portal.get_registry_record('medialog.datatablebehavior.interfaces.ITableBehaviorSettings.page_size')

    def page_sizes(self):
        return api.portal.get_registry_record('medialog.datatablebehavior.interfaces.ITableBehaviorSettings.page_sizes')

    def delimeter(self):
        return api.portal.get_registry_record('medialog.datatablebehavior.interfaces.ITableBehaviorSettings.delimeter').encode('ascii','ignore')

    @property
    def table(self):
        if hasattr(self.context, 'table'):
            return self.context.table
        return None

    @table.setter
    def table(self, value):
        self.context.table = self.to_dict(self.context.csv_file.data)



    def to_dict(self, value):
        #remove this check or make a better one

        table = []
        #data=value


        csv_dict_reader = csv.DictReader(
            StringIO.StringIO(value),
            delimiter=api.portal.get_registry_record('medialog.datatablebehavior.interfaces.ITableBehaviorSettings.delimeter').encode('ascii','ignore'),
            dialect='excel',
            quotechar='"'
        )

        self.context.tableheader = csv_dict_reader.fieldnames

        for row in csv_dict_reader:
            table.append(row)


        return table
