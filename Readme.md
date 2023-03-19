## CS_136_Auto_Grader
---
Gradescope autograder application which automatically evaluates the CS 136 submission in gradescope. 


## Steps to get started:
---
1. Clone the project.
        
        git clone [project_url]

2. Navigate to required branch
      
      | Branch name | Description    |
      | :---:   | :---: | 
      | version_1.0.0 | basic and stable   |
      | version_1.1.0 | latest   |


        git checkout version_1.1.0

3. Navigate to src directory

        cd src

4. Install all the python dependencies

        pip install requirements.txt

5. Update the [config.json](src/config.json)
 based on the task requirements.

6. Modify [utility.py](src/utility.py) and [unit-tests-files](src/tests/) according to your task requirements. 


## Project Structure
---

   - __builds__
     #### Autograder zip files to deploy directly to gradescope
     - [Autograder\_version\_1.0.0.zip](builds/Autograder_version_1.0.0.zip)

            Basic and stable version of autograder.

     - [Autograder\_version\_1.1.0.zip](builds/Autograder_version_1.1.0.zip)
            
            generic version which is not stable yet. 

   - __src__ 
      #### Source Code

     - [config.json](src/config.json)

            configuration file for the autograder

     - [convert\_to\_ascii.py](src/convert_to_ascii.py)

            normal 

     - [requirements.txt](src/requirements.txt)

            file which holds all the python package requirements

     - [run\_autograder](src/run_autograder)

            autograder shell script

     - [run\_tests.py](src/run_tests.py)

            python unit-tests entry file

     - [setup.sh](src/setup.sh)

            environment setup file for autograder

     - __tests__
       - [test\_code\_format.py](src/tests/test_code_format.py)

              unit-test for the code-formatting checking like comments in the submission.

       - [test\_files.py](src/tests/test_files.py)

              unit-test to check the required files in the submission.

       - [test\_return.py](src/tests/test_return.py)

              unit-test to check the normal and edge cases of the submission.  

       - [test\_syntax.py](src/tests/test_syntax.py)

              unit-test for syntax check to the submission. 
     - [utility.py](src/utility.py)

            utilities which reads the config.json and serves as central point for unit-test files.

     - [zip\-convertor.py](src/zip-convertor.py)

            python file to generate the builds


## Contributors:
---
- [Gali Bhaskar](https://github.com/galibhaskar)
