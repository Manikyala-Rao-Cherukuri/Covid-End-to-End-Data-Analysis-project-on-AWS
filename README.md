# Covid_19-Data_Engineering-End-to-End-Data-Analysis-project-on-AWS

### Steps floowed:
##### Data Collection:
-	Download the COVID dataset from an open source data repository, such as AWS (https://aws.amazon.com/covid-19-data-lake/)
-	Created an S3 bucket on AWS and upload the data files to the bucket from local storage.
##### Data Ingestion:
-	Created a database on AWS Glue.
-	Create a crawler on AWS Glue and connected it with the S3 bucket where the data files are stored.
-	Run the crawler to populate the database with the data.
##### Data Analysis:
-	Used Athena to query and analyse the data stored in the Glue database and stored tables/ query result in to output folder in the S3 storage bucket.
-	Used to SQL to understand about COVID-19 data, such as the number of cases per day, per region, or per country.
##### Data Transformation:
-	Created a Glue ETL Job to transform the data from the Glue database into a format that can be loaded into a data warehouse.
-	Write a script to create dimensional and fact tables using the redshift connector in Python.
-	Use the "copy" command to upload the transformed data from the S3 bucket into the newly created tables in the data warehouse.
##### Business Analysis (Further Usage of DWH Data):
Analyze the data in the data warehouse using SQL queries to generate insights about COVID-19 trends and patterns.
Use visualization tools such as Tableau or Power BI to create charts and graphs that summarize the findings.
Share the insights with stakeholders in the business to help inform decisions related to COVID-19.
#### Skill/ Tools Used: Python, Postgre SQL, ETL, Building Data Models & AWS - Athena, Glue, Redshift, S3, IAM
![image](https://github.com/Manikyala-Rao-Cherukuri/Covid-End-to-End-Data-Analysis-project-on-AWS/assets/119756215/7331dbe3-befa-418d-b3c7-f597eb08b36c)
