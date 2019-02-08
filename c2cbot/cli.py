import sys
import click
from c2cbot.cli_helpers import print_version
from c2cbot.__version__ import cli_version, cli_name


@click.group()
@click.pass_context
@click.version_option(prog_name='c2cbot_cli', version=cli_version)
@click.option('--rttapi-username',
              envvar='RTT_API_USERNAME',
              default=None,
              type=str)
@click.option('--rttapi-password',
              envvar='RTT_API_PASSWORD',
              default=None,
              type=str)
@click.option('--rttapi-url',
              envvar='RTT_API_URL',
              default=None,
              type=str)
def c2cbot(c2cbotaccess, rttapi_username, rttapi_password, rttapi_url):
    """c2cbot_cli - cli tool to search and print stats."""
    print_version(cli_name, cli_version)
    if rttapi_username is None or rttapi_password is None: 
        click.secho("An API username and password must be passed when"
                    "running the bot.", color='Red')
    if rttapi_url is None:
       click.secho('''An API url must be passed when running the bot.''',
                   color='Red')
    c2cbotaccess.obj = {"api_username": rttapi_username,
                        "api_password": rttapi_password,
                        "api_url": rttapi_url}


@click.command('search')
@click.option('--startstation',
              help='''
              
              ''',)
@click.pass_obj
def search(c2cbotaccess, startstation):
    """search sub-command to run a service search."""
    pass

# Register sub-commands.

c2cbot.add_command(search)

if __name__ == "__main__":
    c2cbot()
