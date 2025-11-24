from blank_portfolio.models.data_models import Skill, SkillLevel
from typing import List


def sort_skills_by_level(skills: List[Skill]) -> List[Skill]:
    level_priority = {
        SkillLevel.EXPERT: 0,
        SkillLevel.ADVANCED: 1,
        SkillLevel.INTERMEDIATE: 2,
        SkillLevel.BEGINNER: 3,
        None: 4,
    }

    skills_sorted = sorted(skills, key=lambda s: level_priority.get(s.level, 4))
    return skills_sorted


def filter_skills(
    skills: List[Skill],
    names: List[str] = None,
    types: List[str] = None,
    levels: List[str] = None,
) -> List[Skill]:
    filtered_skills = skills
    if names:
        names = [n.lower() for n in names]
        filtered_skills = [
            skill for skill in filtered_skills if skill.name.lower() in names
        ]

    if types:
        types = [t.upper() for t in types]
        filtered_skills = [
            skill for skill in filtered_skills if skill.type.name in types
        ]

    if levels:
        levels = [l.upper() for l in levels]
        filtered_skills = [
            skill for skill in filtered_skills if skill.level.name in levels
        ]

    return filtered_skills
