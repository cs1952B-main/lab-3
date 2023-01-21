from enum import Enum
from data.applicant.applicant import Applicant
from data.employer.employer import Employer

# Shared classes that will need to be used by both applicants and employers data class implementations

class ApplicationStatus(Enum):
    DRAFTING = 0
    RECEIVED = 1
    REVIEWED = 2
    HIRED = 3
    REJECTED = 4

#TODO: Is there a better word than type to represent this.... ?
class JobType(Enum):
    VOLUNTEER_WORK = 0
    INTERNSHIP = 1
    PART_TIME = 2
    FULL_TIME = 3
    OTHER = 4

class DegreeLevel(Enum):
    BELOW_HIGHSCHOOL = 0
    HIGHSCHOOL_DIPLOMA = 1
    ASSOCIATES_DEGREE = 2
    BACHELORS_DEGREE = 3
    MASTERS = 4
    PHD_AND_ABOVE = 5

class Application:
    def __init__(self, applicant : Applicant, employer : Employer, date, app_status : ApplicationStatus):
        self.applicant = applicant
        self.employer = employer
        self.date = date
        self.status = app_status
        
class Company:
    def __init__(self, name, size, location, employees_with_jobs_posted: set[Employer]):
        self.name = name
        self.size = size
        self.location = location
        self.employees_with_jobs_posted = employees_with_jobs_posted
    
    def addEmployeeJobPosting(self, Employee):
        self.employees_with_jobs_posted.add(Employee)