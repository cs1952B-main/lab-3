'''
TODO: 

    FUNCTIONALITY REQUIREMENT:
    REQ-A: Applicants should be able to search for jobs. Since each Employer may only post 1 job, Applicants are essentially searching in the 
    subspace of Employers. Regardless of how this is implemented, it should be a useful tool for helping Applicants to sift through all 
    of the Employers who have posted jobs on the platform and try to find jobs that match their preferences and profile.

    REQ-B: Employers should be able to search for Applicants. This would allow Employers to reach out to these Applicants to encourage them to 
        apply for their job posting. Regardless of how this is implemented, it should be a useful tool for helping Employers to search for and
        find Applicants that would be a good fit for their job posting based on the job's requirements and description.

    STUDENT IMPLEMENTATION:
    Two possibilities, we could ask students to implement these or fill them in for them.

    OPTION 1: FILL IN FOR THEM
        Fill this in with the simple search methods that we will not ask students to implement which
        are currently labeled functionality requirements A and C. 
            A: Allow applicants to search for jobs
            B: Allow employers to search for applicants

        The idea is that instead of giving students too much information in the document itself on how to provide code for this
        assignment and where to "real" code and where to pseudocode, we can provide this as a concrete example for them to refer
        back to.

    OPTION 2: ASK TO IMPLEMENT
        This could still serve as an "intro" to the assignment and a first step to get the thinking about the different 
        kinds of SRC challenges present in these data collection and processing choices for the rest of assignment. 
        To cut down on work load a little and have this serve as the "intro" part, we could supply students with options
        to choose from, rather than allowing them total freedom to prevent them from going off the deep end and demonstrate
        the kinds of questions we're trying to wrestle with.

        I think this might be especially interesting if students have to consider whether the employer side search
        should be more limited than the applicant side search. (Essentially how do we manage the power dynamics between
        employers and applicants in the functionality of the tooling we provide them?)

        Could allow them to choose between:
        1) keyword search 
            - Challenges with what keywords to allow, could we accidentally filter out jobs?
            - Fixed list of keywords or allow user-generated ones as well?
            - Do we create keywords using some of the employer/job data?
        2) user-generated "classic" search query of job descriptions/titles
            - What if users miss out on jobs because of bad searches or bad descriptions/titles?

'''
