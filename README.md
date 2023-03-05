# Code Organization Reference

## Data Classes

The data classes are all located inside src -> data

1) src -> data -> applicant contains the Applicant data class as well as Applicant specific helper classes that essentially serve as containers
for different types of information included in the Applicant profile

2) src -> data -> employer contains the Employer data class as well as Employer specific helper classes that serve as contains for different types of information included in the Employer profile/job posting

3) src -> data -> helper_classes.py contains helper classes used by both the Applicant and Employer classes like Application or Company

## Processing Files

The processing files are located in src -> processing. These are the files represent the majority of the part of the assignment you will be interacting with. There are 3 files that correspond to different functionality requirements or pairs of functionality requirements. Each file presently contains a detailed comment outlining the requirement and helpful hints and ideas to help you get started.