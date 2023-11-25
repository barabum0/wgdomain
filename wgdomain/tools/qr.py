import configparser
import io

import click


def print_qr(config: configparser.ConfigParser):
    import segno

    str_out = io.StringIO()
    config.write(str_out)
    str_out.seek(0)

    qrcode = segno.make(str_out.read(), micro=False)

    click.echo()
    click.echo(qrcode.terminal(compact=True))
