@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo [FluxLab] Creando entorno virtual...
    python -m venv .venv || goto :error
)

echo [FluxLab] Instalando/actualizando dependencias...
".venv\Scripts\python.exe" -m pip install --upgrade pip >nul
".venv\Scripts\python.exe" -m pip install -r requirements.txt || goto :error

if not exist ".venv\fluxlab_chromium_ok" (
    echo [FluxLab] Descargando navegador Chromium para Playwright (solo la primera vez)...
    ".venv\Scripts\python.exe" -m playwright install chromium || goto :error
    echo ok > ".venv\fluxlab_chromium_ok"
)

echo [FluxLab] Iniciando...
".venv\Scripts\python.exe" "FluxLab"
goto :eof

:error
echo.
echo [FluxLab] Ocurrio un error durante la preparacion. Revisa el mensaje de arriba.
pause
