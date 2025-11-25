from datetime import date
from typing import List
from blank_portfolio.models.data_models import *
from blank_portfolio.utils.data_utils import sort_skills_by_level


class DataSource_provider:
    _instance = None

    def __init__(self):
        if self._instance is not None:
            return
        else:
            self._instance = self.generate_portfolio()

    def get_instance(self):
        return self._instance if self._instance else self.__init__()

    def generate_portfolio(self) -> Portfolio:
        _name = "Shantanu Bindhani"
        _role = "SDE / Backend Developer / Software Engineer"
        _bio = [
            "Hi, I am Software Developer from hailing from Balasore, Orissa, India.",
            "I am Experienced in backend development, microservices, \n  and also knowledgeable about Web, Game, Android, software development.",
            "Some of my strongest holds are on python, java, c++, and other technologies related to them.\n you can skim through my portfolio to learn more about them.",
        ]
        _links = self.get_links()
        _contacts = self.get_contacts()
        _experiences = self.get_experiences()
        _projects = self.get_projects()
        _educations = self.get_educations()
        _skills = self.get_skills()
        _certifications = self.get_certifications()

        _portfolio = Portfolio(
            name=_name,
            role=_role,
            bio=_bio,
            links=_links,
            contacts=_contacts,
            experiences=_experiences,
            projects=_projects,
            educations=_educations,
            skills=_skills,
            certifications=_certifications,
        )

        return _portfolio

    def get_links(self) -> List[Link]:
        return [
            Link(url="https://linkedin.com/in/shantanubindhani", label="LinkedIn"),
            Link(url="https://github.com/shantanubindhani", label="GitHub"),
        ]

    def get_contacts(self) -> List[Contact]:
        return [
            Contact(detail="shantanubindhani1805@gmail.com", type=ContactType.EMAIL),
            Contact(detail="+91-8917322838", type=ContactType.PHONE),
        ]

    def get_experiences(self) -> List[Experience]:
        return [
            Experience(
                role="Backend SDE Intern",
                company="Datachecks, Bangalore",
                mode=JobMode.REMOTE,
                start_date=date(2024, 11, 1),
                end_date=date(2025, 4, 30),
                responsibilities=[
                    "Spearheaded the development and enhancement of multiple features and system integrations using a modern Python tech stack, specifically leveraging FastAPI for high-performance API creation, SQL Alchemy for robust ORM, and Celery for efficient asynchronous task processing, all connected to a PostgreSQL database.",
                    "Ensured code reliability and functional correctness by comprehensively designing and writing automated tests at multiple levels, including Unit tests, Integration, and Repository tests, utilizing the Pytest framework to maintain a high standard of quality assurance.",
                    "Applied advanced software engineering principles and system design patterns, such as the Singleton Architecture and Dependency Injection, to optimize code structure and application flow, directly resulting in significant improvements to overall efficiency and reduced load times.",
                    "Actively monitored and maintained the stability and reliability of the deployed APIs and application services; specifically utilized Sentry for real-time error tracking and alerting, and leveraged Codecov to track and enforce high API test coverage metrics.",
                    "Engaged in end-to-end feature development within a small, highly collaborative and qualified team, taking ownership from conceptual design through deployment, and facilitating efficient knowledge sharing and code review processes to ensure alignment with project goals and delivery timelines.",
                ],
                learnings=[
                    "Learned to build and deploy high-performance Python APIs, mastering the FastAPI, SQL Alchemy, and Celery stack with PostgreSQL.",
                    "Gained expertise in test-driven development, mastering the creation of Unit, Integration, and Repository tests using the Pytest framework.",
                    "Acquired practical skills in application monitoring and quality assurance using Sentry for real-time tracking and Codecov for test coverage enforcement.",
                    "Mastered the application of advanced design patterns (Singleton Architecture, Dependency Injection) to optimize code for efficiency and reduced load times.",
                ],
            ),
            Experience(
                role="Software Development Engineer Intern",
                company="Ciright Inc., Ahmedabad",
                mode=JobMode.ONSITE,
                start_date=date(2023, 1, 1),
                end_date=date(2023, 6, 30),
                responsibilities=[
                    "Developed and maintained 30+ business verticals for platforms like Ciright.com and Veuit.com, utilizing a Java Microservices architecture for scalable back-end development.",
                    "Drove significant system efficiency and modernization by implementing Spring Boot 3 and leveraging multithreading techniques, resulting in a 20% overall performance improvement.",
                    "Handled the entire data and presentation layer, implementing the Hibernate ORM with H2DB for data persistence and integrating back-end services with the UI built using JSP (Java Full Stack).",
                    "Designed and enforced core application structure by utilizing the Spring framework and applying industry-standard patterns like the Java Singleton Architecture for resource management.",
                    "Contributed to specialized technical requirements, including complex report generation using JRXML and the implementation of security components using C++ (STL) and cryptography principles.",
                ],
                learnings=[
                    "Learned to develop and scale enterprise applications by applying Java Microservices architecture with Spring and Spring Boot.",
                    "Gained critical knowledge in performance tuning, specifically how to achieve 20% system efficiency gains using multithreading and modern Spring Boot 3 features.",
                    "Acquired full-stack proficiency, learning to manage data persistence with Hibernate and H2DB, and integrating the back-end with the JSP view layer.",
                    "Developed foundational versatility by learning specialized tools like JRXML for reporting and implementing low-level concepts using C++ (STL) and cryptography.",
                ],
            ),
        ]

    def get_projects(self) -> List[Project]:
        return [
            Project(
                name="Expense Tracker",
                description="Android app to track daily and monthly expenses using Kotlin, Jetpack Compose, MVVM, Room-DB, Coroutines.",
                technologies=[
                    "Kotlin",
                    "Jetpack Compose",
                    "MVVM",
                    "Room-DB",
                    "Coroutines",
                ],
                link="https://github.com/shantanubindhani/Expense-tracker",
            ),
            Project(
                name="Melodic Hues",
                description="Web app recommending songs based on facial expressions using Deep Learning and Flask, supporting multiple languages.",
                technologies=["Python", "Flask", "CNN", "Deep Learning"],
                link="https://github.com/shantanubindhani/Melodic-Hues",
            ),
        ]

    def get_educations(self) -> List[Education]:
        return [
            Education(
                degree="Masters in Computer Applications",
                grade=Grade(score=8.68, scale=10.0),
                institution="Lovely Professional University, Punjab",
                graduation_date=date(2025, 5, 1),
                additional_info=None,
            ),
            Education(
                degree="Bachelors in Computer Application",
                grade=Grade(score=8.75, scale=10.0),
                institution="Rai University, Ahmedabad",
                graduation_date=date(2023, 5, 1),
                additional_info=None,
            ),
        ]

    def get_skills(self) -> List[Skill]:
        _skills = [
            Skill(name="Python", type=SkillType.LANGUAGE, level=SkillLevel.EXPERT),
            Skill(name="C++", type=SkillType.LANGUAGE, level=SkillLevel.ADVANCED),
            Skill(name="Java", type=SkillType.LANGUAGE, level=SkillLevel.ADVANCED),
            Skill(name="Kotlin", type=SkillType.LANGUAGE, level=SkillLevel.BEGINNER),
            Skill(
                name="JavaScript",
                type=SkillType.LANGUAGE,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(name="SQL", type=SkillType.TECHNOLOGY, level=SkillLevel.ADVANCED),
            Skill(name="Git", type=SkillType.TOOL, level=SkillLevel.EXPERT),
            Skill(name="BASH", type=SkillType.TOOL, level=SkillLevel.ADVANCED),
            Skill(name="FastAPI", type=SkillType.FRAMEWORK, level=SkillLevel.ADVANCED),
            Skill(
                name="Spring Boot",
                type=SkillType.FRAMEWORK,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(name="Docker", type=SkillType.TOOL, level=SkillLevel.INTERMEDIATE),
            Skill(name="Kubernetes", type=SkillType.TOOL, level=SkillLevel.BEGINNER),
            Skill(name="Celery", type=SkillType.TOOL, level=SkillLevel.INTERMEDIATE),
            Skill(
                name="PostgreSQL", type=SkillType.TECHNOLOGY, level=SkillLevel.ADVANCED
            ),
            Skill(
                name="REST APIs", type=SkillType.TECHNOLOGY, level=SkillLevel.ADVANCED
            ),
            Skill(
                name="Microservices",
                type=SkillType.TECHNOLOGY,
                level=SkillLevel.ADVANCED,
            ),
            Skill(name="JUnit", type=SkillType.TOOL, level=SkillLevel.BEGINNER),
            Skill(
                name="JWTAuth", type=SkillType.TECHNOLOGY, level=SkillLevel.INTERMEDIATE
            ),
            Skill(
                name="Android Development",
                type=SkillType.TECHNOLOGY,
                level=SkillLevel.BEGINNER,
            ),
            Skill(
                name="Jetpack Compose",
                type=SkillType.FRAMEWORK,
                level=SkillLevel.BEGINNER,
            ),
            Skill(
                name="Coroutines", type=SkillType.TECHNOLOGY, level=SkillLevel.BEGINNER
            ),
            Skill(
                name="Flask", type=SkillType.FRAMEWORK, level=SkillLevel.INTERMEDIATE
            ),
            Skill(name="CNN", type=SkillType.TECHNOLOGY, level=SkillLevel.BEGINNER),
            Skill(
                name="Deep Learning",
                type=SkillType.TECHNOLOGY,
                level=SkillLevel.BEGINNER,
            ),
            Skill(name="Pytest", type=SkillType.TOOL, level=SkillLevel.ADVANCED),
            Skill(
                name="System Design",
                type=SkillType.CONCEPT,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(
                name="Multiprocessing",
                type=SkillType.TECHNOLOGY,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(name="Sentry", type=SkillType.TOOL, level=SkillLevel.BEGINNER),
            Skill(name="Codecov", type=SkillType.TOOL, level=SkillLevel.BEGINNER),
            Skill(
                name="Python-Typing", type=SkillType.CONCEPT, level=SkillLevel.BEGINNER
            ),
            Skill(
                name="Data Structures & Algorithms",
                type=SkillType.CONCEPT,
                level=SkillLevel.ADVANCED,
            ),
            Skill(
                name="OOPs Concepts", type=SkillType.CONCEPT, level=SkillLevel.EXPERT
            ),
            Skill(
                name="Design Patterns",
                type=SkillType.CONCEPT,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(
                name="Agile", type=SkillType.METHODOLOGY, level=SkillLevel.INTERMEDIATE
            ),
            Skill(
                name="Scrum", type=SkillType.METHODOLOGY, level=SkillLevel.INTERMEDIATE
            ),
            Skill(
                name="Unit Testing",
                type=SkillType.METHODOLOGY,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(
                name="Integration Testing",
                type=SkillType.METHODOLOGY,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(
                name="Repository Testing",
                type=SkillType.METHODOLOGY,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(
                name="Multithreading", type=SkillType.CONCEPT, level=SkillLevel.BEGINNER
            ),
            Skill(
                name="JRXML", type=SkillType.TECHNOLOGY, level=SkillLevel.INTERMEDIATE
            ),
            Skill(
                name="CI/CD", type=SkillType.METHODOLOGY, level=SkillLevel.INTERMEDIATE
            ),
            Skill(
                name="Github Workflows",
                type=SkillType.TOOL,
                level=SkillLevel.INTERMEDIATE,
            ),
            Skill(name="Linux", type=SkillType.TECHNOLOGY, level=SkillLevel.ADVANCED),
            Skill(name="VS Code", type=SkillType.TOOL, level=SkillLevel.EXPERT),
            Skill(name="Eclipse", type=SkillType.TOOL, level=SkillLevel.ADVANCED),
            Skill(
                name="Android Studio", type=SkillType.TOOL, level=SkillLevel.BEGINNER
            ),
            Skill(name="Postman", type=SkillType.TOOL, level=SkillLevel.INTERMEDIATE),
            Skill(name="DBeaver", type=SkillType.TOOL, level=SkillLevel.INTERMEDIATE),
            Skill(name="C#", type=SkillType.LANGUAGE, level=SkillLevel.BEGINNER),
            Skill(
                name="HTML/CSS", type=SkillType.TECHNOLOGY, level=SkillLevel.ADVANCED
            ),
            Skill(name="ReactJS", type=SkillType.FRAMEWORK, level=SkillLevel.BEGINNER),
            Skill(name="GitHub", type=SkillType.TOOL, level=SkillLevel.ADVANCED),
        ]

        return _skills

    def get_certifications(self) -> List[Certification]:
        return [
            Certification(
                name="Java (Basic) Certificate",
                organization="Hackerrank",
                issue_date=date(2024, 8, 1),
                expiration_date=None,
                url="https://www.hackerrank.com/certificates/3fbe9c798cd2",
            ),
            Certification(
                name="Software Engineer Certificate",
                organization="Hackerrank",
                issue_date=date(2024, 8, 1),
                expiration_date=None,
                url="https://www.hackerrank.com/certificates/3760edda3156",
            ),
            Certification(
                name="Mastering Android Development with Kotlin From Beginner to Pro Certification",
                organization="GFG",
                issue_date=date(2024, 6, 1),
                expiration_date=date(2024, 7, 31),
                url="https://www.geeksforgeeks.org/certificate/bdb05332ac99bedba18c420cbb25445f",
            ),
            Certification(
                name="Jetpack Compose & Kotlin & Java for Android App Development Certification",
                organization="Udemy",
                issue_date=date(2024, 4, 1),
                expiration_date=date(2024, 7, 31),
                url="https://www.udemy.com/certificate/UC-f88e1672-eaa9-4442-a3aa-e07c0f69468c/",
            ),
            Certification(
                name="The Complete Python Developer Certification",
                organization="Udemy",
                issue_date=date(2024, 1, 1),
                expiration_date=date(2024, 6, 30),
                url="https://www.udemy.com/certificate/UC-0096b90f-42cf-4135-9b89-947b437d09bd/",
            ),
        ]


portfolio = DataSource_provider().get_instance()
