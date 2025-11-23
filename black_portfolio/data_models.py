from enum import Enum
from datetime import date
from dataclasses import dataclass
from typing import List, Optional, Union


class JobMode(Enum):
    REMOTE = "REMOTE"
    ONSITE = "ONSITE"
    HYBRID = "HYBRID"


class ContactType(Enum):
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    OTHER = "OTHER"
    GITHUB = "GITHUB"
    LINKEDIN = "LINKEDIN"


class SkillLevel(Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    EXPERT = "EXPERT"


class SkillType(Enum):
    LANGUAGE = "LANGUAGE"
    FRAMEWORK = "FRAMEWORK"
    TOOL = "TOOL"
    METHODOLOGY = "METHODOLOGY"
    CONCEPT = "CONCEPT"
    TECHNOLOGY = "TECHNOLOGY"
    OTHER = "OTHER"


@dataclass
class Link:
    url: str
    label: str


@dataclass
class Contact:
    detail: str
    type: ContactType


@dataclass
class Grade:
    score: float
    scale: float
    details: Optional[str] = None


@dataclass
class Education:
    degree: str
    grade: Grade
    institution: str
    graduation_date: date
    additional_info: Optional[str] = None


@dataclass
class Project:
    name: str
    description: str
    technologies: List[str]
    link: Optional[str] = None


@dataclass
class Skill:
    name: str
    type: SkillType
    level: Optional[SkillLevel] = None 

@dataclass
class Experience:
    role: str
    company: str
    mode : JobMode
    start_date: date
    responsibilities: List[str]
    end_date: Optional[date] = None 
    learnings: Optional[List[str]] = None


@dataclass
class Certification:
    url: str
    name: str
    organization: str
    issue_date: date
    expiration_date: Optional[date] = None


@dataclass
class Portfolio:
    name: str
    role: str
    bio: Union[List[str],  str]
    links: List[Link]
    contacts: List[Contact]
    experiences: List[Experience]
    projects: List[Project]
    educations: List[Education]
    skills: List[Skill]
    certifications: List[Certification]
