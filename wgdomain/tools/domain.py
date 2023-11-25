import sys

import click
import dns.resolver


def get_A_records(domain: str):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        click.echo(f"DNS query error: {e}")
        sys.exit(0)
