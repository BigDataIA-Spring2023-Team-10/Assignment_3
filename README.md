# Assignment 3

#  Geospatial  API as a service.


[![PyPI](https://img.shields.io/pypi/pyversions/locust.svg)](https://pypi.org/project/locust/)



# Codelabs link

[Code Labs Link](https://codelabs-preview.appspot.com/?file_id=1nghIHlS4LUmvoRvo3yWZrO-jxsyU_Wz35ny6Q_JB0RQ#2)








#  Overview

We are in a scenario where users are making API requests on a daily basis to fetch the GOES and NEXRAD data. As part of this assignment, our objective is to keep track of the API requests that have been made by the user and based upon the API usage users can be categorized into various tiers which can later be charged as service based upon the API requests.




# Process Outline

1. Made a few public and private endpoints based upon the user authentication to access the Metadata.

2. Based on the user API endpoint usage created by the three different tiers here are the details of the tentative service plan that has been created.
Free - 10 API requests per user
Gold- 15 API requests per user
Platinum -20 API requests per day

3. Created a functionality that enabled login for user and admin which then had visibility about the API responses made

4. We used cloud watch to track the activity of the user API hit and at the same time used this to visualize it in order to compare it with various users

5. Created a CLI that helped in checking the FastAPI responses and at the same time creating users details from the command line Interface

6. Created a DAG to scrape the Metadata on daily basis using daily basis, populate the collected data into a database and export all the data into an Excel sheet and run a Great Expectation data quality report to ensure data quality





## How to use  this project:


1. Clone this repo locally `git clone <repo-url>`

2. Setup the local python enviornment.

3. Install all the dependencies from the requirements.txt file
`pip install -r requirements.txt`

4. Install all local dependencies 
`pip install -e .`

5. Create `.env` file.











### Team Member

| NUID | Team Member       |
|:-----:|---------------|
| 002766036       | Anuj Kumar |
| 002794258      |  Hitesh  Pant            |
| 002773080      |  Kunal Bhoyar              |
| 002772221      |  Snehashis Lenka              |


WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK.
