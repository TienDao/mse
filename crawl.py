import urllib.request
import xml.etree.ElementTree as ET

f = urllib.request.urlopen("http://localhost:5000/export_xml")
text = f.read()
text = text.decode("utf8")
f.close()

tree = ET.fromstring(text)

lst = tree.findall('student')
print("User count: ", len(lst))
for item in lst:
    print("Student:", item.find('name').text)
    print("- Email: ", item.find('email').text)
    print("- Birthday: ", item.find('birthday').text)
    print("- Address: ", item.find('address').text)
    print("- Store: ", item.find('score').text)
    print("------------------------------")
