import pandas as pd
import xml.etree.ElementTree as et

# xml_file = open("./resources/import.xml","w+")

xtree = et.parse("./resources/import.xml")

xroot = xtree.getroot()


for node in xroot:
    s_name = node.attrib.get("name")
    s_mail = node.find("email").text
    s_grade = node.find("grade").text
    s_age = node.find("age").text

print (s_mail)

