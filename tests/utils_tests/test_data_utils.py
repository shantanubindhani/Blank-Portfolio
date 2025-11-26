# Central Test Pattern Template

import pytest
from typing import List, Optional
from blank_portfolio.models.data_models import Skill, SkillLevel, SkillType
from blank_portfolio.utils.data_utils import sort_skills_by_level, filter_skills
from tests.test_data.test_data import sample_skills


def test_should_sort_skills_by_level_correctly(sample_skills):
    sorted_skills = sort_skills_by_level(sample_skills)
    levels = [skill.level for skill in sorted_skills]
    expected_levels = [
        SkillLevel.BEGINNER,
        SkillLevel.INTERMEDIATE,
        SkillLevel.ADVANCED,
        SkillLevel.EXPERT,
        SkillLevel.EXPERT,
    ]
    assert levels == expected_levels


def test_should_filter_skills_by_names_case_insensitive(sample_skills):
    filtered = filter_skills(sample_skills, names=["skill1", "skill2"])
    filtered_names = sorted([skill.name for skill in filtered])
    expected_names = ["skill1", "skill2"]
    assert filtered_names == expected_names


def test_should_filter_skills_by_types_properly(sample_skills):
    filtered = filter_skills(sample_skills, types=["TOOL"])
    filtered_names = sorted([skill.name for skill in filtered])
    expected_names = ["skill3", "skill5"]
    assert filtered_names == expected_names


def test_should_filter_skills_by_levels_properly(sample_skills):
    filtered = filter_skills(sample_skills, levels=["EXPERT"])
    filtered_names = sorted([skill.name for skill in filtered])
    expected_names = ["skill1", "skill5"]
    assert filtered_names == expected_names


def test_should_filter_skills_by_names_and_levels_together(sample_skills):
    filtered = filter_skills(
        sample_skills, names=["skill3", "skill4"], levels=["INTERMEDIATE"]
    )
    filtered_names = sorted([skill.name for skill in filtered])
    expected_names = ["skill3"]
    assert filtered_names == expected_names


def test_should_return_all_skills_when_no_filter_applied(sample_skills):
    filtered = filter_skills(sample_skills)
    assert len(filtered) == len(sample_skills)
