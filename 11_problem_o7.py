i=1
content=True
with open("log.txt") as f:
   while content:
    content=f.readline()
    if 'python ' in content.lower():
      print(content)
      print(f"Yes python is present on line number {i}")
    i+=1


