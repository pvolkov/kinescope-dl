# -*- mode: python ; coding: utf-8 -*-


import os
from os import environ

block_cipher = None

ffmpeg_path = 'bin/ffmpeg.exe'
mp4decrypt_path = 'bin/mp4decrypt.exe'

if not (os.path.exists(ffmpeg_path) and os.path.exists(mp4decrypt_path)):
    raise Exception('FFMPEG_PATH or MP4DECRYPT_PATH files are not found in bin folder')

a = Analysis(
    ['kinescope-dl.py'],
    pathex=[],
    binaries=[(ffmpeg_path, '.'), (mp4decrypt_path, '.')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='kinescope-dl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='NONE',
)
