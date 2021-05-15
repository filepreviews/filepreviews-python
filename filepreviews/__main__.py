import click

from filepreviews import VERSION, FilePreviews


@click.group()
@click.version_option(version=VERSION)
@click.option("--debug", default=False, is_flag=True)
@click.option("--api_key", required=True, help="FilePreviews API Key")
@click.option("--api_secret", required=True, help="FilePreviews API Secret")
@click.pass_context
def cli(ctx, **kwargs):
    if ctx.obj is None:
        ctx.obj = {}

    ctx.obj["file_previews"] = FilePreviews(
        api_key=kwargs["api_key"],
        api_secret=kwargs["api_secret"],
        debug=kwargs["debug"],
    )


@cli.command()
@click.option("--metadata")
@click.option("--width", help="Specifies maximum value of thumbnail width.")
@click.option("--height", help="Specifies maximum value of thumbnail height.")
@click.option("--format", type=click.Choice(["png", "jpg", "jpeg"]))
@click.argument("url")
@click.pass_context
def generate(ctx, url, *args, **kwargs):
    """
    Generate preview for URL.
    """
    file_previews = ctx.obj["file_previews"]

    options = {}
    metadata = kwargs["metadata"]
    width = kwargs["width"]
    height = kwargs["height"]
    output_format = kwargs["format"]

    if metadata:
        options["metadata"] = metadata.split(",")

    if width:
        options.setdefault("size", {})
        options["size"]["width"] = width

    if height:
        options.setdefault("size", {})
        options["size"]["height"] = height

    if output_format:
        options["format"] = output_format

    results = file_previews.generate(url, **options)

    click.echo(results)


@cli.command()
@click.argument("preview_id")
@click.pass_context
def retrieve(ctx, preview_id, *args, **kwargs):
    """
    Retreive preview results for ID.
    """
    file_previews = ctx.obj["file_previews"]
    results = file_previews.retrieve(preview_id)

    click.echo(results)
