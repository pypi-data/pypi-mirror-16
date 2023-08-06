# -*- mode: python -*-

block_cipher = None


a = Analysis(['ftpservx.py'],
             pathex=['D:\\10\\dev\\ftpservx'],
             binaries=None,
             datas=None,
             hiddenimports=['pyftpdlib', 'PyQt4', 'PySide'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ftpservx',
          debug=False,
          strip=False,
          upx=False,
          console=False , icon='folder-remote.ico')
