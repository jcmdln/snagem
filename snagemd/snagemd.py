import click
import uvicorn

from snagemd import api


@click.command()
def main() -> None:
    uvicorn.run(app=api.app, host="127.0.0.1", port=5050, log_level="info")


if __name__ == "__main__":
    main()
