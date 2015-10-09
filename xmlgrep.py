#!/usr/bin/python

#
# Website:
#      https://github.com/wo3kie/xmlgrep
#
# Author:
#      Lukasz Czerwinski
#
# Usage:
#     $ cat xml.xml 
#     <?xml version="1.0"?>
#     <messages>
#       <note ID="501">
#         <to>Tove</to>
#       </note>
#     </messages>
#     
#     $ ./xmlgrep.py xml.xml "messages"
#     name(/messages)
#    
#     $ ./xmlgrep.py xml.xml "note"
#     name(/messages/note)
#    
#     $ ./xmlgrep.py xml.xml "ID"
#     name(/messages/note/@ID)
#     
#     $ ./xmlgrep.py xml.xml "501"
#     string(/messages[1]/note[1]/@ID)
#    
#     $ ./xmlgrep.py xml.xml "to"
#     name(/messages/note/to)
#    
#     $ ./xmlgrep.py xml.xml "Tove"
#     string(/messages[1]/note[1]/to[1])
# 

import re
import sys
import xml.sax

class Node:
    def __init__(self, name, parent):
        self.dict = dict();
        self.name = name
        self.parent = parent
        self.counter = 0

class Backtrace:
    def __init__(self):
        self.node = None

    def getOrCreate(self, name):
        if name not in self.node.dict:
            self.node.dict[name] = Node(name, self.node)

        return self.node.dict[name]

    def startElement(self, name):
        if self.node == None:
            self.node = Node(name, None)
        else:
            self.node = self.getOrCreate(name)

        self.node.counter += 1

    def endElement(self, name):
        for (name, node) in self.node.dict.items():
            node.counter = 0

        self.node = self.node.parent

    def getPath(self):
        path = ""
        node = self.node

        while node is not None:
            path = node.name + "/" + path
            node = node.parent

        return "/" + path[0:-1]
    
    def getFullPath(self):
        path = ""
        node = self.node

        while node is not None:
            path = node.name + "[" + str(node.counter) + "]" + "/" + path
            node = node.parent

        return "/" + path[0:-1]

class XmlHandler(xml.sax.ContentHandler):
    def __init__(self, regex):
        self.regex = regex
        self.result = set()
        self.backtrace = Backtrace()

    def startElement(self, name, attrs):
        self.backtrace.startElement(name)

        if re.match(self.regex, name):
            self.result.add("name(" + self.backtrace.getPath() + ")")

        for (n, v) in attrs.items():
            if re.match(self.regex, n):
                self.result.add("name(" + self.backtrace.getPath() + "/@" + n + ")")

            if re.match(self.regex, v):
                self.result.add("string(" + self.backtrace.getFullPath() + "/@" + n + ")")

    def endElement(self, name):
        self.backtrace.endElement(name)

    def characters(self, content):
        if len(content.strip()) == 0:
            return

        if re.match(self.regex, content):
            self.result.add("string(" + self.backtrace.getFullPath() + ")")

    def getResult(self):
        return self.result

def main():
    handler = XmlHandler(sys.argv[2])
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(open(sys.argv[1], "r"))

    for i in handler.getResult():
        print i

main()

