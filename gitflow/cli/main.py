from pathlib import Path
from typing import Optional

import typer
from git import Repo
from typer import Option
from typing_extensions import Annotated

import gitflow

repo = Repo(Path.cwd(), search_parent_directories=True)
app = typer.Typer(no_args_is_help=True, pretty_exceptions_enable=False, add_completion=False)


def version_callback(value: bool):
    if not value:
        return
    print(gitflow.__version__)
    raise typer.Exit()


@app.callback()
def common(
    ctx: typer.Context,
    version: Annotated[
        bool,
        Option(
            "--version",
            "-v",
            callback=version_callback,
            help="Print gnwmanager version.",
        ),
    ] = False,
):
    pass


def issue_id(id: str):
    return f"issue-{id}" if id else "no-ref"


@app.command()
def feature(
    name: Annotated[str, typer.Option(prompt=True)],
    id: Annotated[Optional[str], typer.Argument(callback=issue_id)] = None,
):
    branch = f"feature/{id}/{name.replace(' ', '-')}"
    repo.git.checkout(branch, b=True)
    print(f"created branch {branch}")


@app.command()
def bug(
    name: Annotated[str, typer.Option(prompt=True)],
    id: Annotated[Optional[str], typer.Argument(callback=issue_id)] = None,
):
    branch = f"bugfix/{id}/{name.replace(' ', '-')}"
    repo.git.checkout(branch, b=True)


@app.command()
def complete(target_branch: Annotated[str, typer.Argument()] = "main"):
    purged_branch = repo.active_branch
    repo.git.checkout(target_branch)
    repo.git.pull()
    repo.git.branch("-D", purged_branch.name)
    print(f"removed branch {purged_branch.name}, currently on {target_branch}")


def run_app():
    app(prog_name="gitflow")
