from data.helper_classes import *
'''
TODO: 

    FUNCTIONALITY REQUIREMENT:
    REQ-C: HireSense should ingest information it knows about an Applicant, then using this information (and perhaps other relevant information
           on the platform) it should make useful and fair tailored recommendations to the Applicant of a few Employers who have posted a job they might
           find interesting.
    REQ-D: HireSense should ingest information it knows about the job an Employer posted then using this information (and other relevant information)
           it should make useful and fair tailored recommendations to the Employer of a few Applicants who have active profiles on the platform 
           whom they may be interested in reaching out to.

    STEP 4-B: 
        For this task you will first want to define what makes a recommendation "useful" and "fair" for HireSense's purposes. You can do this
        explicitly in a "REFLECTION:" comment or just have it in your mind as you code. Be sure to have some sense though, it will help you
        on your written questions later on. 

        You'll want to think about what Applicant and Employer data to use in your recommendations. What best represents reality? 
        Could using certain data points open the door for discrimination? Could your algorithm reflect an unfair bias? Next you'll want 
        to choose a method for the recommendation system, we've provided a few ideas for you to choose from, though you may use something 
        else as long as it's clear from your code how the system establishes connections between data points, what data points it is using,
        and whether these recommendations are based solely on each user's data, based solely on similar users' data, or both.

        Some potential recommendation algorithms to explore:

            a) A simple if-then system which ingests "immutable" attributes of an Applicant/Employer profile to filter
            through recommended Employers/Applicants. Essentially, this would have hard-coded rules on how to filter through 
            and intelligently provide recommendations. This kind of system gives you as the programmer the most control over and 
            insight into how the code reaches it's decisions.

            b) "Individual" recommendations system which ingests immutable attributes as well as user interactions on the platform. It will combine
            both of these data sources together to output tailored recommendations which reflect static as well as dynamic user preferences over time.
            If you choose to pursue this route, you will need to fill in the UserInteractions class located in helper_classes.py to determine what
            kinds of user interaction data you will collect (ex: fields most viewed, time spent on a profile, # of times a profile is visited, etc.).

            c) A more complex collaborative filtering recommendations system which matches users to "similar" users based on key profile and/or interaction 
            characteristics, examines the past outcomes of "similar" users, and leverages these connections to make recommendations to Applicants/Employers.

            d) Other! If you think you have a better method, feel free to implement it so long as it is clear (and perhaps commented) so that we can 
            understand what data it is using, how it is using that data, and what the recommendations are based on.

        NOTE: These are not rigid options, you can combine or reinterpret them as you see fit. You can also choose to use the UserPreferences class
        regardless of how you implement the recommendations if you think it will prove useful.

        NOTE: Remember that we don't expect you to write functional code, if you don't know how to do something or how to implement a piece of
        your recommendation algorithm or want to make a fake call to a method, use pseudocode! Just make sure whatever you are doing is clear
        and be sure to specify what and how a pseudocoded section might accomplish its task, even if you can't write the code that would 
        actually do it.

'''

class Recommender: 
    
    #TODO: Fill in the arguments and method with an implementation that satisfies functionality REQ-C
    def recommend_employers_to_applicant(self, ___):
        pass

    #TODO: Fill in the arguments and method with an implementation that satisfies functionality REQ-D
    def recommend_applicants_to_employers(self, ___):
        pass


