from rich.console import Console
from rich.markup import escape
from rich.prompt import Prompt
from rich.table import Table

from datos import cargar, guardar
from gasto import Gasto

console = Console()


def pedir_monto():
    while True:
        try:
            return float(Prompt.ask("Monto"))
        except ValueError:
            console.print("[red]Eso no es un número. Intenta de nuevo.[/red]")


def agregar(gastos):
    descripcion = Prompt.ask("Descripción").strip()
    if not descripcion:
        console.print("[red]La descripción no puede estar vacía.[/red]")
        return

    monto = pedir_monto()
    categoria = Prompt.ask("Categoría", default="otros").strip().lower()

    gastos.append(Gasto(descripcion, monto, categoria))
    guardar(gastos)
    console.print("[green]Gasto agregado.[/green]")


def listar(gastos):
    if not gastos:
        console.print("No hay gastos todavía.")
        return

    tabla = Table(title="Gastos")
    tabla.add_column("Descripción")
    tabla.add_column("Monto", justify="right")
    tabla.add_column("Categoría")
    for g in gastos:
        tabla.add_row(g.descripcion, f"{g.monto} €", g.categoria)
    console.print(tabla)


def total(gastos):
    suma = sum(g.monto for g in gastos)
    console.print(f"[bold]Total: {suma} €[/bold]")


def por_categoria(gastos):
    categorias = {g.categoria for g in gastos}
    if not categorias:
        console.print("No hay gastos todavía.")
        return

    for cat in sorted(categorias):
        subtotal = sum(g.monto for g in gastos if g.categoria == cat)
        console.print(f"- {cat}: {subtotal} €")


def borrar(gastos):
    if not gastos:
        console.print("No hay gastos para borrar.")
        return

    for i, g in enumerate(gastos, start=1):
        console.print(f"{i}. {g}", markup=False)

    try:
        numero = int(Prompt.ask("Número del gasto a borrar"))
    except ValueError:
        console.print("[red]Eso no es un número.[/red]")
        return

    if numero < 1 or numero > len(gastos):
        console.print("[red]Ese número no existe.[/red]")
        return

    eliminado = gastos.pop(numero - 1)
    guardar(gastos)
    console.print(f"[green]Borrado: {escape(str(eliminado))}[/green]")


def main():
    gastos = cargar()
    console.print("[bold cyan]=== GESTOR DE GASTOS ===[/bold cyan]")

    while True:
        opcion = Prompt.ask("Opción: 1 agregar, 2 listar, 3 total, 4 por categoría, 5 borrar, salir").strip().lower()

        if opcion == "salir":
            console.print("[cyan]¡Hasta luego![/cyan]")
            break
        elif opcion == "1":
            agregar(gastos)
        elif opcion == "2":
            listar(gastos)
        elif opcion == "3":
            total(gastos)
        elif opcion == "4":
            por_categoria(gastos)
        elif opcion == "5":
            borrar(gastos)
        else:
            console.print("[red]Opción no válida.[/red]")


if __name__ == "__main__":
    main()
