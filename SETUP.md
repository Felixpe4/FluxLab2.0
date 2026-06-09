# FluxLab — instalación y configuración

## Opción A: correrlo como script de Python (cualquier carpeta/PC con Python)

1. Copia toda esta carpeta donde quieras (otra PC, otra ubicación, un USB, etc.).
2. Asegúrate de tener [Python 3.10+](https://www.python.org/downloads/) instalado
   (marca la casilla "Add Python to PATH" durante la instalación).
3. Haz doble clic en `iniciar.bat`. La primera vez:
   - crea un entorno virtual (`.venv`),
   - instala las dependencias de `requirements.txt`,
   - descarga el navegador Chromium que usa Playwright (~150 MB, una sola vez),
   - y abre la app.
4. Si es la primera vez que se ejecuta en esta computadora, FluxLab te pedirá:
   - tu **API key de Anthropic** (Claude),
   - el **usuario y contraseña del portal del laboratorio**,
   - un **usuario interno** para entrar a la app (puedes dejar el sugerido).

   Esos datos se guardan en `config.json`, **junto al ejecutable, solo en esta
   computadora** — nunca se comparten ni se suben a ningún lado.

## Opción B: instalarlo como app de escritorio (.exe)

Si te entregaron un instalador o un `FluxLab.exe`:

1. Ejecuta el instalador (o copia la carpeta del `.exe` donde prefieras) — no
   necesita tener Python instalado.
2. Al abrirlo por primera vez te pedirá la misma información que en la Opción A
   (tu propia API key, credenciales del portal, usuario interno). Cada
   instalación configura las suyas: puedes repartir el mismo instalador a varias
   personas/computadoras sin compartir tus credenciales.
3. Los datos capturados (`data/`) y la configuración (`config.json`) quedan
   junto al ejecutable, así que puedes mover toda la carpeta sin perder nada.

## ¿Dónde consigo cada dato?

- **API key de Anthropic**: se genera en la consola de [Anthropic](https://console.anthropic.com/)
  (sección "API Keys"). Cada persona/instalación debería usar su propia key.
- **Usuario/contraseña del portal del laboratorio**: las credenciales que
  normalmente usas para entrar a `https://diazlab.sistematoronjalab.com/pos`.
- **Usuario interno de la app**: lo que tú definas — sirve solo para el login
  de FluxLab, no para el portal del laboratorio.

## Cambiar la configuración después

Puedes editar `config.json` directamente con un editor de texto, o borrarlo y
volver a abrir la app: te volverá a mostrar la pantalla de configuración inicial.
También puedes usar `config.example.json` como referencia del formato.

## Auto-actualización (solo para quien publica nuevas versiones)

FluxLab revisa solo, al abrir, si hay una versión más nueva publicada en
GitHub Releases; si la encuentra, pregunta al usuario si quiere instalarla y,
de aceptar, se descarga, se reinstala y se reabre sola — nadie tiene que volver
a recibir ni reinstalar el `.exe` a mano. Así quedó configurado:

1. ✅ Ya hecho: el repositorio privado `Felixpe4/FluxLab` está creado y
   conectado en el código (`GITHUB_REPO = "Felixpe4/FluxLab"`, cerca del inicio
   de `FluxLab`). No hace falta subir ahí el código fuente — solo sirve para
   publicar los `.exe` como "Releases".
2. **Publica una versión nueva** cuando hagas mejoras:
   - Sube el número de `APP_VERSION` en `FluxLab` (p. ej. de `"4.2.0"` a `"4.3.0"`).
   - Compila el `.exe` con `compilar.bat`.
   - En GitHub, entra a tu repositorio → **Releases** → **Draft a new release**.
   - En "Tag" escribe la misma versión con `v` adelante (p. ej. `v4.3.0`),
     dale un título y, si quieres, una breve descripción de qué cambió.
   - Arrastra el `FluxLab.exe` recién compilado al cuadro de archivos adjuntos
     ("Attach binaries") y publica ("Publish release").

A partir de ahí, todas las instalaciones que ya tengan FluxLab abierto van a
detectar la nueva versión solas la próxima vez que la abran y se actualizarán
con un clic — sin que tengas que mandarles el archivo uno por uno.
