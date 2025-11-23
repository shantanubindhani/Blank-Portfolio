import pytest
from typing import List
from black_portfolio.data_models import Skill, SkillLevel, SkillType


@pytest.fixture
def sample_skills() -> List[Skill]:
    return [
        Skill(name="skill1", type=SkillType.LANGUAGE, level=SkillLevel.EXPERT),
        Skill(name="skill2", type=SkillType.LANGUAGE, level=SkillLevel.ADVANCED),
        Skill(name="skill3", type=SkillType.TOOL, level=SkillLevel.INTERMEDIATE),
        Skill(name="skill4", type=SkillType.METHODOLOGY, level=SkillLevel.BEGINNER),
        Skill(name="skill5", type=SkillType.TOOL, level=SkillLevel.EXPERT),
    ]
