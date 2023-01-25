from data.helper_classes import *
'''
    FUNCTIONALITY REQUIREMENTS:

    REQ-A: Applicants should be able to search for jobs. Since each Employer may only post 1 job, Applicants are essentially searching in the 
        subspace of Employers. Regardless of how this is implemented, it should be a useful tool for helping Applicants to sift through all 
        of the Employers who have posted jobs on the platform and try to find jobs that match their preferences and profile.

    REQ-B: Employers should be able to search for Applicants. This would allow Employers to reach out to these Applicants to encourage them to 
        apply for their job posting. Regardless of how this is implemented, it should be a useful tool for helping Employers to search for and
        find Applicants that would be a good fit for their job posting based on the job's requirements and description.

    STEP 5-A:
        For this task you will need to choose how to implement simple search for applicants and employers. In addition to the data classes
        you've already looked at, we've provided most of the implementation for simple search below. Your task is to choose between two methods
        of implementation: keyword search and full-text search. Be sure to think about --why-- you're making the choice you are and consider
        what it will mean for different types of users and the power dynamics present on a hiring/jobs platform. You will need to select a 
        method for both the applicant search and the employer search, they do --not-- need to be the same.

        KEYWORD SEARCH: There is map (or dictionary) of different categories of keyword to filter the search results by and pre-selected values
                        for those categories that users can click on to filter their search results. To search, users pick value(s) for whichever
                        categories they want to filter by, press enter, and receive results that match their search.

                        Challenges/Considerations: 
                            - Could we accidentally filter out jobs by having limited values for the keyword categories?
                            - Is the list of keywords fixed or should we intelligently generate them?
                            - Do we create keywords using data from the existing applicants/employers on the platform?
                            - Who supplies the keywords?

        FULL-TEXT SEARCH: Users simply enter a query into a search bar, stop words are filtered out, and then the search is matched against the
                          text of data for Applicants or Employees for similarity. Most relevant results as determined by term frequency/relevancy
                          to the prompt as returned.

                          Challenges/Considerations
                            - What if users miss out because of bad searches or bad descriptions/titles?
                            - Is there anything we won't allow users to search for?
                            - What data will we use to match queries on? 
                                - Is there any way for users to disallow the use of certain data?
'''
class SimpleSearch:

    APPLICANT_SEARCH_KEYWORD_DICT = {
        "field" : ["Medicine", "Tech", "Business", "Finance", "Law", "Administration", "Education", "Other"],
        "type" : ["Volunteer", "Internship", "Part-Time", "Full-Time", "Other"],
        "salary" : ["< 30k", "30k - 50k", "50k - 80k", "80k - 120k", "120k - 200k", "200k+"],
        "distance" : ["1 mile" "1-5 miles", "5-10 miles", "10-20 miles", "20-50 miles", "50+ miles"],
        "company_size" : ["100 or fewer employees", "100-500 employees", "500-1500 employees", "1500 - 5000 employees", "5000 - 10000 employees", "10000+ employees"],
        "degree_level" : ["below highschool", "highschool diploma", "associates degree", "bachelors degree", "masters", "phd and above"]
    }

    EMPLOYER_SEARCH_KEYWORD_DICT = {
        "field" : ["Medicine", "Tech", "Business", "Finance", "Law", "Administration", "Education", "Other"],
        "years_of_experience" : ["0-1", "2-5", "5-9", "10+"],
        "degree_level" : ["below highschool", "highschool diploma", "associates degree", "bachelors degree", "masters", "phd and above"],
        "distance" : ["1 mile" "1-5 miles", "5-10 miles", "10-20 miles", "20-50 miles", "50+ miles"],
    }


    #TODO: Fill in the 
    def do_keyword_search(self, ___):
        results = ...
        return results

    def do_full_text_search(self, ___):
        results = ...
        return results

    #TODO: Choose either keyword or full text for the search feature applicants will use to search for employers/jobs to satisfy REQ-A
    def applicant_search_for_employer(self, applicant : Applicant, all_employers : list[Employer]):
        pass

    #TODO: Choose either keyword or full text for the search feature employers will use to search for applicants to satisfy REQ-B
    def employer_search_for_applicants(self, employer : Employer, all_potential_applicants : list[Applicant]):
        pass