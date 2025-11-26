from typing import List
from blank_portfolio.models.data_models import *
from blank_portfolio.utils.data_utils import sort_skills_by_level, filter_skills
from blank_portfolio.data.datasource import DataSource_provider


class CLIService:
    def __init__(self, portfolio: Portfolio = None):
        self._portfolio = portfolio
        if not self._portfolio:
            self._portfolio = DataSource_provider().get_instance()

    def get_portfolio(self) -> Portfolio:
        return self._portfolio

    def get_contacts(self) -> List[Contact]:
        return self._portfolio.contacts

    def get_experiences(self) -> List[Experience]:
        return self._portfolio.experiences

    def get_skills(self) -> List[Skill]:
        return self._portfolio.skills

    def get_skills_sorted_by_level(self) -> List[Skill]:
        return sort_skills_by_level(self._portfolio.skills)

    def get_skills_filtered(
        self,
        skill_types: List[str],
        skill_names: List[str],
        skill_levels: List[str],
        sort: str = None,
    ) -> List[Skill]:
        _skills = self._portfolio.skills
        if sort == "asc":
            _skills = self.get_skills_sorted_by_level()[::-1]
        elif sort == "desc":
            _skills = self.get_skills_sorted_by_level()

        return filter_skills(
            skills=_skills,
            names=skill_names,
            types=skill_types,
            levels=skill_levels,
        )
