import click

from .main import main


def validate_key_value_pair(ctx, param, keys_and_values):
    for key_and_value in keys_and_values:
        try:
            key, value = key_and_value.split(':')
        except ValueError:
            raise click.BadParameter(
                "Values must be formatted as 'key:value'."
            )
    return keys_and_values


@main.group(invoke_without_command=True)
@click.pass_context
def config(ctx):
    """
    Wrapper around `geth`.
    """
    if ctx.invoked_subcommand is None:
        project = ctx.obj['PROJECT']
        config = project.config

        if not any(config.options(section) for section in config.sections()):
            click.echo(
                "No configuration values set.  Use `populus config set "
                "some_key:a_value` to set configuration options."
            )

        for section in config.sections():
            if not config.options(section):
                # don't print empty sections
                continue
            click.echo("[{0}]".format(section))
            for key in config.options(section):
                click.echo("  {key} = {value}".format(
                    key=key, value=config.get(section, key)
                ))


@config.command('set')
@click.option(
    '--section',
    '-s',
    default='populus',
)
@click.argument(
    'keys_and_values',
    nargs=-1,
    callback=validate_key_value_pair,
)
@click.pass_context
def config_set(ctx, section, keys_and_values):
    """
    Sets key/value pairs in the populus.ini configuration file. Values should
    be formatted as 'key:value'.
    """
    project = ctx.obj['PROJECT']
    config = project.config

    if not config.has_section(section):
        config.add_section(section)

    for key_and_value in keys_and_values:
        key, value = key_and_value.split(':')
        config.set(section, key, value)

    with open(ctx.obj['PRIMARY_CONFIG'], 'w') as config_file:
        config.write(config_file)


@config.command('unset')
@click.option(
    '--section',
    '-s',
    default='populus',
)
@click.option(
    '--confirm/--no-confirm',
    is_flag=True,
    default=True,
)
@click.argument(
    'keys',
    nargs=-1,
)
@click.pass_context
def config_unset(ctx, section, confirm, keys):
    """
    Deletes the provided keys from the configuration.  To delete an entire
    section, pass in '*'
    """
    project = ctx.obj['PROJECT']
    config = project.config

    if not config.has_section(section):
        if confirm:
            confirm_msg = (
                "Are you sure you want to delete the {0!r} section?".format(
                    section
                )
            )
            if not click.prompt(confirm_msg):
                ctx.abort()
        ctx.abort("Unknown section: {0!r}".format(section))

    if len(keys) == 1 and keys[0] == "*":
        config.remove_section(section)
    else:
        for key in keys:
            config.remove_option(section, key)

    with open(ctx.obj['PRIMARY_CONFIG'], 'w') as config_file:
        config.write(config_file)
