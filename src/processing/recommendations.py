'''
TODO: 

    FUNCTIONALITY REQUIREMENT:
    REQ-C: HireSense should ingest information it knows about an Applicant, then using this information (and perhaps other relevant information
           on the platform) it should make useful, tailored recommendations to the Applicant of a few Employers who have posted a job they might
           find interesting.
    REQ-D: HireSense should ingest information it knows about the job an Employer posted then using this information (and other relevant information)
           it should make useful and fair tailored recommendations to the Employer of a few Applicants who have active profiles on the platform 
           whom they may be interested in reaching out to.

    STUDENT IMPLEMENTATION:

    Students will need to:
    - Define what makes a recommendation "useful" or "fair" for their purposes
    - What Applicant and Employer information is fair and relevant to use in these recommendations?
    - How will the algorithm make it's recommendations? This is where providing a few examples may be helpful and productive:
        a) Simple recommendation system which ingests "immutable" attributes of Applicant/Employer profile to filter through Employers/Applicants
        b) "Individual" recommendations system which ingest immutable attributes as well as user interactions on the platform and takes these
           both together to output tailored recommendations that reflect user preferences over time
        c) More complex collaborative filtering recommendations which matches users to "similar" users based on key profile/interaction characteristics,
           examines past outcomes of these "similar" user, and leverages those to make recommendations to Applicants/Employers
    - Will these recommendations be one-sided or two-sided matching?
        - ie. if we recommend an Employer to an Applicant, should we also recommend that Applicant to the Employer?
    
    Dev Questions:
        Should we supply a class they could fill in to track user interactions with the platform to incorporate into their recommendation 
        model if they so choose? Or should we keep it simple?
            - Would it be enough to simply provide instructions about where they should put a new attribute in a helper class if they
              pursue this method of algorithmic recommendation?

'''