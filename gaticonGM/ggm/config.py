"""
ggm.config — Gestión de rutas y configuración global.
"""

import os
from pathlib import Path

# Directorio base de trabajo
GGM_DIR = Path(os.environ.get("GGM_HOME", Path.home() / ".config" / "ggm"))
BUILD_DIR = GGM_DIR / "buildD"
REPOS_CONF = GGM_DIR / "repositories.conf"
STATE_FILE = GGM_DIR / "state.conf"  # alias -> tag instalado actualmente
CONFIG_FILE = GGM_DIR / "config"

def readConfig() -> dict[str, str]:
    """Leer config general: formato clave valor"""
    cfg = {}
    if not CONFIG_FILE.exists():
        return cfg
    for line in CONFIG_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            cfg[k.strip()] = v.strip()
    return cfg

def getProcValue() -> int:
    cfg = readConfig()
    try:
        return int(cfg.get("jobs", 1))
    except ValueError:
        return 1

def init():
    """Crear estructura de directorios si no existe."""
    GGM_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    if not REPOS_CONF.exists():
        REPOS_CONF.touch()
    if not STATE_FILE.exists():
        STATE_FILE.touch()


def read_repos() -> dict[str, str]:
    """
    Leer repositories.conf.
    Retorna: {alias: url}
    """
    repos = {}
    for line in REPOS_CONF.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) == 2:
            alias, url = parts
            repos[alias] = url
    return repos


def write_repos(repos: dict[str, str]):
    """Escribir repositories.conf desde un dict {alias: url}."""
    lines = [f"{alias} {url}" for alias, url in sorted(repos.items())]
    REPOS_CONF.write_text("\n".join(lines) + "\n" if lines else "")


def read_state() -> dict[str, str]:
    """
    Leer state.conf.
    Retorna: {alias: tag_instalado}
    """
    state = {}
    for line in STATE_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) == 2:
            alias, tag = parts
            state[alias] = tag
    return state


def write_state(state: dict[str, str]):
    """Escribir state.conf desde un dict {alias: tag}."""
    lines = [f"{alias} {tag}" for alias, tag in sorted(state.items())]
    STATE_FILE.write_text("\n".join(lines) + "\n" if lines else "")


def get_build_path(alias: str) -> Path:
    """Retorna el directorio de build para un alias."""
    return BUILD_DIR / alias
