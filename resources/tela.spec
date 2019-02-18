# -*- mode: python -*-

block_cipher = None

a = Analysis(['..\\src\\tela.py'],
             pathex=['D:\\Mateus\\Mega\\Python\\util\\cripto'],
             binaries=[],
             datas=[('D:\\Mateus\\Mega\\Python\\util\\filechoser\\fileman.py', '.'),
                    ('D:\\Mateus\\Mega\\Python\\util\\tkpop\\avisos.py', '.')],
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
