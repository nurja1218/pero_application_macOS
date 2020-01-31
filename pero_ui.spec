# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pero_ui.py'],
             pathex=['/Users/kimjungmo/PycharmProjects/pero_application'],
             binaries=[],
             datas=[('./setting/img/palmcat_title.png', 'data')],
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
          [],
          exclude_binaries=True,
          name='pero_ui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pero_ui')
app = BUNDLE(coll,
             name='pero_ui.app',
             icon=None,
             bundle_identifier=None)
