from PyInstaller.__main__ import run

opts = [
    'interfazCapturarPantalla.py',
    '--onefile',
    '--windowed',
    '--name=lolonCaptura',
    '--clean',
    '--noupx',
    '--strip',
    '--exclude-module=matplotlib',
    '--exclude-module=numpy',
    '--exclude-module=PIL',
    '--exclude-module=pandas',
]
run(opts)
