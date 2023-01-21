from applicant.applicant_helper_classes import *

'''
    The applicant class represents a job applicant user on the HireSense platform. This class is a container for applicant
    data, including personal information, background information, job preferences, and current applications.

    Demographics - personal categorical data; ex) gender, race, age... etc
    Education - highest level of degree achieved and additional details about that degree
    WorkExperience - list of past work experiences with relevant details about field, type, start/end dates
    Preferences - a data class to encapsulate job search preferences of the applicant field, type, salary, etc ... TODO: Update this description if we decide to let students fill in prefs
    ApplicationsSent - a wrapper class around a set of applications sent by the applicant
'''
class Applicant:
    def __init__(self, demo : Demographics, educ : Education, work_ex : WorkExperience, prefs : Preferences, apps: ApplicationsSent):
        self.demographics = demo
        self.education = educ
        self.work_experience = work_ex
        self.preferences = prefs
        self.applications = apps