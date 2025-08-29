# Python-Automation-Developer-Coding-Exercise
A coding exercise focused on web automation using Python.

## Description
Fetches data from the challenge.xlsx file that will be downloaded from the rpachallenge page.
Then fills the rpachallenge page's input fields with the fetched data.

## Flowchart
![picture_of_the_flowchart](https://github.com/BorisHiltunen/Python-Automation-Developer-Coding-Exercise/blob/main/docs/Flowchart.png)

## Tools and Libraries
- [Pandas](https://pandas.pydata.org/)
- [Selenium](https://www.selenium.dev/)
- [Pytest](https://docs.pytest.org/en/stable/)
- You can find required packets from requirements.txt

## Setup
1. Clone or fork the repository.
2. Install virtualenv if not already installed
```
pip install virtualenv
```

3. Make an Virtual Environment
```
virtualenv env
```

4. Access it
    - Windows
    ```
    .\env\Scripts\activate
    ```
    - Mac
    ```
    source env/bin/activate
    ```

5. Install requirements.txt
```
pip install -r requirements.txt
```
- If installing the requirements.txt fails you can also install dependencies one by one:
    ```
    pip install pandas
    ```
    ```
    pip install openpyxl
    ```
    ```
    pip install selenium
    ```
    ```
    pip install pytest
    ```
6. Install the "challenge.xlsx" from the [RPA Challenge](https://rpachallenge.com/) page
  - After installing add the file to the app's files folder

7. Run the code
    - Normal run
    ```
    python main.py normal_mode
    ```
    - Performance mode run
    ```
    python main.py performance_mode
    ```

## Application's structure
```GAP
- ├── docs
- |   ├── Flowchart.html
- |   ├── Flowchart.png
- |   ├── Plan.md
- ├── files
- |   ├── challenge.xlsx
- ├── form_filler
- |   ├── __init__.py
- |   ├── excel.py
- |   ├── selenium.py
- ├── tests
- |   ├── __init__.py
- ├── env
- ├── .qitignore
- ├── main.py
- ├── README.md
- ├── requirements
```

## Testing
- Tests can be run normally
-> For example a simple test file can be run with:
    ```
    python -m pytest tests/<test_file>.py::<test_function>
    ```

## key design or technical decisions.
1. Flowcharts and plan.md were added to simulate a normal work project
2. CLI flag
    - The code is separated into normal run and performance run
3. Headless mode
    - The headless mode is only used when running the program with the performance mode flag
