import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text

from plone import api


class IDataTableWidget(interfaces.IWidget):
    """DataTable widget."""


@zope.interface.implementer_only(IDataTableWidget)
class DataTableWidget(text.TextWidget):
    """DataTable Widget"""



    def plone5(self):
        try:
            from Products.CMFPlone.factory import _IMREALLYPLONE5
            return 1
        except ImportError:
            return 0

    def page_sizes(self):
        return api.portal.get_registry_record('medialog.datatablebehavior.interfaces.ITableBehaviorSettings.page_sizes')


    def page_sizes_names(self):
        page_names = []
        for size in self.page_sizes():
            page_names.append(size['menu_name'])
        return page_names

    def page_sizes_values(self):
        page_values = []
        for size in self.page_sizes():
            page_values.append(size['pagesize'])
        return page_values




@zope.interface.implementer(interfaces.IFieldWidget)
def DataTableFieldWidget(field, request):
    """IFieldWidget factory for DataTableWidget."""

    #if api.user.is_anonymous:
    #    # enable datatables for anonymous users
    #    from Products.CMFPlone.resources import add_bundle_on_request
    #    add_bundle_on_request(self.request, 'plone-datatables')
    return widget.FieldWidget(field, DataTableWidget(request))
