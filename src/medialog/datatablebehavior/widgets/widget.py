import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text

#from plone import api







class IDataTableWidget(interfaces.IWidget):
    """DataTable widget."""


@zope.interface.implementer_only(IDataTableWidget)
class DataTableWidget(text.TextWidget):
    """DataTable Widget"""


@zope.interface.implementer(interfaces.IFieldWidget)
def DataTableFieldWidget(field, request):
    """IFieldWidget factory for DataTableWidget."""

    #if api.user.is_anonymous:
    #    # enable datatables for anonymous users
    #    from Products.CMFPlone.resources import add_bundle_on_request
    #    add_bundle_on_request(self.request, 'plone-datatables')
    return widget.FieldWidget(field, DataTableWidget(request))
