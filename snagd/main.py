from fastapi import FastAPI

import click
import uvicorn

from snagd.api.v1 import api_router


app = FastAPI()


@click.command()
def main() -> None:
    """Main function."""
    uvicorn.run(app=app, host="127.0.0.1", port=5050, log_level="info")


if __name__ == "__main__":
    main()

app.include_router(api_router)
