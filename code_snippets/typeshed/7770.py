import xml.etree.ElementTree as ET

tree = ET.ElementTree()
print(tree.getroot()) # prints None

class ElementTree:
    def __init__(self, element=None, file=None):
        # assert element is None or iselement(element)
        self._root = element # first node
        if file:
            self.parse(file)

    def getroot(self):
        """Return root element of this tree."""
        return self._root
