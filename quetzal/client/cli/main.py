import click


from quetzal.client import Client, Configuration
from quetzal.client.cli import BaseGroup, help_options, State, MutexOption
from quetzal.client.cli.auth import auth
from quetzal.client.cli.data import data


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Quetzal client version x.y.z')
    ctx.exit()


def url_option(f):

    def callback(ctx, param, value):
        if value and not ctx.resilient_parsing:
            state = ctx.ensure_object(State)
            # Set or leave the default configuration value
            state.api_config.host = value or state.api_config.host

    default_value = Configuration().host
    return click.option('--url',
                        envvar='QUETZAL_URL',
                        default=default_value,
                        show_default=True,
                        help='Quetzal URL. If not set, uses environment '
                             'variable QUETZAL_URL if this variable is defined.',
                        callback=callback)(f)


def user_option(f):

    def callback(ctx, param, value):
        if value and not ctx.resilient_parsing:
            state = ctx.ensure_object(State)
            state.api_config.username = value

    return click.option('--username',
                        envvar='QUETZAL_USER',
                        help='Quetzal username. If not set, uses environment '
                             'variable QUETZAL_USER.',
                        cls=MutexOption,
                        not_required_if=['token'],
                        callback=callback)(f)


def password_option(f):

    def callback(ctx, param, value):
        if value and not ctx.resilient_parsing:
            state = ctx.ensure_object(State)
            state.api_config.password = value

    return click.option('--password',
                        envvar='QUETZAL_PASSWORD',
                        help='Quetzal password. If not set, uses environment '
                             'variable QUETZAL_PASSWORD.',
                        cls=MutexOption,
                        not_required_if=['token'],
                        callback=callback)(f)


def token_option(f):

    def callback(ctx, param, value):
        if value and not ctx.resilient_parsing:
            state = ctx.ensure_object(State)
            state.api_config.access_token = value

    return click.option('--token',
                        envvar='QUETZAL_TOKEN',
                        help='Quetzal access token. If not set, uses environment '
                             'variable QUETZAL_TOKEN.',
                        cls=MutexOption,
                        not_required_if=['username', 'password'],
                        callback=callback)(f)


def insecure_option(f):

    def callback(ctx, param, value):
        if value and not ctx.resilient_parsing:
            state = ctx.ensure_object(State)
            state.api_config.verify_ssl = False
            # Changing the verify_ssl option needs propagation in the client
            state.api_client = Client(state.api_config)
            # Mute urllib3 warnings
            import urllib3
            urllib3.disable_warnings()

    return click.option('--insecure',
                        is_flag=True,
                        help='Do not verify HTTPS certificates.',
                        callback=callback)(f)


def verbose_option(f):
    def callback(ctx, param, value):
        if value and not ctx.resilient_parsing:
            state = ctx.ensure_object(State)
            state.api_config.debug = (value > 1)

    return click.option('-v', '--verbose', count=True, help='Verbosity level.',
                        expose_value=False,
                        callback=callback)(f)


def global_options(f):
    import quetzal.client
    # Note that options need to be chained in reversed order
    f = click.version_option(version=quetzal.client.__version__)(f)
    f = help_options(f)
    f = verbose_option(f)
    f = token_option(f)
    f = password_option(f)
    f = user_option(f)
    f = insecure_option(f)
    f = url_option(f)
    return f


@click.group(options_metavar='[GLOBAL OPTIONS]', cls=BaseGroup)
@global_options
def cli(*args, **kwargs):
    pass


cli.add_command(auth)
cli.add_command(data)


if __name__ == '__main__':
    cli()
