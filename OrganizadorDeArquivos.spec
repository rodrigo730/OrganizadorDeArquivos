# -*- mode: python ; coding: utf-8 -*-

import os

FILES_DIR = os.path.join(SPECPATH, 'Gui', 'files')
ROOT_DIR = SPECPATH

a = Analysis(
    ['Gui\\src\\main.py'],
    pathex=[os.path.join(SPECPATH, 'Gui', 'src'),
    SPECPATH,],
    binaries=[],
    datas=[('Gui/files', 'files')],
    hiddenimports=['mover_arquivos'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='OrganizadorDeArquivos',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['Gui/files/python-logo-only.png'],
)
