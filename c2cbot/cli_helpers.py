import click

def print_version(prgname, prgversion):
    """Helper function to print version of cli."""
    click.secho("{0}, version {1}".format(prgname, prgversion), 
                color='Green')
    
