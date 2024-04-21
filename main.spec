# -*- mode: python ; coding: utf-8 -*-

# https://stackoverflow.com/a/48068640/23530805

import os
import importlib
from pathlib import Path

package_imports = [
    ['inflect', ['__init__.py']],
    ['g2p_en', ['checkpoint20.npz', 'homographs.en']],
    ['discord', ['bin/libopus-0.x64.dll', 'bin/libopus-0.x86.dll']],
]

datas = []
for package, files in package_imports:
    proot = os.path.dirname(importlib.import_module(package).__file__)
    datas.extend((os.path.join(proot, f), str((Path(package)/f).parent)) for f in files)

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("lyingbard/lyingbard_tts/talkotron_model.pt", "lyingbard/lyingbard_tts"),
        ("lyingbard/lyingbard_tts/500", "lyingbard/lyingbard_tts/500"),
        ("lyingbard/lyingbard_tts/emojisound/sounds", "lyingbard/lyingbard_tts/emojisound/sounds"),
        ("lyingbard/lyingbard_tts/melgan_neurips/models/multi_speaker.pt", "lyingbard/lyingbard_tts/melgan_neurips/models"),
        ("lyingbard/favicon.ico", "lyingbard"),
    ]+datas,
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='LyingBard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FUBAI',
)
