# Download https://raw.githubusercontent.com/jakubcerveny/gilbert/master/gilbert2d.py and store in gilbert2d.py
import urllib.request

with urllib.request.urlopen(
    "https://raw.githubusercontent.com/jakubcerveny/gilbert/master/gilbert2d.py"
) as response, open("gilbert2d.py", "wb") as out_file:
    out_file.write(response.read())

# https://raw.githubusercontent.com/jakubcerveny/gilbert/master/gilbert3d.py
import urllib.request

with urllib.request.urlopen(
    "https://raw.githubusercontent.com/jakubcerveny/gilbert/master/gilbert3d.py"
) as response, open("gilbert3d.py", "wb") as out_file:
    out_file.write(response.read())
