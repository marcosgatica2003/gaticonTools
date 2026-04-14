"""
ggm.repo — Alta, baja y consulta de repositorios.
"""

import subprocess
import sys
from pathlib import Path

from . import config


def add(url: str, alias: str):
    """Registrar un repositorio nuevo."""
    repos = config.read_repos()
    if alias in repos:
        print(f"[ggm] Error: el alias '{alias}' ya existe ({repos[alias]}).")
        print(f"[ggm] Usá 'ggm remove {alias}' primero si querés reemplazarlo.")
        sys.exit(1)
    repos[alias] = url
    config.write_repos(repos)
    print(f"[ggm] Repositorio añadido: {alias} -> {url}")


def remove(alias: str):
    """Eliminar un repositorio registrado."""
    repos = config.read_repos()
    if alias not in repos:
        print(f"[ggm] Error: alias '{alias}' no encontrado.")
        sys.exit(1)

    build_path = config.get_build_path(alias)
    if build_path.exists():
        import shutil
        shutil.rmtree(build_path)
        print(f"[ggm] Directorio de build eliminado: {build_path}")

    del repos[alias]
    config.write_repos(repos)

    state = config.read_state()
    if alias in state:
        del state[alias]
        config.write_state(state)

    print(f"[ggm] Repositorio '{alias}' eliminado.")


def list_repos():
    """Listar repositorios registrados con su estado."""
    repos = config.read_repos()
    state = config.read_state()

    if not repos:
        print("[ggm] No hay repositorios registrados.")
        return

    col_alias = max(len(a) for a in repos) + 2
    print(f"{'ALIAS':<{col_alias}} {'TAG INSTALADO':<20} URL")
    print("-" * 80)
    for alias, url in sorted(repos.items()):
        tag = state.get(alias, "(no instalado)")
        print(f"{alias:<{col_alias}} {tag:<20} {url}")


def checkdeps(alias: str):
    """
    Verificar dependencias declaradas en el repositorio.
    Busca un archivo ggm-deps.txt en la raíz del repo clonado.
    Si no existe, avisa al usuario que revise la documentación upstream.
    """
    repos = config.read_repos()
    if alias not in repos:
        print(f"[ggm] Error: alias '{alias}' no encontrado.")
        sys.exit(1)

    build_path = config.get_build_path(alias)
    if not build_path.exists():
        print(f"[ggm] El repositorio '{alias}' no está clonado aún.")
        print(f"[ggm] Ejecutá 'ggm build {alias}' primero.")
        sys.exit(1)

    deps_file = build_path / "ggm-deps.txt"
    if deps_file.exists():
        deps = [l.strip() for l in deps_file.read_text().splitlines() if l.strip() and not l.startswith("#")]
        if deps:
            print(f"[ggm] Dependencias declaradas para '{alias}':")
            print(f"      apt install {' '.join(deps)}")
        else:
            print(f"[ggm] ggm-deps.txt presente pero vacío.")
    else:
        # Fallback: intentar leer CMakeLists.txt o meson.build para dar pistas
        print(f"[ggm] No se encontró ggm-deps.txt en '{alias}'.")
        print(f"[ggm] Revisá la documentación upstream en:")
        print(f"      {build_path / 'README.md'} o {build_path / 'INSTALL'}")
        _hint_buildsystem(build_path)

def changetag(alias: str):
    repos = config.read_repos()
    if alias not in repos:
        print(f"[ggm] Error: alias '{alias}' no encontrado.")
        sys.exit(1)

    url = repos[alias]
    print(f"[ggm] Obteniendo tags de '{alias}'...")

    result = subprocess.run(
        ["git", "ls-remote", "--tags", "--sort=-v:refname", url],
        capture_output=True, text=True, timeout=60
    )

    tags = []
    for line in result.stdout.splitlines():
        ref = line.split("\t")[-1]
        if ref.endswith("^{}") or not ref.startswith("refs/tags/"):
            continue
        tags.append(ref.replace("refs/tags/", ""))

    if not tags:
        print(f"[ggm] No se encontraron tags en {url}")
        sys.exit(1)

    # Mostrar en less
    tag_list = "\n".join(tags)
    subprocess.run(["less"], input=tag_list, text=True)

    # Pedir selección
    tag = input("[ggm] Ingresá el tag deseado: ").strip()
    if tag not in tags:
        print(f"[ggm] Tag '{tag}' no encontrado en la lista.")
        sys.exit(1)

    state = config.read_state()
    state[f"{alias}__tag"] = tag
    config.write_state(state)
    print(f"[ggm] Tag seleccionado para '{alias}': {tag}")
def _hint_buildsystem(path: Path):
    """Detectar sistema de build y dar pista al usuario."""
    if (path / "CMakeLists.txt").exists():
        print("[ggm] Sistema de build detectado: CMake")
        print("[ggm] Dependencias mínimas sugeridas: cmake build-essential")
    elif (path / "meson.build").exists():
        print("[ggm] Sistema de build detectado: Meson")
        print("[ggm] Dependencias mínimas sugeridas: meson ninja-build build-essential")
    elif (path / "configure").exists() or (path / "configure.ac").exists():
        print("[ggm] Sistema de build detectado: Autotools")
        print("[ggm] Dependencias mínimas sugeridas: autoconf automake build-essential")
    elif (path / "Makefile").exists():
        print("[ggm] Sistema de build detectado: Makefile directo")
        print("[ggm] Dependencias mínimas sugeridas: build-essential")
    else:
        print("[ggm] Sistema de build no reconocido automáticamente.")


def get_latest_tag(url: str) -> str | None:
    """Obtener el último tag semántico de un repositorio remoto sin clonarlo."""
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--tags", "--sort=-v:refname", url],
            capture_output=True, text=True, timeout=30
        )
        for line in result.stdout.splitlines():
            ref = line.split("\t")[-1]
            # Ignorar refs de anotación (^{})
            if ref.endswith("^{}"):
                continue
            if ref.startswith("refs/tags/"):
                return ref.replace("refs/tags/", "")
        return None
    except subprocess.TimeoutExpired:
        print(f"[ggm] Timeout al consultar tags remotos de {url}")
        return None
    except Exception as e:
        print(f"[ggm] Error al obtener tags: {e}")
        return None
