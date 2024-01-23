from position.position_helper_classes import *
from helper_classes import *

'''
    The position class represents a single job posting on the HireSense platform. This class is a container for the 
    information about the job like title, field, salary, job description etc. While a Company may have multiple Positions within it,
    each Position represents a single job on the platform. In short, you can think of a Position as a 
    a role within a larger company or within a small business.

    Company - the larger Company to which the Position belongs
    SalaryInfo - the low, high, and median salary for this position
    JobDescription - background info about the job: job title, type, field, location, responsibilities, etc
    JobRequirements - requirements for applicants to the role: degree level, field of study, years of experience, etc
    ApplicationsReceived - a wrapper class around a set of applications received by for the position
'''

class Position:
    def __init__(self, company : Company, salary : SalaryInfo, job_desc : JobDescription, job_req : JobRequirements, applicants : ApplicationsReceived):
        self.company = company
        self.salary = salary
        self.job_description = job_desc
        self.job_requirements = job_req
        self.applicants = applicants
