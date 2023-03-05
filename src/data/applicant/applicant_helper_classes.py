from enum import Enum
from helper_classes import *

class Demographics:
    def __init__(self, age, gender, race, ethnicity, sexual_orientation, marital_status, country_of_residence):
        self.age = age
        self.gender = gender
        self.race = race
        self.ethnicity = ethnicity
        self.sexual_orientation = sexual_orientation
        self.marital_status = marital_status
        self.country_of_residence = country_of_residence

class Education:
    def __init__(self, highest_DL : DegreeLevel, hDL_institution, degree_field, gpa, start_date, end_date, is_completed : bool):
        self.highest_DL = highest_DL
        self.hDL_institution = hDL_institution
        self.degree_field = degree_field
        self.gpa = gpa
        self.start_date = start_date
        self.end_date = end_date
        self.is_completed = is_completed 

class Experience:
    def __init__(self, type : JobType, field, title, start_date, end_date):
        self.type = type
        self.field = field
        self.job_title = title
        self.start_date = start_date
        self.end_date = end_date

class WorkExperience:
    def __init__(self, experiences: list[Experience]):
        experiences.sort(key = lambda ex : ex.start_date) #sorts experiences by start date
        self.work_history = experiences.copy 

    def addExperience(self, experience):
        self.work_history.append(experience)
        self.work_history.sort(key = lambda ex : ex.start_date) #sorts work_history by start date

class Preferences:
    def __init__(self, salary, location, field, years_of_ex, type : JobType, target_companies : list[Company]):
        self.salary = salary
        self.location = location
        self.field = field
        self.years_of_ex = years_of_ex
        self.type = type
        self.target_companies = target_companies

class ApplicationsSent:
    def __init__(self, apps_sent : set[Application]):
        self.apps_sent = apps_sent
    
    def sendApplication(self, app : Application):
        self.apps_sent.add(app)