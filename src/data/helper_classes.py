from enum import Enum
from data.applicant.applicant import Applicant
from data.position.position import Position

# Shared classes that will need to be used by both applicants and positions data class implementations

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
  This class represents the Applicant's application to a Position. It contains both the Applicant and Position
  as well as the date it was sent and the application status.

  Applicant - the applicant whose application this is
  Position - the job recieving the applicant's application
  date - the date the application was sent in
  app_status - where the application is in the hiring process
  
''' 
class Application:
    def __init__(self, applicant : Applicant, position : Position, date, app_status : ApplicationStatus):
        self.applicant = applicant
        self.position = position
        self.date = date
        self.status = app_status

'''
  The Company class represents the larger company where positions are held. The class contains information about the company name, size, location,
  and a list of company positions that are currently open and being posted on the HireSense platform. When HireSense does equitable hiring analyses,
  they do it at the Company level, not the Position level.

  name - the name of the company
  size - the number of employees working for the company
  location - the location of the main office/headquarters of the company
  positions_posted - a set of Positions within the Company that have postings on HireSense
  
'''   
class Company:
    def __init__(self, name, size, location, positions_posted: set[Position]):
        self.name = name
        self.size = size
        self.location = location
        self.positions_posted = positions_posted
    
    def addPositionPosting(self, posting : Position):
        self.positions_posted.add(posting)


# -------------------------------------------------------------------------------------------------- #

#NOTE: ONLY FILL THIS IN IF YOU NEED IT FOR YOUR RECOMMENDATIONS IN STEP 4-B, see recommendations.py for more details
'''
    Fill in this class with any attributes/fields you think would be helpful data to collect!
    We have also provided separate classes for applicant and position which inherit from the UserInteractions class if you'd like
    To collect some Applicant/Position specific metrics 
'''
class UserInteractions:
    def __init___(self, ____):
        pass

# # UNCOMMENT TO USE THESE CLASSES
# class ApplicantUserInteractions(UserInteractions):
#     def __init___(self, ____):
#         super().__init___(____) #call to the parent class, pass the UserInteractions arguments (if there are any) here!
#         #insert Applicant specific interation attributes here

# class PositionUserInteractions(UserInteractions):
#     def __init___(self, ____):
#         super().__init___(____) #call to the parent class, pass the UserInteractions arguments (if there are any) here!
#         #insert Position specific interation attributes here
