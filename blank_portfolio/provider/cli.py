import click
from blank_portfolio.utils.formatter_utils import (
    print_splash,
    print_portfolio,
    print_skills,
    print_experiences,
)
from blank_portfolio.services.cli_service import CLIService

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """🛠️ Blank Portfolio CLI: Explore and filter your developer portfolio from the terminal."""
    print_splash()


@cli.command()
def show_portfolio():
    """Show the portfolio summary including bio, skills, and projects."""
    print_portfolio()


@cli.command(
    help="Show the list of skills with optional filters on name, type, level, and sort order."
)
@click.option(
    "--skill-name",
    "-sn",
    help="Filter skills by comma-separated name(s), e.g., 'skill1,skill2'.",
)
@click.option(
    "--skill-type",
    "-st",
    multiple=True,
    help="Filter skills by type(s). Multiple types can be specified using repeated flags, e.g., -st Tool -st Framework.",
)
@click.option(
    "--skill-level",
    "-sl",
    multiple=True,
    help="Filter skills by level(s). Multiple levels are specified using repeated flags, e.g., -sl Expert -sl Beginner.",
)
@click.option(
    "--sort",
    "-s",
    type=click.Choice(["asc", "desc"], case_sensitive=False),
    default=None,
    help="Sort skills by level ascending ('asc') or descending ('desc').",
)
def list_skills(skill_name, skill_type, skill_level, sort):
    """List your skills filtered by provided criteria."""
    # Process comma-separated skill names into list if provided
    if skill_name:
        skill_name = list(set(skill_name.split(",")))
    if skill_level:
        skill_level = list(set(skill_level))
    if skill_type:
        skill_type = list(set(skill_type))
    print_skills(
        skill_name=skill_name, skill_type=skill_type, skill_level=skill_level, sort=sort
    )


@cli.command(help="Show the list of experiences in your portfolio.")
def list_exp():
    print_experiences()
