# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Volumes/LaCie/python/snake'],
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
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='/Users/erikzenkov/Desktop/snake.icns')
app = BUNDLE(exe,
             name='main.app',
             icon='/Users/erikzenkov/Desktop/snake.icns',
             bundle_identifier=None)
