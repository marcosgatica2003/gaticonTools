"""
ggm.builder — Clonado, compilación e instalación desde tags git.
"""

import subprocess
import sys
import shutil
from pathlib import Path

from . import config
from .repo import get_latest_tag, _hint_buildsystem

def _fetch_appimage(alias: str, url: str, tag: str):
    """Descargar AppImage desde GitHub releases."""
    import re
    import urllib.request
    import json

    # Extraer owner/repo de la URL
    match = re.search(r"github\.com/([^/]+)/([^/]+?)(?:\.git)?$", url)
    if not match:
        print(f"[ggm] Error: no se pudo parsear URL de GitHub: {url}")
        sys.exit(1)

    owner, repo = match.group(1), match.group(2)
    api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}"

    print(f"[ggm] Consultando release {tag} en GitHub...")
    try:
        with urllib.request.urlopen(api_url, timeout=15) as r:
            release = json.loads(r.read())
    except Exception as e:
        print(f"[ggm] Error al consultar API de GitHub: {e}")
        sys.exit(1)

    assets = release.get("assets", [])
    appimages = [a for a in assets if a["name"].endswith(".AppImage")]

    if not appimages:
        print(f"[ggm] No se encontró AppImage x86_64 en el release {tag}.")
        sys.exit(1)

    if len(appimages) > 1:
        print("[ggm] Múltiples AppImages encontrados:")
        for i, a in enumerate(appimages):
            print(f"  [{i}] {a['name']}")
        idx = int(input("[ggm] Elegí uno: "))
        asset = appimages[idx]
    else:
        asset = appimages[0]
    
    # Limpiar AppImage anterior si existe
    state = config.read_state()
    old_path = state.get(f"{alias}__appimage")
    if old_path:
        old = Path(old_path)
        if old.exists():
            old.unlink()
        link = Path.home() / ".local" / "bin" / alias
        if link.is_symlink():
            link.unlink()
        print(f"[ggm] AppImage anterior eliminado.")

    appimage_dir = config.GGM_DIR / "appimagesD"
    appimage_dir = config.GGM_DIR / "appimagesD"
    appimage_dir.mkdir(exist_ok=True)
    dest = appimage_dir / asset["name"]
    print(f"[ggm] Descargando {asset['name']}...")
    urllib.request.urlretrieve(asset["browser_download_url"], dest)
    dest.chmod(0o755)

    # Guardar path en estado
    # state = config.read_state()
    state[f"{alias}__appimage"] = str(dest)
    state[f"{alias}__built"] = tag
    config.write_state(state)

    print(f"[ggm] AppImage guardado en {dest}")
    print(f"[ggm] Ejecutá 'ggm install {alias}' para crear el symlink.")

def build(alias: str, tag: str | None = None, appimage: bool = False):
    """
    Clonar el repositorio en el tag más reciente (o el especificado) y compilar.
    Si ya está clonado, hace fetch y checkout al tag indicado.
    """
    repos = config.read_repos()
    if alias not in repos:
        print(f"[ggm] Error: alias '{alias}' no encontrado.")
        sys.exit(1)

    url = repos[alias]
    build_path = config.get_build_path(alias)
    if tag is None:
        state = config.read_state()
        tag = state.get(f"{alias}__tag")
        if tag:
            print(f"[ggm] Usando tag fijado: {tag}")
        else:
            print(f"[ggm] Consultando último tag de '{alias}'...")
            tag = get_latest_tag(url)
            if tag is None:
                print(f"[ggm] Error: no se encontró ningún tag en {url}")
                sys.exit(1)
            print(f"[ggm] Último tag: {tag}")
    # Resolver tag
    if tag is None:
        print(f"[ggm] Consultando último tag de '{alias}'...")
        tag = get_latest_tag(url)
        if tag is None:
            print(f"[ggm] Error: no se encontró ningún tag en {url}")
            sys.exit(1)
        print(f"[ggm] Último tag: {tag}")

    if appimage:
        _fetch_appimage(alias, url, tag)
        return

    # Clonar o actualizar
    if build_path.exists():
        print(f"[ggm] Directorio existente, actualizando...")
        _run(["git", "fetch", "--tags"], cwd=build_path)
    else:
        print(f"[ggm] Clonando {url}...")
        _run(["git", "clone", url, str(build_path)])

    # Checkout al tag
    print(f"[ggm] Checkout a tag {tag}...")
    _run(["git", "checkout", f"tags/{tag}", "-B", f"ggm-{tag}"], cwd=build_path)

    # Detectar sistema de build y compilar
    print(f"[ggm] Compilando '{alias}' ({tag})...")
    _compile(build_path)

    # Guardar tag compilado en estado
    state = config.read_state()
    state[f"{alias}__built"] = tag
    config.write_state(state)

    print(f"[ggm] Build completado: {alias} @ {tag}")
    print(f"[ggm] Ejecutá 'ggm install {alias}' para instalar.")


def install(alias: str):
    """
    Instalar el software compilado siguiendo el protocolo del autor.
    Detecta el sistema de build y ejecuta el paso de instalación estándar.
    Si no es estándar, avisa al usuario con instrucciones.
    """
    repos = config.read_repos()
    if alias not in repos:
        print(f"[ggm] Error: alias '{alias}' no encontrado.")
        sys.exit(1)


    state = config.read_state()
    built_tag = state.get(f"{alias}__built", "(desconocido)")

    print(f"[ggm] Instalando '{alias}' @ {built_tag}...")

    # Caso appimage
    appimage_path = state.get(f"{alias}__appimage")
    if appimage_path:
        target = Path(appimage_path)
        if not target.exists():
            print(f"[ggm] Error: AppImage no encontrado en {target}")
            sys.exit(1)
        link = Path.home() / ".local" / "bin" / alias
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(target)
        state[alias] = built_tag
        config.write_state(state)
        print(f"[ggm] Symlink creado: {link} -> {target}")
        return

    build_path = config.get_build_path(alias)
    if not build_path.exists():
        print(f"[ggm] Error: '{alias}' no está compilado. Ejecutá 'ggm build {alias}' primero.")
        sys.exit(1)
    _install(build_path, alias)
    _install(build_path, alias)

    state[alias] = built_tag
    config.write_state(state)
    print(f"[ggm] '{alias}' instalado correctamente @ {built_tag}")


def _compile(path: Path):
    """Detectar sistema de build y compilar."""
    build_dir = path / "build"

    if (path / "CMakeLists.txt").exists():
        build_dir.mkdir(exist_ok=True)
        _run(["cmake", "..", "-DCMAKE_BUILD_TYPE=Release"], cwd=build_dir)
        _run(["cmake", "--build", ".", "-j", str(config.getProcValue())], cwd=build_dir)

    elif (path / "meson.build").exists():
        build_dir.mkdir(exist_ok=True)
        _run(["meson", "setup", str(build_dir)], cwd=path)
        _run(["ninja", "-j", str(config.getProcValue()), "-C", str(build_dir)], cwd=path)

    elif (path / "configure").exists():
        _run(["./configure"], cwd=path)
        _run(["make", "-j", str(config.getProcValue())], cwd=path)

    elif (path / "configure.ac").exists():
        _run(["autoreconf", "-fi"], cwd=path)
        _run(["./configure"], cwd=path)
        _run(["make", "-j", str(config.getProcValue())], cwd=path)

    elif (path / "Makefile").exists():
        _run(["make", "-j", str(config.getProcValue())], cwd=path)

    else:
        print("[ggm] Error: sistema de build no reconocido.")
        _hint_buildsystem(path)
        sys.exit(1)


def _install(path: Path, alias: str):
    """Detectar e invocar el paso de instalación."""
    build_dir = path / "build"

    if (path / "CMakeLists.txt").exists() and build_dir.exists():
        _run_doas(["cmake", "--install", "."], cwd=build_dir)

    elif (path / "meson.build").exists() and build_dir.exists():
        _run_doas(["ninja", "-C", str(build_dir), "install"], cwd=path)

    elif (path / "Makefile").exists():
        _run_doas(["make", "install"], cwd=path)

    else:
        print(f"[ggm] No se detectó un paso de instalación estándar para '{alias}'.")
        print(f"[ggm] Revisá manualmente:")
        print(f"      {path / 'INSTALL'} o {path / 'README.md'}")
        _hint_buildsystem(path)
        sys.exit(1)


def _run(cmd: list[str], cwd: Path | None = None):
    """Ejecutar un comando, abortando si falla."""
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"[ggm] Error al ejecutar: {' '.join(cmd)}")
        sys.exit(result.returncode)


def _run_doas(cmd: list[str], cwd: Path | None = None):
    """Ejecutar un comando con doas."""
    _run(["doas"] + cmd, cwd=cwd)


