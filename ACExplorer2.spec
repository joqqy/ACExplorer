# -*- mode: python -*-
block_cipher = None

a = Analysis(
	['ACExplorer2.py'],
	pathex=['D:\\Programs\\AC-Explorer'],
	binaries=[],
	datas=[
		('./resources', './resources'),
		('./pyUbiForge', './pyUbiForge'),
		('./icon.ico', '.')
	],
	hiddenimports=[],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher,
	noarchive=False
)

pyz = PYZ(
	a.pure,
	a.zipped_data,
	cipher=block_cipher
)

exe = EXE(
	pyz,
	a.scripts,
	[],
	exclude_binaries=True,
	name='ACExplorer',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	console=True,
	icon='icon.ico'
)

coll = COLLECT(
	exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	name='ACExplorer'
)