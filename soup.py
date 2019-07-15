from bs4 import BeautifulSoup

html_doc = """
<html>
   <head>
     <title>Hello World</title>
   </head>
   <body>
      <p>Michael is the best cook in the world</p>
   </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.pasrser')


soup.title
soup.title.text
