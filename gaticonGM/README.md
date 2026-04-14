# ggm — Gaticon Git Manager

Gestiona compilación e instalación de software desde tags de repositorios git.
Diseñado para Debian Stable: traé versiones recientes sin romper el sistema base.

## Estructura

```
~/.config/ggm/
├── repositories.conf   # alias url
├── state.conf          # alias tag_instalado
└── buildD/
    ├── kicad/          # fuente clonada
    └── freecad/
```

## Instalación

```bash
git clone <este repo>
cd ggm
pip install -e . --break-system-packages
```

O simplemente copiá `ggm.py` y el directorio `ggm/` a `~/.local/bin/ggm` y hacelo ejecutable.

## Uso

```bash
# Añadir repositorio
ggm --add-repository https://gitlab.com/kicad/code/kicad.git kicad

# Verificar dependencias (después del primer build)
ggm checkdeps kicad

# Compilar (último tag automático)
ggm build kicad

# Compilar tag específico
ggm build kicad --tag 8.0.3

# Instalar
ggm install kicad

# Ver estado de todos los repos
ggm list

# Actualizar todos
ggm update

# Eliminar
ggm remove kicad
```

## Sistemas de build soportados

| Sistema     | Detectado por         | Build                        | Install              |
|-------------|-----------------------|------------------------------|----------------------|
| CMake       | CMakeLists.txt        | cmake + cmake --build        | cmake --install      |
| Meson       | meson.build           | meson setup + ninja          | ninja install        |
| Autotools   | configure / configure.ac | ./configure + make        | make install         |
| Makefile    | Makefile              | make -j$(nproc)              | make install         |

## Dependencias opcionales por repo (ggm-deps.txt)

Si el repositorio incluye un archivo `ggm-deps.txt` en su raíz,
`ggm checkdeps` mostrará el comando apt listo para ejecutar.

Formato de `ggm-deps.txt`:
```
# Dependencias para kicad
cmake
libboost-dev
libglew-dev
```

## KiCad y FreeCAD — dependencias de referencia

**KiCad**
```bash
sudo apt install cmake libboost-all-dev libglew-dev libcurl4-openssl-dev \
  libwxgtk3.2-dev python3-dev swig libocct-modeling-algorithms-dev \
  libocct-data-exchange-dev libngspice-dev
```

**FreeCAD**
```bash
sudo apt install cmake libboost-all-dev libcoin-dev libsoqt520-dev \
  libeigen3-dev libgts-dev libopencv-dev python3-dev swig \
  libvtk9-dev libmed-dev
```
