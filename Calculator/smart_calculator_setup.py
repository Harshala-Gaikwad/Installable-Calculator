from cx_Freeze import *

includefiles = ['Calculator-icon.ico']
base = None
if sys.platform=="win32":
    base="win32GUI"

shortcut_table = [
    ( "DesktopShortcut", # Shortcut
      "DesktopFolder", # Directory_
      "My Calculator", # Name
      "TARGETDIR", # Component
      "[TARGETDIR]\calculator.exe", # Target
      None, # Arguments
      None, # Description
      None, # Hotkey
      None, # Icon
      None, # IconIndex
      None, # ShowCmd
      "TARGETDIR", # WKDir
     )
]
msi_data = {"Shortcut": shortcut_table}

#Change some default MSI options and specify the use of the above defined table
bdist_msi_options = {'data':msi_data}
setup(
    version="0.1",
    description="My Calculator",
    author="Harshala Gaikwad",
    name="My Calculator",
    options={'bulid_exe': {'include_files': includefiles},"bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="calculator.py",
            base=base,
            icon="Calculator-icon.ico",
        )
    ]
)
