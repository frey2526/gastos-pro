import json
from pathlib import Path

from gasto import Gasto

ARCHIVO = Path(__file__).parent / "gastos.json"


def cargar():
    if not ARCHIVO.exists():
        return []
    with ARCHIVO.open(encoding="utf-8") as f:
        datos = json.load(f)
    return [Gasto.desde_diccionario(d) for d in datos]


def guardar(gastos):
    datos = [g.a_diccionario() for g in gastos]
    with ARCHIVO.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
