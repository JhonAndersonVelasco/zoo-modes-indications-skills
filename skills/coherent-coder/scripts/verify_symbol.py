#!/usr/bin/env python3
"""
verify_symbol.py

Verifica que una ruta punteada (modulo.submodulo.funcion_o_clase) EXISTA
realmente en el entorno Python actual, antes de usarla en el codigo.
Reemplaza la memoria del modelo por un hecho verificable.

Uso:
    python scripts/verify_symbol.py scipy.signal.savgol_filter
    python scripts/verify_symbol.py pandas.DataFrame.rolling
    python scripts/verify_symbol.py numpy.trapz

Salida:
    OK: <ruta> existe -> <tipo>
    NOT_FOUND: ...  (indicando el punto exacto donde se rompe la cadena)

Exit code: 0 si existe, 1 si no existe o hay error.
"""
import importlib
import sys


def verify(dotted_path: str) -> tuple[bool, str]:
    parts = dotted_path.split(".")
    obj = None
    imported = ""
    rest: list[str] = []

    # Intenta importar el prefijo mas largo posible como modulo,
    # luego resuelve el resto como cadena de atributos.
    for i in range(len(parts), 0, -1):
        modname = ".".join(parts[:i])
        try:
            obj = importlib.import_module(modname)
            imported = modname
            rest = parts[i:]
            break
        except ImportError:
            continue

    if obj is None:
        return False, f"NOT_FOUND: ningun modulo importable dentro de '{dotted_path}'"

    path_so_far = imported
    for attr in rest:
        if hasattr(obj, attr):
            obj = getattr(obj, attr)
            path_so_far += "." + attr
        else:
            return False, (
                f"NOT_FOUND: '{attr}' no existe en '{path_so_far}' "
                f"(revisa la version instalada con 'pip show' o el nombre real del simbolo, "
                f"no adivines otro nombre de memoria)"
            )

    return True, f"OK: '{dotted_path}' existe -> {type(obj)}"


def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: python scripts/verify_symbol.py <ruta.punteada.al.simbolo>")
        sys.exit(2)

    ok, message = verify(sys.argv[1])
    print(message)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()