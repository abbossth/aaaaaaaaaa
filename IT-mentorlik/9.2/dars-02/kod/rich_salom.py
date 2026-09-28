from rich import print
from rich.table import Table
from rich.console import Console

print("[bold magenta]Salom, dunyo![/bold magenta] :rocket:")

table = Table(title="Mening texnologiyalarim")
table.add_column("Texnologiya", style="cyan")
table.add_column("Daraja", style="green")
table.add_row("Python", "⭐⭐⭐")
table.add_row("Git", "⭐⭐")
table.add_row("Docker", "⭐ (tez orada!)")

Console().print(table)
