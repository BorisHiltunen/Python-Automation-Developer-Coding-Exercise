# Plan

Python Automation Developer - Coding Exercise

## Overview
- **Name:** RPA coding exercise (Form Filler)
- **Summary:** App that fetches data from excel file and pushes that data to a form page's input elements

## Tasks
- **Plan for the app**
  - **Status:** Done

- **Functionality for the data fetching and possible reformatting of the data**
  - **Status:** Done

- **Functionality for establishing connection to the rpa challenge page**
  - **Status:** Done

- **Functionality for sending the previous challenge data to the rpa challenge page's input fields.**
  - **Status:** Done

## App structure
- **Docs:** Contains all the necessary documentation except for the main readme.md
  - flowchart.png
  - flowchart.html
  - plan.md
- **form_filler:** Contains the app's functionality
  - excel.py
  - selenium.py
- **tests:** Contains the necessary tests
- main.py

## Dependencies
- **Pandas:** Will be used to read and possibly edit the challenge.xlsx excel's data
- **Selenium:** Will be used to establish a connection to the form page and to fill the input fields with the previously fetched excel data 
- **Pytest:** Will be used for testing


