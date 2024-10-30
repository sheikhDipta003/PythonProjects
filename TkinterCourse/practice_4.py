d1 = {1: {"img": "Text&Images/1.jpg", "text": "Text&Images/1.txt"},
      2: {"img": "Text&Images/2.jpg", "text": "Text&Images/2.txt"},
      3: {"img": "Text&Images/3.jpg", "text": "Text&Images/3.txt"},
      4: {"img": "Text&Images/4.jpg", "text": "Text&Images/4.txt"},
      5: {"img": "Text&Images/5.jpg", "text": "Text&Images/5.txt"},
      }

f = open(d1[1]["text"], "rt")
content = f.read()
print(content)
