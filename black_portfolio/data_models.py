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

    def __post_init__(self):
        if not self.url or not self.label:
            raise ValueError(f"Link url and label attributes cannot be left empty!.")


@dataclass
class Contact:
    detail: str
    type: ContactType

    def __post_init__(self):
        if not self.type or not self.detail:
            raise ValueError("Contact Type and Detail cannot be left empty!.")


@dataclass
class Grade:
    score: float
    scale: float
    details: Optional[str] = None

    def __post_init__(self):
        if not self.score or not self.scale:
            raise ValueError("Grade Score and Scale cannot be left empty!.")


@dataclass
class Education:
    degree: str
    grade: Grade
    institution: str
    graduation_date: date
    additional_info: Optional[str] = None

    def __post_init__(self):
        err_str = (
            "" + "degree, "
            if not self.degree
            else (
                "" + "grade, "
                if not self.grade
                else (
                    "" + "institution, "
                    if not self.institution
                    else "" + "graduation_date, " if not self.graduation_date else ""
                )
            )
        )
        if err_str != "":
            raise ValueError("Education (" + err_str[:-2] + ") cannot be left empty!.")


@dataclass
class Project:
    name: str
    description: str
    technologies: List[str]
    link: Optional[str] = None

    def __post_init__(self):
        err_str = (
            "" + "name, "
            if not self.name
            else (
                "" + "description, "
                if not self.description
                else "" + "technologies, " if not self.technologies else ""
            )
        )
        if err_str != "":
            raise ValueError("Project (" + err_str[:-2] + ") cannot be left empty!.")


@dataclass
class Skill:
    name: str
    type: SkillType
    level: Optional[SkillLevel] = None

    def __post_init__(self):
        if not self.type:
            self.type = SkillType.OTHER
        if not self.level:
            self.level = SkillLevel.BEGINNER


@dataclass
class Experience:
    role: str
    company: str
    mode: JobMode
    start_date: date
    responsibilities: List[str]
    end_date: Optional[date] = None
    learnings: Optional[List[str]] = None

    def __post_init__(self):
        err_str = (
            "" + "role, "
            if not self.role
            else (
                "" + "company, "
                if not self.company
                else (
                    "" + "mode, "
                    if not self.mode
                    else (
                        "" + "start_date, "
                        if not self.start_date
                        else (
                            "" + "responsibilities, "
                            if not self.responsibilities
                            else ""
                        )
                    )
                )
            )
        )
        if err_str != "":
            raise ValueError("Experience (" + err_str[:-2] + ") cannot be left empty!.")


@dataclass
class Certification:
    url: str
    name: str
    organization: str
    issue_date: date
    expiration_date: Optional[date] = None

    def __post_init__(self):
        err_str = (
            "" + "url, "
            if not self.url
            else (
                "" + "name, "
                if not self.name
                else (
                    "" + "organization, "
                    if not self.organization
                    else "" + "issue_date, " if not self.issue_date else ""
                )
            )
        )
        if err_str != "":
            raise ValueError(
                "Certification (" + err_str[:-2] + ") cannot be left empty!."
            )


@dataclass
class Portfolio:
    name: str
    role: str
    bio: Union[List[str], str]
    links: List[Link]
    contacts: List[Contact]
    experiences: List[Experience]
    projects: List[Project]
    educations: List[Education]
    skills: List[Skill]
    certifications: List[Certification]

    def __post_init__(self):
        err_str = (
            "" + "name, "
            if not self.name
            else (
                "" + "role, "
                if not self.role
                else (
                    "" + "bio, "
                    if not self.bio
                    else (
                        "" + "links, "
                        if not self.links
                        else (
                            "" + "contacts, "
                            if not self.contacts
                            else (
                                "" + "experiences, "
                                if not self.experiences
                                else (
                                    "" + "projects, "
                                    if not self.projects
                                    else (
                                        "" + "educations, "
                                        if not self.educations
                                        else (
                                            "" + "skills, "
                                            if not self.skills
                                            else (
                                                "" + "certifications, "
                                                if not self.certifications
                                                else ""
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
        if err_str != "":
            raise ValueError("Education (" + err_str[:-2] + ") cannot be left empty!.")
