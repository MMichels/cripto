# -*- mode: python -*-
import os

FILECHOSER_PATH = os.path.abspath('../../filechoser/fileman.py')  # Subistituir pelo diretorio da dependencia filechoser
TKPOP_PATH = os.path.abspath('../../tkpop/avisos.py')  # Subistituir pelo diretorio da dependencia tkpop
block_cipher = None

a = Analysis(['../src/tela.py'],
             pathex=['../'],
             binaries=[],
             datas=[(FILECHOSER_PATH, '.'),
                    (TKPOP_PATH, '.')],
             hiddenimports=['cryptography', 'tkinter.filedialog', 'mysql', 'psycopg2'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='tela',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='tela')
