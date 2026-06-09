@echo off
setlocal
cd /d "%~dp0"

if not exist "build_venv\Scripts\python.exe" (
    echo [FluxLab] Creando entorno de compilacion con Python 3.12...
    rem Se fija la version 3.12 a proposito: PyInstaller no empaqueta bien
    rem los modulos compilados de Pillow (_imaging) en Python 3.14, lo que
    rem provoca "cannot import name '_imaging' from 'PIL'" al abrir el .exe
    rem en otras PCs. 3.12 es la version estable mejor soportada por PyInstaller.
    py -3.12 -m venv build_venv || goto :error
)

echo [FluxLab] Instalando dependencias y PyInstaller...
"build_venv\Scripts\python.exe" -m pip install --upgrade pip >nul
"build_venv\Scripts\python.exe" -m pip install -r requirements.txt pyinstaller || goto :error

rem PLAYWRIGHT_BROWSERS_PATH=0 hace que el navegador se descargue DENTRO del
rem paquete de playwright, para poder incluirlo en el .exe (ver fluxlab.spec)
echo [FluxLab] Descargando Chromium para incluirlo en el ejecutable...
set "PLAYWRIGHT_BROWSERS_PATH=0"
"build_venv\Scripts\python.exe" -m playwright install chromium || goto :error

echo [FluxLab] Generando ejecutable (esto puede tardar varios minutos)...
"build_venv\Scripts\python.exe" -m PyInstaller --noconfirm fluxlab.spec || goto :error

echo.
echo [FluxLab] Listo. El ejecutable quedo en dist\FluxLab.exe
echo Copia ese .exe a la carpeta donde lo vayas a instalar (junto con logo_fluxlab.png si lo usas).
echo Al primer arranque, FluxLab pedira su propia configuracion en esa PC
echo (API key, credenciales del portal, usuario interno) - el navegador ya viene incluido.
pause
goto :eof

:error
echo.
echo [FluxLab] La compilacion fallo. Revisa el mensaje de arriba.
pause
