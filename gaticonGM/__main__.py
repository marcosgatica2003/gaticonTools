#!/usr/bin/env python3
"""
ggm - Gaticon Git Manager
Gestiona compilación e instalación de software desde tags de repositorios git.

Uso:
    ggm --add-repository <url> <alias>
    ggm checkdeps <alias>
    ggm build <alias>
    ggm install <alias>
    ggm update
    ggm list
    ggm remove <alias>
"""

import sys
import argparse
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ggm import config, repo, builder, updater

def main():

    parser = argparse.ArgumentParser(
        prog="ggm",
        description="Gaticon Git Manager — gestión de software desde tags git",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    subparsers = parser.add_subparsers(dest="command")

    # --add-repository
    p_add = subparsers.add_parser("add", help="Añadir repositorio")
    p_add.add_argument("url", help="URL del repositorio git")
    p_add.add_argument("alias", help="Alias local para el repositorio")

    # checkdeps
    p_deps = subparsers.add_parser("checkdeps", help="Verificar dependencias de un repositorio")
    p_deps.add_argument("alias", help="Alias del repositorio")

    # build
    p_build = subparsers.add_parser("build", help="Compilar un repositorio")
    p_build.add_argument("alias", help="Alias del repositorio")
    p_build.add_argument("--tag", help="Tag específico a compilar (por defecto: último tag)", default=None)

    # install
    p_install = subparsers.add_parser("install", help="Instalar un repositorio compilado")
    p_install.add_argument("alias", help="Alias del repositorio")

    # update
    subparsers.add_parser("update", help="Verificar y actualizar todos los repositorios")

    # list
    subparsers.add_parser("list", help="Listar repositorios registrados")

    # remove
    p_remove = subparsers.add_parser("remove", help="Eliminar un repositorio")
    p_remove.add_argument("alias", help="Alias del repositorio a eliminar")

    p_build.add_argument("--appimage", action="store_true", help="Descargar AppImage en lugar de compilar")
    p_changetag = subparsers.add_parser("changetag", help="Seleccionar tag de un repositorio")
    p_changetag.add_argument("alias", help="Alias del repositorio")
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # Inicializar estructura de directorios
    config.init()

    match args.command:
        case "add":
            repo.add(args.url, args.alias)
        case "checkdeps":
            repo.checkdeps(args.alias)
        case "build":
            builder.build(args.alias, tag=args.tag, appimage=args.appimage)
        case "install":
            builder.install(args.alias)
        case "update":
            updater.update_all()
        case "list":
            repo.list_repos()
        case "help":
            print("Hola!")
        case "changetag":
            repo.changetag(args.alias)
        case "remove":
            repo.remove(args.alias)
        case _:
            parser.print_help()
            sys.exit(1)


if __name__ == "__main__":
    main()
