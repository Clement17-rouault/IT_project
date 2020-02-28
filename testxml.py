import lxml
from lxml import etree
#import question_de_base_Update

tree = etree.parse("test.xml")
for user in tree.xpath("/users/user/nom"):
    print(user.text)


