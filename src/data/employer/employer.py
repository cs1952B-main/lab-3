from employer.employer_helper_classes import *
from helper_classes import *

'''
    The employer class represents an employer with a single job posting on the HireSense platform. This class is a container for the 
    information about the job like title, field, salary, job description etc. While a Company may have multiple Employers within it,
    each Employer may only post one job at a time on the platform for simplicity's sake. In short, you can think of an Employer as a 
    manager of a small team that has a role to fill within a larger company or within a small business.

    Company - the larger Company to which the Employer belongs
    SalaryInfo - the low, high, and median salary for this position
    JobDescription - background info about the job: job title, type, field, location, responsibilities, etc
    JobRequirements - requirements for applicants to the role: degree level, field of study, years of experience, etc
    ApplicationsReceived - a wrapper class around a set of applications received by the employer
'''

class Employer:
    def __init__(self, company : Company, salary : SalaryInfo, job_desc : JobDescription, job_req : JobRequirements, applicants : ApplicationsReceived):
        self.company = company
        self.salary = salary
        self.job_description = job_desc
        self.job_requirements = job_req
        self.applicants = applicants