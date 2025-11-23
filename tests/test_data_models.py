import pytest
from datetime import date
from blank_portfolio.data_models import (
    Link,
    Contact,
    Grade,
    Education,
    Project,
    Skill,
    Experience,
    Certification,
    Portfolio,
    SkillType,
    SkillLevel,
    ContactType,
    JobMode,
)


def test_link_validation():
    with pytest.raises(ValueError):
        Link(url="", label="Label")
    with pytest.raises(ValueError):
        Link(url="http://test.com", label="")
    link = Link(url="http://test.com", label="Test")
    assert link.url == "http://test.com"


def test_contact_validation():
    with pytest.raises(ValueError):
        Contact(detail="", type=ContactType.EMAIL)
    with pytest.raises(ValueError):
        Contact(detail="test@example.com", type=None)
    contact = Contact(detail="test@example.com", type=ContactType.EMAIL)
    assert contact.type == ContactType.EMAIL


def test_grade_validation():
    with pytest.raises(ValueError):
        Grade(score=0, scale=0)
    grade = Grade(score=90, scale=100, details="Top scorer")
    assert grade.score == 90


def test_education_validation_and_fields():
    grade = Grade(score=90, scale=100)
    with pytest.raises(ValueError):
        Education(
            degree="", grade=grade, institution="Inst", graduation_date=date.today()
        )
    with pytest.raises(ValueError):
        Education(
            degree="BSc", grade=None, institution="Inst", graduation_date=date.today()
        )
    edu = Education(
        degree="BSc", grade=grade, institution="Inst", graduation_date=date.today()
    )
    assert edu.degree == "BSc"


def test_project_validation():
    with pytest.raises(ValueError):
        Project(name="", description="desc", technologies=["Python"])
    with pytest.raises(ValueError):
        Project(name="Proj", description="", technologies=["Python"])
    with pytest.raises(ValueError):
        Project(name="Proj", description="desc", technologies=[])
    proj = Project(name="Proj", description="desc", technologies=["Python"])
    assert proj.name == "Proj"


def test_skill_defaults():
    skill = Skill(name="Python", type=None, level=None)
    assert skill.type == SkillType.OTHER
    assert skill.level == SkillLevel.BEGINNER
    skill2 = Skill(name="Java", type=SkillType.LANGUAGE, level=SkillLevel.EXPERT)
    assert skill2.type == SkillType.LANGUAGE
    assert skill2.level == SkillLevel.EXPERT


def test_experience_validation():
    with pytest.raises(ValueError):
        Experience(
            role="",
            company="Comp",
            mode=JobMode.REMOTE,
            start_date=date.today(),
            responsibilities=["Dev"],
        )
    with pytest.raises(ValueError):
        Experience(
            role="Dev",
            company="",
            mode=JobMode.REMOTE,
            start_date=date.today(),
            responsibilities=["Dev"],
        )
    with pytest.raises(ValueError):
        Experience(
            role="Dev",
            company="Comp",
            mode=None,
            start_date=date.today(),
            responsibilities=["Dev"],
        )
    with pytest.raises(ValueError):
        Experience(
            role="Dev",
            company="Comp",
            mode=JobMode.REMOTE,
            start_date=None,
            responsibilities=["Dev"],
        )
    with pytest.raises(ValueError):
        Experience(
            role="Dev",
            company="Comp",
            mode=JobMode.REMOTE,
            start_date=date.today(),
            responsibilities=[],
        )
    exp = Experience(
        role="Dev",
        company="Comp",
        mode=JobMode.REMOTE,
        start_date=date.today(),
        responsibilities=["Dev"],
    )
    assert exp.role == "Dev"


def test_certification_validation():
    with pytest.raises(ValueError):
        Certification(url="", name="Cert", organization="Org", issue_date=date.today())
    with pytest.raises(ValueError):
        Certification(url="url", name="", organization="Org", issue_date=date.today())
    with pytest.raises(ValueError):
        Certification(url="url", name="Cert", organization="", issue_date=date.today())
    with pytest.raises(ValueError):
        Certification(url="url", name="Cert", organization="Org", issue_date=None)
    cert = Certification(
        url="url", name="Cert", organization="Org", issue_date=date.today()
    )
    assert cert.name == "Cert"


def test_portfolio_validation():
    # Missing required lists or fields
    empty_list = []
    with pytest.raises(ValueError):
        Portfolio(
            name="",
            role="Role",
            bio="Bio",
            links=[Link("url", "label")],
            contacts=[Contact("e@mail.com", ContactType.EMAIL)],
            experiences=[],
            projects=[],
            educations=[],
            skills=[],
            certifications=[],
        )
    with pytest.raises(ValueError):
        Portfolio(
            name="Name",
            role="",
            bio="Bio",
            links=[Link("url", "label")],
            contacts=[Contact("e@mail.com", ContactType.EMAIL)],
            experiences=[],
            projects=[],
            educations=[],
            skills=[],
            certifications=[],
        )
    # Missing lists raises error
    with pytest.raises(ValueError):
        Portfolio(
            name="Name",
            role="Role",
            bio=None,
            links=[],
            contacts=[],
            experiences=[],
            projects=[],
            educations=[],
            skills=[],
            certifications=[],
        )
    # Valid portfolio
    portfolio = Portfolio(
        name="Name",
        role="Role",
        bio="Bio",
        links=[Link(url="http://site", label="Site")],
        contacts=[Contact(detail="email", type=ContactType.EMAIL)],
        experiences=[
            Experience(
                role="Dev",
                company="Comp",
                mode=JobMode.REMOTE,
                start_date=date.today(),
                responsibilities=["Dev"],
            )
        ],
        projects=[Project(name="Proj", description="desc", technologies=["Python"])],
        educations=[
            Education(
                degree="BSc",
                grade=Grade(90, 100),
                institution="Inst",
                graduation_date=date.today(),
            )
        ],
        skills=[Skill(name="Python", type=SkillType.LANGUAGE, level=SkillLevel.EXPERT)],
        certifications=[
            Certification(
                url="url", name="Cert", organization="Org", issue_date=date.today()
            )
        ],
    )
    assert portfolio.name == "Name"
