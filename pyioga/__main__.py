import click
import pyioga


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--client-secret-file",
    required=True,
    help="Path to client secrets file, downloaded from GCP/Credentials",
    type=str,
)
@click.option(
    "--output-file",
    required=True,
    help="Path in which authorized user file will be created",
    type=str,
)
@click.option(
    "--port",
    default=0,
    help="Port used by local server used by Google to perform `Flow`.",
    type=int,
)
def init(client_secret_file: str, output_file: str, port: int) -> None:
    pyioga.get_authorized_user_file(
        client_secret_file=client_secret_file, output_file=output_file, port=port
    )


if __name__ == "__main__":
    init()
