import typer
from rich.console import Console
from rich.table import Table
from model import ToDo
from database import insert_task, get_tasks, delete_task, update_task, complete_task


console = Console()
app = typer.Typer()

@app.command(short_help="Add new Task")
def add(task: str, category: str):
    console.print(f"[bold green] [+] Task Added [/bold green]")
    toDo = ToDo(task, category)
    insert_task(toDo)
    show()

@app.command()
def delete(position: int):
    console.print(f"[bold red] [-] Task [{position}] Was Deleted[/bold red]")
    delete_task(position-1)
    show()

@app.command()
def update(position: int, task: str, category: str):
    console.print(f"[bold blue] [+] Update Task [{position}] Successful! [/bold blue]")
    update_task(position-1, task, category)
    show()

@app.command()
def complete(position: int):
    console.print(f"[bold yellow] [+] Task [{position}] Completed [/bold yellow]")
    complete_task(position-1)
    show()

@app.command()
def show():
    tasks = get_tasks()
    table = Table(show_header=True)
    table.add_column("[grey62]#[/grey62]", style="bold white", min_width=2)
    table.add_column("[deep_sky_blue3]Tasks To Do[/deep_sky_blue3] 🔖", style="bold", min_width=20)
    table.add_column("[aquamarine1]Category[/aquamarine1]", min_width=11, justify="center")
    table.add_column("[bold green]Task Added At[/bold green]", min_width=10, justify="center")
    table.add_column("[bold red]Task Completed At[/bold red]", min_width=10, justify="center")
    table.add_column("[bold dark_orange]Status[/bold dark_orange]", min_width=5, justify="center")

    def get_category_color(category: str):
        COLORS = {'Learn': 'cyan', 'Watch': 'red', 'Study': 'green', 'Play': 'blue', 'Read': 'bold magenta'}
        if category in COLORS:
            return COLORS[category]
        return 'yellow'

    for index, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done = '✅' if task.status == 2 else '❌'
        table.add_row(f'[grey62]{str(index)}[/grey62]', f'[bright_white]{task.task}[/bright_white]', f'[{c}]{task.category}[/{c}]', f'[bold green]{task.date_added}[/bold green]' ,f'[bold red]{task.date_completed}[/bold red]' if (task.date_completed) else "-/-/-", is_done)
   
    console.print(table)


def print_banner():
	console.print(r"""
                                   _,)
                         _..._.-;-'
                      .-'     `(
                     /      ;   \
                     ;.' ;`  ,;  ;      📚 [bold purple]ALL TASKS TO DO[/bold purple] 📃
                    .'' ``. (  \ ; 
                   / f_ _L \ ;  )\
                   \/|` '|\/;; <;/
                  ((; \_/  (()
                       "
    """)


if __name__ == "__main__":
    print_banner()
    app()