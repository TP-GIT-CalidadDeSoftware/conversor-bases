# Conversor de Bases Numéricas

CLI en Python para convertir números entre las bases binaria, decimal y hexadecimal.


## Funcionalidades

El conversor soporta las 6 conversiones posibles entre las 3 bases:

| Subcomando | Conversión              | Ejemplo                                 |
| ---------- | ----------------------- | --------------------------------------- |
| `bin-dec`  | Binario → Decimal       | `conversor bin-dec 1010` → `10`         |
| `dec-bin`  | Decimal → Binario       | `conversor dec-bin 10` → `1010`         |
| `dec-hex`  | Decimal → Hexadecimal   | `conversor dec-hex 255` → `FF`          |
| `hex-dec`  | Hexadecimal → Decimal   | `conversor hex-dec FF` → `255`          |
| `bin-hex`  | Binario → Hexadecimal   | `conversor bin-hex 11111111` → `FF`     |
| `hex-bin`  | Hexadecimal → Binario   | `conversor hex-bin FF` → `11111111`     |

## Requisitos

- Python 3.11 o superior
- `pip`

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/TP-GIT-CalidadDeSoftware/conversor-bases.git
cd conversor-bases
```

Crear y activar un entorno virtual:

```bash
# Linux / macOS
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar el proyecto y sus dependencias de desarrollo:

```bash
pip install -e ".[dev]"
```

## Uso

Con el entorno virtual activo:

```bash
conversor bin-dec 1010
conversor dec-hex 255
conversor hex-bin FF
```

Alternativa sin entry point (también funciona):

```bash
python -m conversor_bases bin-dec 1010
```

Ver ayuda:

```bash
conversor --help
conversor bin-dec --help
```

## Desarrollo

### Correr los tests

```bash
pytest
```

Pytest está configurado para reportar cobertura automáticamente.

### Correr los linters y el formatter

```bash
# Verificar formato (sin modificar archivos)
ruff format --check .

# Aplicar formato
ruff format .

# Lint
ruff check .

# Type checking
mypy src/
```

### Pipeline completo (lo mismo que corre el CI)

```bash
ruff format --check .
ruff check .
mypy src/
pytest
```

## Flujo de trabajo Git

Este proyecto sigue **GitHub Flow** con `main` protegida.

1. **`main` siempre estable.** No se permiten commits directos. Toda integración pasa por Pull Request con CI verde y aprobación de al menos un compañero.
2. **Una rama por feature/fix.** Crear desde `main`:
   ```bash
   git checkout main
   git pull
   git checkout -b feat/mi-feature
   ```
3. **Commits siguiendo [Conventional Commits](https://www.conventionalcommits.org/):**
   - `feat:` nueva funcionalidad
   - `fix:` arreglo de bug
   - `docs:` cambios de documentación
   - `style:` cambios de formato (sin afectar comportamiento)
   - `refactor:` refactorización
   - `test:` agregar o modificar tests
   - `chore:` mantenimiento (deps, configs)
   - `ci:` cambios en workflows de CI
4. **Push de la rama y abrir Pull Request hacia `main`:**
   ```bash
   git push -u origin feat/mi-feature
   ```
5. **El PR debe pasar el CI** (formato, lint, type check, tests) y ser **aprobado por al menos un miembro del equipo**.
6. **Merge y eliminación de la rama** (usar "Squash and merge" o "Create a merge commit" según preferencia del equipo).

