"""This script provides a configuration utility for GPT-3 app."""

import os
import click
import keyring


APP_NAME = 'gptoolkit'


@click.command()
@click.option('--api-key', prompt='Enter your OpenAI API key', help='Your OpenAI API key.')
@click.option('--app-data', default=os.path.expanduser('~/.gptoolkit'), help='Directory for storing app data.')
def configure(api_key, app_data):
    """Configures the GPT-3 app with the OpenAI API key and app data directory."""
    keyring.set_password(APP_NAME, 'openai', api_key)
    os.makedirs(app_data, exist_ok=True)
    click.echo(f'OpenAI API key stored in keyring for {APP_NAME}.')
    click.echo(f'App data directory set to {app_data}.')


if __name__ == '__main__':
    configure()

