#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node
# that have name attributes, the third node should be Panama.
#

import xml.etree.cElementTree as ET

root = ET.Element("root")
ET.SubElement(root, "country", name="Wakanda")
ET.SubElement(root, "country", name="Shieldfrieden")
ET.SubElement(root, "country", name="Panama")
tree = ET.ElementTree(root)
tree.write("/tmp/vulnerable-countries.xml")