from distutils.core import setup
import py2exe
from glob import glob
data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))] 
setup(data_files=data_files,   windows=[{'script':'smdh.py',
                'icon_resources':[(0x0004,'smdh.ico')]


                }],
      options = {"py2exe": {"skip_archive":1,
                            "dist_dir": "dist/bin",
                            #'bundle_files': 1
                            }}
      )
