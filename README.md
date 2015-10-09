# xmlgrep  
Find a given text return it position in xml as an XPath  
  
## website  
https://github.com/wo3kie/xmlgrep  
  
## license  
For license please refer to LICENSE file  
  
## requirements  
python  
  
## how to use it  
```xml
$ cat xml.xml ``  
<?xml version="1.0"?>``  
<messages>``  
  <note ID="501">``  
    <to>Tove</to>``  
    <from>Jani</from>``  
    <heading>Reminder</heading>``  
    <body>Don't forget me this weekend!</body>``  
  </note>``  
  <note ID="502">``  
    <to>Jani</to>``  
    <from>Tove</from>``  
    <heading>Re: Reminder</heading>``  
    <body>I will not!</body>``  
  </note> ``  
</messages>``  
```

``$ ./xmlgrep.py xml.xml "messages"``  
``name(/messages)``  
  
``$ ./xmlgrep.py xml.xml "note"``  
``name(/messages/note)``  
  
``$ ./xmlgrep.py xml.xml "ID"``  
``name(/messages/note/@ID)``  
  
``$ ./xmlgrep.py xml.xml "501"``  
``string(/messages[1]/note[1]/@ID)``  
  
``$ ./xmlgrep.py xml.xml "to"``  
``name(/messages/note/to)``  
  
``$ ./xmlgrep.py xml.xml "Tove"``  
``string(/messages[1]/note[2]/from[1])``  
``string(/messages[1]/note[1]/to[1])``  
  
``$ ./xmlgrep.py xml.xml "from"``  
``name(/messages/note/from)``  
  
``$ ./xmlgrep.py xml.xml "Jani"``  
``string(/messages[1]/note[2]/to[1])``  
``string(/messages[1]/note[1]/from[1])``  
  
``$ ./xmlgrep.py xml.xml "heading"``  
``name(/messages/note/heading)``  
  
``$ ./xmlgrep.py xml.xml "Reminder"``  
``string(/messages[1]/note[1]/heading[1])``  
  
``$ ./xmlgrep.py xml.xml "Don't"``  
``string(/messages[1]/note[1]/body[1])``  
  
``$ ./xmlgrep.py xml.xml "502"``  
``string(/messages[1]/note[2]/@ID)``  
  
``$ ./xmlgrep.py xml.xml "Re: Reminder"``  
``string(/messages[1]/note[2]/heading[1])``  
  
``$ ./xmlgrep.py xml.xml "I will"``  
``string(/messages[1]/note[2]/body[1])``  
  
