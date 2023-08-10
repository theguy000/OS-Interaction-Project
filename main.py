#check what os it is
import os

os_name = os.name

if os_name == "nt":
    import win
else:
    import linux