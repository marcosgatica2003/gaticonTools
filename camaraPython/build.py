from PyInstaller.__main__ import run

opts = [
    'camaraOpenCvBasico.py',
    '--onefile',
    '--windowed',
    '--name=lolonCamaraDeFotos',
    '--clean',
    '--noupx',
    '--strip',
    '--exclude-module=matplotlib',
    '--exclude-module=PIL',
    '--exclude-module=pandas',
]
run(opts)
