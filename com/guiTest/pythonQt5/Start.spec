# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Start.py'],
             pathex=['D:\\workspacePy4\\com\\guiTest\\pythonQt5\\QFlowLayout', 'D:\\workspacePy4\\com\\guiTest\\pythonQt5\\QFlowLayout\\otherPage', 'D:\\workspacePy4\\com\\guiTest\\pythonQt5\\source', 'D:\\workspacePy4\\com\\guiTest\\pythonQt5'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
