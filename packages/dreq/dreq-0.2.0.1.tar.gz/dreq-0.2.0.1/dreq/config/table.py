# -*- coding: utf-8 -*-

"""
.. module:: dreq.config.table.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps a table defined within dreq2Defn.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from dreq import constants
from dreq import _utils as utils



# Map of table xml attribute names to value covertors.
_CONVERTORS = {
    'is_lab_unique': lambda v: False if v == "No" else True,
    'level': int,
    'max_occurs': int
}



class Table(object):
    """Wraps a table defined within dreq2Defn.xml.

    """
    def __init__(self, elem):
        """Instance constructor.

        :param xml.etree.Element elem: XML element declared within data request configuration.

        """
        utils.init_from_xml(self, elem, elem.keys(), _CONVERTORS)
        try:
            self.label_pythonic = constants.LABEL_MAP[self.label]
        except KeyError:
            self.label_pythonic = self.label
        self.attributes = []


    def __repr__(self):
        """Instance representation.

        """
        return self.label


    def __len__(self):
        """Returns number of attributes in managed collection.

        """
        return len(self.attributes)


    def __contains__(self, target):
        """Returns flag indicating whether an attribute of the matching name exists or not.

        """
        if target in self.attributes:
            return True
        return self[target] is not None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.attributes)


    def __getitem__(self, key):
        """Returns a child table attribute.

        """
        try:
            int(key)
        except ValueError:
            key = str(key).strip().lower()
            for attribute in self.attributes:
                if attribute.label.lower() == key:
                    return attribute
        else:
            return self.attributes[key]


    @property
    def attribute_names(self):
        """Returns set of unique attribute names.

        """
        return {i.label for i in self}


    @property
    def attribute_convertors(self):
        """Returns set of attribute value convertors.

        """
        return {i.name: i.type_python for i in self if i.type_python != list}


    @property
    def required_attributes(self):
        """Returns set of required attributes.

        """
        return [i for i in self if i.required]


    @property
    def scalar_attributes(self):
        """Returns set of scalar attributes.

        """
        return [i for i in self if i.type_python != list]
