#file automation
from pathlib import Path

import os
file_path =os.path.join(os.path.expanduser("~"),"Doownloads","report.pdf")


#new way
file_path = Path.home()/ "Downlaods"/ "format.pdf"