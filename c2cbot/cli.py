# pylint: disable=no-value-for-parameter

import sys
import click
from datetime import datetime
from c2cbot.cli_helpers import print_version
from c2cbot.__version__ import cli_version, cli_name
import rttapi 


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


@click.command('service',
               help='''
               Search sub-command to run a service search.  
               ''')
@click.option('--startstation',
              help='''
              Start station CRS code. Use https://www.nationalrail.co.uk/
              stations_destinations/48541.aspx to find the station code.''',
              default='FST')
@click.option('--endstation',
              help='''
              End station CRS code. Use https://www.nationalrail.co.uk/
              stations_destinations/48541.aspx to find the station code.''',
              default='SRY')
@click.option('--startdate',
              help='''
              Start Date for the search in DDMMYYYY (ie. 01012019)
              ''',
              default=datetime.now().strftime('%d%m%Y'))
@click.option('--enddate',
              help='''
              End Date for the search in DDMMYYYY (ie. 01012019)
              ''',
              default=datetime.now().strftime('%d%m%Y'))
@click.option('--starttime',
              help='''
              Start time for the search in 24hr HHMM (ie. 1743)
              ''',
              default=datetime.now().strftime('%H%M'))
@click.option('--endtime',
              help='''
              End time for the search in 24hr HHMM (ie. 1743)
              ''',
              default='2359')
@click.pass_obj
def service(c2cbotaccess, startstation, endstation, startdate, enddate, 
            starttime, endtime):
    """search sub-command to run a service search."""
    click.secho('{0}-{1}-{2}-{3}-{4}-{5}'.format(c2cbotaccess['api_username'], 
                                           startstation,
                                           endstation,
                                           startdate,
                                           starttime,
                                           endtime))
    ss = rttapi.resource("service", c2cbotaccess)


# Register sub-commands.

c2cbot.add_command(service)

if __name__ == "__main__":
    c2cbot()
