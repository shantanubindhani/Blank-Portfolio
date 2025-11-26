import pytest
from blank_portfolio.services.cli_service import CLIService
from blank_portfolio.models.data_models import SkillLevel, SkillType


@pytest.fixture
def cli_service():
    return CLIService()


def test_get_portfolio(cli_service):
    portfolio = cli_service.get_portfolio()
    assert portfolio.name is not None
    assert portfolio.skills is not None


def test_get_contacts(cli_service):
    contacts = cli_service.get_contacts()
    assert isinstance(contacts, list)
    assert all(hasattr(c, "detail") for c in contacts)


def test_get_experiences(cli_service):
    experiences = cli_service.get_experiences()
    assert isinstance(experiences, list)
    assert all(hasattr(e, "role") for e in experiences)


def test_get_skills(cli_service):
    skills = cli_service.get_skills()
    assert isinstance(skills, list)
    assert all(hasattr(s, "name") for s in skills)


def test_get_skills_sorted_by_level(cli_service):
    skills = cli_service.get_skills_sorted_by_level()
    levels = [s.level for s in skills]
    assert all(levels[i].value <= levels[i + 1].value for i in range(len(levels) - 1))


def test_get_skills_filtered_name(cli_service):
    filtered = cli_service.get_skills_filtered(
        skill_names=["Python"], skill_types=None, skill_levels=None
    )
    assert all("Python".lower() in s.name.lower() for s in filtered)


def test_get_skills_filtered_type(cli_service):
    filtered = cli_service.get_skills_filtered(
        skill_names=None, skill_types=[SkillType.TOOL.name], skill_levels=None
    )
    assert all(s.type.name == SkillType.TOOL.name for s in filtered)


def test_get_skills_filtered_level(cli_service):
    filtered = cli_service.get_skills_filtered(
        skill_names=None, skill_types=None, skill_levels=[SkillLevel.EXPERT.name]
    )
    assert all(s.level.name == SkillLevel.EXPERT.name for s in filtered)


def test_get_skills_filtered_sort_asc(cli_service):
    filtered = cli_service.get_skills_filtered(
        skill_names=None, skill_types=None, skill_levels=None, sort="asc"
    )
    levels = [s.level for s in filtered]
    assert all(levels[i].value >= levels[i + 1].value for i in range(len(levels) - 1))


def test_get_skills_filtered_sort_desc(cli_service):
    filtered = cli_service.get_skills_filtered(
        skill_names=None, skill_types=None, skill_levels=None, sort="desc"
    )
    levels = [s.level for s in filtered]
    assert all(levels[i].value <= levels[i + 1].value for i in range(len(levels) - 1))
