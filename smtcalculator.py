from cx_Freeze import *
includefiles = ['icon.ico']
base = None
# if sys.platform == "win32":
#     base ="Win32GUI"
shortcut_table = [
    ("DesktopShortcut",     #shortcut
     "DesktopFolder",       #Directory_
     "My Calculator",       #Name
     "TARGTDIR",            #component_
     "[TARGTDIR]\main.exe",  #Target
     None,                  #Arguments
     None,                  #Discription
     None,                  #Hotkey
     None,                  #Icon
     None,                  #Iconindex
     None,                  #ShowCmd
     "TARGTDIR",            #WKDir
    )
]
mis_data = { "Shortcut": shortcut_table }
bdist_msi_options = { 'data' : mis_data }
setup(
    version="0.1",
    description = "My Calculator",
    author = "COSEC TEAM A",
    name = "My Calculator",
    options = { 'build.exe': { 'include_files' : includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico',
        )
    ]
)