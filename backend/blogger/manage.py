#!/usr/bin/env python3

from typer import Typer

app = Typer()


def run():
    app()


@app.command()
def runserver(
    host: str = "0.0.0.0", port: int = 8000, reload: bool = False, debug: bool = False
):
    import uvicorn

    uvicorn.run("blogger.asgi:app", host=host, port=port, reload=reload, debug=debug)


if __name__ == "__main__":
    run()
