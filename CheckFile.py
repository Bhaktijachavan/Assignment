from importlib.resources import path
import os
from unittest.mock import patch
filepaths = ["C:\Bhaktija\MCA\Python\package.json","C:\Bhaktija\MCA\CheckFile\First_PDF.pdf"]
for fp in filepaths:
      ext = os.path.splitext(fp)[-1].lower()
if ext == ".json":
      print (fp,"is an json file")
elif ext == ".pdf":
      print (fp,"is an pdf file")
else:
      print (fp,"unknow file fromat")