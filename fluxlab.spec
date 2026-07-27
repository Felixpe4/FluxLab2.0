# -*- mode: python ; coding: utf-8 -*-
"""
Spec de PyInstaller para FluxLab — genera un .exe autocontenido (no requiere
Python instalado en la PC destino).

Uso:  pyinstaller fluxlab.spec    (o simplemente correr compilar.bat)
"""
import pathlib
import sys
import customtkinter
import playwright

BASE_DIR = pathlib.Path(SPECPATH)
CTK_DIR  = pathlib.Path(customtkinter.__file__).parent
PW_DIR   = pathlib.Path(playwright.__file__).parent
PYTHON_DIR = pathlib.Path(sys.base_prefix)
TCL_DIR = PYTHON_DIR / "tcl"
DLLS_DIR = PYTHON_DIR / "DLLs"
TKINTER_DIR = PYTHON_DIR / "Lib" / "tkinter"

# CustomTkinter carga sus temas/assets como archivos sueltos en tiempo de
# ejecución — hay que incluir la carpeta completa para que el .exe los encuentre.
#
# El paquete de playwright incluye, además del driver, el navegador Chromium
# que `compilar.bat` descarga ahí mismo (PLAYWRIGHT_BROWSERS_PATH=0) — al
# incluir toda la carpeta, el .exe queda con el navegador ya integrado y no
# necesita descargarlo en la PC destino.
datas = [
    (str(CTK_DIR), "customtkinter"),
    (str(PW_DIR), "playwright"),
]

# Tkinter se incluye de forma explícita. En algunas instalaciones de Python,
# PyInstaller no consigue inicializar Tcl durante el análisis y excluye
# tkinter aunque los archivos sí estén instalados. El ejecutable resultante
# fallaría al arrancar con "No module named tkinter".
for origen, destino in [
    (TCL_DIR / "tcl8.6", "_tcl_data"),
    (TCL_DIR / "tk8.6", "_tk_data"),
    # Se agrega también como datos porque el hook estándar de PyInstaller
    # puede excluir el módulo al no poder inicializar Tcl en la PC de build.
    (TKINTER_DIR, "tkinter"),
]:
    if origen.exists():
        datas.append((str(origen), destino))

tk_binaries = [
    DLLS_DIR / "_tkinter.pyd",
    DLLS_DIR / "tcl86t.dll",
    DLLS_DIR / "tk86t.dll",
]
binaries_tk = [(str(archivo), ".") for archivo in tk_binaries if archivo.exists()]

logo = BASE_DIR / "logo_fluxlab.png"
if logo.exists():
    datas.append((str(logo), "."))

# Icono del .exe / accesos directos de Windows — generado con la misma
# identidad visual que el logo dentro de la app (ver logo_fluxlab.png).
icono = BASE_DIR / "logo_fluxlab.ico"
ICON_PATH = str(icono) if icono.exists() else None

a = Analysis(
    [str(BASE_DIR / "FluxLab")],
    pathex=[str(BASE_DIR)],
    binaries=binaries_tk,
    datas=datas,
    hiddenimports=[
        "customtkinter",
        "tkinter",
        "tkinter.ttk",
        "tkinter.font",
        "tkinter.messagebox",
        "tkinter.filedialog",
        "PIL._tkinter_finder",
        "anthropic",
        "playwright",
        "playwright.sync_api",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[str(BASE_DIR / "runtime_tkinter.py")],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="FluxLab",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=ICON_PATH,
)
