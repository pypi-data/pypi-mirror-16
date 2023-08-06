# -*- mode: python -*-
import os
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal,\
        hookspath, runtime_hooks

import importlib.machinery
sysfont = importlib.machinery\
        .SourceFileLoader('sysfont', os.getcwd() + '/music_sampler/sysfont.py') \
        .load_module()

excluded_and_hidden_modules = get_deps_minimal(
        video=None,
        camera=None,
        audio=None,
        clipboard=None,
        spelling=None)

excluded_and_hidden_modules['hiddenimports'] += [
        'six',
        'packaging',
        'packaging.version',
        'packaging.specifiers',
        'packaging.requirements' ]

commit_message = os.popen('git log -1 --format="%h  %ci"').read()
pyinstaller_file = open(".pyinstaller_commit", "w")
pyinstaller_file.write(commit_message)
pyinstaller_file.close()

data = [
  ('music_sampler/music_sampler.kv', '.'),
  ('.pyinstaller_commit', '.')
]

a = Analysis(['run.py'],
             binaries=None,
             datas=data,
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             **excluded_and_hidden_modules)

for fontname, style in [("Ubuntu", sysfont.STYLE_NORMAL), ("Ubuntu", sysfont.STYLE_BOLD), ("Symbola", sysfont.STYLE_NONE)]:
    font = sysfont.get_font(fontname, style=style)
    a.datas.append((
        'fonts/{}_{}.ttf'.format(fontname, style),
        font[4],
        'DATA'
        ))

pyz = PYZ(a.pure, a.zipped_data)

# Single file
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
        name='music_sampler')

# Directory
# exe = EXE(pyz, a.scripts,
#     exclude_binaries=True,
#     name='music_sampler_dir',
#     debug=False,
#     strip=False,
#     upx=True,
#     console=True)
# coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas,
#     strip=False,
#     upx=True,
#     name='music_sampler_dir')
