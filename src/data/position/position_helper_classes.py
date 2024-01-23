from helper_classes import *
class SalaryInfo:
    def __init__(self, low, high, median):
        self.low = low
        self.high = high
        self.median = median  

class JobDescription:
    def __init__(self, title, type : JobType, field, location, responsibilities : list[str], blurb):
        self.title = title
        self.type = type
        self.field = field
        self.location = location
        self.responsibilities = responsibilities
        self.blurb = blurb

class JobRequirements:
    def __init__(self, years_of_experience, degree_level : DegreeLevel, degree_field, other_requirements : list[str]):
        self.years_of_experience = years_of_experience
        self.degree_level = degree_level
        self.degree_field = degree_field
        self.other_requirements = other_requirements
        
class ApplicationsReceived:
    def __init__(self, apps : set[Application]):
        self.applications = apps

    def receiveApplication(self, app : Application):
        self.applications.add(app)
