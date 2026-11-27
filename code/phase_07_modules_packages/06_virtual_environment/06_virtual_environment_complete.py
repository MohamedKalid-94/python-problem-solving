"""
=========================================================
Topic : Virtual Environment (venv) in Python

Covered:

1. Understanding virtual environment
2. Creating isolated environments
3. Checking environment information
4. Package isolation concept
5. Project dependency management
6. Real-world workflow

=========================================================
"""


import sys
import os
import subprocess



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def python_environment_info():

    separator("1. Python Environment Information")


    print(
        "Python Version:"
    )


    print(
        sys.version
    )


    print(
        "\nPython Executable:"
    )


    print(
        sys.executable
    )



def check_virtual_environment():

    separator("2. Check Virtual Environment")


    virtual_env = os.environ.get(
        "VIRTUAL_ENV"
    )


    if virtual_env:

        print(
            "Virtual Environment Active:"
        )

        print(
            virtual_env
        )


    else:

        print(
            "Running in Global Python Environment"
        )



def installed_packages():

    separator("3. Installed Packages")


    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "list"
        ],
        capture_output=True,
        text=True
    )


    print(
        result.stdout
    )



def virtual_environment_commands():

    separator("4. Virtual Environment Commands")


    print(
        """
Create Virtual Environment:

python -m venv venv


Activate Windows:

venv\\Scripts\\activate


Activate Linux/Mac:

source venv/bin/activate


Deactivate:

deactivate
        """
    )



def why_virtual_environment():

    separator("5. Why Use Virtual Environment?")


    reasons = [

        "Project dependency isolation",

        "Avoid package version conflicts",

        "Separate development environments",

        "Easy deployment",

        "Better project management"

    ]


    for item in reasons:

        print(
            "-",
            item
        )



def real_world_project_example():

    separator("6. Real World Project Example")


    print(
        """
AI Project:

rag_project/

├── venv/
├── app.py
├── requirements.txt
├── embeddings/
├── vector_database/
└── models/


Environment:

venv
 |
 +-- langchain
 +-- chromadb
 +-- fastapi
 +-- openai
        """
    )



def dependency_workflow():

    separator("7. Professional Workflow")


    print(
        """
1. Create project folder

2. Create virtual environment

3. Activate venv

4. Install required packages

5. Develop application

6. Freeze dependencies

7. Share requirements.txt

8. Deploy project
        """
    )



def main():

    python_environment_info()

    check_virtual_environment()

    installed_packages()

    virtual_environment_commands()

    why_virtual_environment()

    real_world_project_example()

    dependency_workflow()



if __name__ == "__main__":

    main()