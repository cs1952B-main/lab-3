from enum import Enum
from data.applicant.applicant import Applicant
from data.employer.employer import Employer

# Shared classes that will need to be used by both applicants and employers data class implementations

class ApplicationStatus(Enum):
    DRAFTING = 0
    RECEIVED = 1
    REVIEWED = 2
    OFFERED = 3
    HIRED = 4
    DECLINED = 5
    REJECTED = 6

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


'''
  This class represents the Applicant's application to an Employer’s position. It contains both the Applicant and Employer
  as well as the date it was sent and the application status.

  Applicant - the applicant whose application this is
  Employer - the employer who is receiving the application for their job posting
  date - the date the application was sent in
  app_status - where the application is in the hiring process
  
''' 
class Application:
    def __init__(self, applicant : Applicant, employer : Employer, date, app_status : ApplicationStatus):
        self.applicant = applicant
        self.employer = employer
        self.date = date
        self.status = app_status

'''
  The Company class represents the larger company where employers work. The class contains information about the company name, size, location,
  and a list of company employees who are currently posting jobs on the HireSense platform. When HireSense does equitable hiring analyses,
  they do it at the Company level, not the Employer level.

  name - the name of the company
  size - the number of employees working for the company
  location - the location of the main office/headquarters of the company
  employees_with_jobs_posted - a set of Employers that work for the company with job postings on HireSense
  
'''   
class Company:
    def __init__(self, name, size, location, employees_with_jobs_posted: set[Employer]):
        self.name = name
        self.size = size
        self.location = location
        self.employees_with_jobs_posted = employees_with_jobs_posted
    
    def addEmployeeJobPosting(self, employee : Employer):
        self.employees_with_jobs_posted.add(employee)


# -------------------------------------------------------------------------------------------------- #

#NOTE: ONLY FILL THIS IN IF YOU NEED IT FOR YOUR RECOMMENDATIONS IN STEP 4-B, see recommendations.py for more details
'''
    Fill in this class with any attributes/fields you think would be helpful data to collect!
    We have also provided separate classes for applicant and employer which inherit from the UserInteractions class if you'd like
    To collect some Applicant/Employer specific metrics 
'''
class UserInteractions:
    def __init___(self, ____):
        pass

# # UNCOMMENT TO USE THESE CLASSES
# class ApplicantUserInteractions(UserInteractions):
#     def __init___(self, ____):
#         super().__init___(____) #call to the parent class, pass the UserInteractions arguments (if there are any) here!
#         #insert Applicant specific interation attributes here

# class EmployerUserInteractions(UserInteractions):
#     def __init___(self, ____):
#         super().__init___(____) #call to the parent class, pass the UserInteractions arguments (if there are any) here!
#         #insert Employer specific interation attributes here