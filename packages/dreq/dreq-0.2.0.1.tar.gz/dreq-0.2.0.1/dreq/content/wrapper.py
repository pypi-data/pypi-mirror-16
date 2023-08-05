# -*- coding: utf-8 -*-

"""
.. module:: dreq.content.wrapper.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps dreq.xml.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from dreq.content.section import Section
from dreq.content.section_item import SectionItem



class Wrapper(object):
    """Wraps dreq.xml.

    """
    def __init__(self, sections):
        """Instance constructor.

        :param list sections: Collection of content sections.

        """
        self.sections = sorted(sections, key=lambda i: i.label.lower())
        for section in sections:
            setattr(self, section.label, section)
            setattr(self, section.label_pythonic, section)


    def __len__(self):
        """Returns number of sections in managed collection.

        """
        return len(self.sections)


    def __contains__(self, key):
        """Returns flag indicating whether a certain section exists or not.

        """
        if key in self.sections:
            return True
        return self[key] is not None


    def __iter__(self):
        """Instance iterator initializer.

        """
        return iter(self.sections)


    def __getitem__(self, key):
        """Returns a child section.

        """
        try:
            int(key)
        except ValueError:
            key = str(key).strip().lower()
            for section in self.sections:
                if section.label.lower() == key or section.label_pythonic.lower() == key :
                    return section
        else:
            return self.sections[key]
