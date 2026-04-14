"""
ggm.updater — Verificación y actualización de todos los repositorios.
"""

from . import config
from .repo import get_latest_tag
from . import builder


def update_all():
    """
    Verificar el último tag de cada repositorio registrado.
    Si el tag remoto difiere del instalado, recompilar e instalar.
    """
    repos = config.read_repos()
    state = config.read_state()

    if not repos:
        print("[ggm] No hay repositorios registrados.")
        return

    updated = []
    skipped = []
    failed = []

    for alias, url in sorted(repos.items()):
        installed_tag = state.get(alias, None)
        print(f"[ggm] Verificando '{alias}'...", end=" ", flush=True)

        latest_tag = get_latest_tag(url)

        if latest_tag is None:
            print(f"ERROR (no se pudo obtener tag remoto)")
            failed.append(alias)
            continue

        if installed_tag == latest_tag:
            print(f"actualizado ({latest_tag})")
            skipped.append(alias)
            continue

        if installed_tag is None:
            print(f"no instalado, último tag disponible: {latest_tag}")
        else:
            print(f"actualización disponible: {installed_tag} -> {latest_tag}")

        # Compilar e instalar
        builder.build(alias, tag=latest_tag)
        builder.install(alias)
        updated.append((alias, installed_tag, latest_tag))

    # Resumen
    print()
    print("[ggm] === Resumen ===")
    if updated:
        for alias, old, new in updated:
            old_str = old if old else "(no instalado)"
            print(f"  ✓ {alias}: {old_str} -> {new}")
    if skipped:
        print(f"  — Sin cambios: {', '.join(skipped)}")
    if failed:
        print(f"  ✗ Fallidos: {', '.join(failed)}")
