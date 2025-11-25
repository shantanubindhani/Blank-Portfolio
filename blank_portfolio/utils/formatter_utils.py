from typing import List, Literal
from rich.console import Console, Group
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from rich.align import Align
from rich.markdown import Markdown
from rich.columns import Columns
from rich.rule import Rule
from rich import box
import time
from blank_portfolio.models.data_models import (
    Portfolio,
    Contact,
    Link,
    Skill,
    SkillLevel,
    Experience,
    Project,
)
from datetime import date
from blank_portfolio.services.cli_service import CLIService

console = Console()
cli_service = CLIService()


SKILL_LEVEL_COLORS = {
    SkillLevel.BEGINNER.name: "bright_black",
    SkillLevel.INTERMEDIATE.name: "yellow",
    SkillLevel.ADVANCED.name: "cyan",
    SkillLevel.EXPERT.name: "green",
}


def get_divider(text: str, style: str = "bright_black"):
    divider = Rule(text, style=style)
    return divider


def show_loading(sleep_time: float = 1.0):
    spinner = Spinner("dots", text="Loading portfolio data...", style="bold cyan")
    with Live(spinner, refresh_per_second=10, transient=True):
        time.sleep(sleep_time)


def format_portfolio_summary(portfolio: Portfolio) -> Panel:
    bio_md = "\n\n".join(portfolio.bio)
    bio_panel = Panel(Markdown(bio_md), title="Bio", border_style="magenta")
    header = Text(
        f"{portfolio.name}\n{portfolio.role}", justify="center", style="bold cyan"
    )
    return Panel(
        Group(header, bio_panel),
        title="Portfolio Summary",
        border_style="cyan",
        padding=(1, 2),
    )


def format_contacts(contacts: List[Contact]) -> Table:
    table = Table(title="Contacts", show_lines=True)
    table.add_column("Type", style="bold")
    table.add_column("Detail")
    for c in contacts:
        table.add_row(c.type.name, c.detail)
    return table


def format_links(links: List[Link]) -> Table:
    table = Table(title="Links", show_lines=True)
    table.add_column("Label", style="bold")
    table.add_column("URL", style="cyan underline")
    for link in links:
        table.add_row(link.label, link.url)
    return table


def format_skills(skills: List[Skill]) -> Table:
    table = Table(title="Skills")
    table.add_column("Skill", style="bold")
    table.add_column("Type")
    table.add_column("Level")
    for skill in skills:
        color = SKILL_LEVEL_COLORS.get(skill.level.name, "white")
        level_text = Text(skill.level.name.capitalize(), style=color)
        table.add_row(skill.name, skill.type.name.capitalize(), level_text)
    return table


def format_experiences(experiences: List[Experience]) -> Panel:
    aligned_panels = []
    for exp in experiences:
        start = exp.start_date.strftime("%b %Y") if exp.start_date else ""
        end = exp.end_date.strftime("%b %Y") if exp.end_date else "Present"
        header_text = f"{exp.role} @ {exp.company} ({start} - {end})"
        header = Text(header_text, style="bold cyan")

        # Format responsibilities with indentation and bullets
        body_lines = [f"- {r}" for r in exp.responsibilities]

        if exp.learnings:
            body_lines.append("")
            body_lines.append("[bold underline]Learnings:[/bold underline]")
            body_lines.extend(f"- {l}" for l in exp.learnings)

        body = "\n".join(body_lines)
        panel = Panel(
            body,
            title=header,
            border_style="blue",
            padding=(1, 2),  # Add padding for better spacing
            expand=False,
        )
        aligned_panels.append(Align(panel, align="center"))

    return Panel(
        Group(*aligned_panels),
        title="[bold bright_blue]Experiences[/bold bright_blue]",
        border_style="bright_blue",
        padding=(1, 2),
    )


def format_projects(projects: List[Project]) -> List[Panel]:
    panels = []
    for proj in projects:
        header = Text(proj.name, style="bold")
        techs = ", ".join(proj.technologies)
        body = f"{proj.description}\n\nTechnologies: {techs}"
        if proj.link:
            body += f"\nLink: [underline cyan]{proj.link}[/underline cyan]"
        panels.append(
            Align(
                Panel(body, title=header, border_style="green", expand=False),
                align="center",
            )
        )
    return Panel(
        Group(*panels), title="Projects", border_style="bright_green", padding=(1, 2)
    )


def print_splash():
    welcome_text = Text(
        "Welcome to Shantanu's CLI Portfolio", style="bold yellow", justify="center"
    )
    context = Text(
        "\nNavigate the portfolio by typing commands.",
        style="white italic",
        justify="center",
    )

    console.print(
        Panel(
            Align(
                Group(
                    welcome_text,
                    get_divider("----- --- -- - -- --- -----"),
                    context,
                ),
                align="center",
            ),
            title="[bold bright_green]🚀 Portfolio CLI[/bold bright_green]",
            border_style="bold magenta",
            padding=(1, 4),
        )
    )


def print_portfolio():
    show_loading(1.1)
    portfolio = cli_service.get_portfolio()
    console.print(format_portfolio_summary(portfolio))
    show_loading(0.4)
    contact_panel = format_contacts(portfolio.contacts)
    link_panel = format_links(portfolio.links)
    social_panel = Panel(
        Group(contact_panel, link_panel),
        title="Contacts & Links",
        border_style="magenta",
        padding=(1, 2),
    )
    skill_panel = format_skills(portfolio.skills)
    columns = Columns([skill_panel, social_panel], equal=True, expand=True)
    console.print(columns)
    show_loading(0.6)
    console.print(format_experiences(portfolio.experiences))
    show_loading(0.6)
    console.print(format_projects(portfolio.projects))


def print_skills(
    skill_name: List[str] = None,
    skill_type: List[str] = None,
    skill_level: List[str] = None,
    sort: Literal["aesc", "desc", None] = None,
):
    skills = cli_service.get_skills_filtered(
        skill_names=skill_name,
        skill_types=skill_type,
        skill_levels=skill_level,
        sort=sort,
    )
    # skills = cli_service.get_skills_sorted_by_level(skills)
    show_loading(0.5)
    console.print("\n\n")
    skill_table = format_skills(skills)
    console.print(skill_table)
    console.print("\n\n")


def print_experiences():
    experiences = cli_service.get_experiences()
    exp_panels = []

    for exp in experiences:
        role_panel = Text(f"{exp.role}\n", style="bold cyan")
        date_panel = Text(
            f"{exp.start_date} to {exp.end_date if exp.end_date else 'Present'}\n",
            style="bold cyan",
        )
        company_panel = Text(f"At : {exp.company}", style="bold cyan")
        mode_panel = Text(f"Mode : {exp.mode.value}", style="bold cyan")

        col1 = Align(
            Panel(Group(role_panel, company_panel), box=box.MINIMAL), align="left"
        )
        col2 = Align(
            Panel(Group(date_panel, mode_panel), box=box.MINIMAL), align="right"
        )

        col_group = Columns(
            [col1, col2],
            align="",
            equal=False,
            expand=True,
        )

        responsibilites_panel = Panel(
            Group(
                get_divider("Responsibilites"),
                Text("\n"),
                Text(
                    "\n\n".join(f"- {r}" for r in exp.responsibilities), justify="left"
                ),
            ),
            style="cyan",
            box=box.MINIMAL,
        )

        learnings_panel = Panel(
            Group(
                get_divider("Learnings"),
                Text("\n"),
                Text("\n\n".join(f"- {r}" for r in exp.learnings), justify="left"),
            ),
            style="cyan",
            box=box.MINIMAL,
        )

        exp_panel = Panel(
            Group(
                col_group,
                responsibilites_panel,
                learnings_panel,
            ),
            title="_-'-_-'-_-'-_-'-_-'-_-'-_",
            style="bright_black",
        )
        exp_panels.append(exp_panel)

    parent_panel = Panel(
        Group(*exp_panels),
        title="Experiences",
        border_style="bright_blue",
        padding=(1, 2),
    )
    show_loading(0.4)
    console.print(parent_panel)
