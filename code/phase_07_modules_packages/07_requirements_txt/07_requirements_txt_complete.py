"""
=========================================================
Topic : requirements.txt in Python

Covered:

1. Understanding requirements.txt
2. Creating dependency list
3. Installing dependencies
4. Package version management
5. Project sharing workflow
6. Real-world project example

=========================================================
"""


import subprocess
import sys
from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def check_current_packages():

    separator("1. Check Installed Packages")


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



def requirements_file_concept():

    separator("2. requirements.txt Concept")


    print(
        """
requirements.txt stores project dependencies.

Example:

requirements.txt

fastapi==0.115.0
requests==2.32.3
pandas==2.2.3
numpy==2.1.0


Purpose:

- Share project dependencies
- Recreate environment
- Support deployment
        """
    )



def create_requirements_command():

    separator("3. Create requirements.txt")


    print(
        """
Command:

pip freeze > requirements.txt


Process:

Installed Packages
        |
        ↓
pip freeze
        |
        ↓
requirements.txt
        """
    )



def install_from_requirements():

    separator("4. Install Dependencies")


    print(
        """
Command:

pip install -r requirements.txt


Flow:

requirements.txt
        |
        ↓
pip reads packages
        |
        ↓
Packages installed
        """
    )



def version_management():

    separator("5. Package Version Management")


    examples = [

        "requests==2.32.3",

        "fastapi>=0.100.0",

        "numpy~=2.1.0"

    ]


    print(
        "Version Examples:"
    )


    for item in examples:

        print(
            "-",
            item
        )



def create_sample_requirements():

    separator("6. Create Sample requirements.txt")


    file_path = Path(
        "sample_requirements.txt"
    )


    packages = """
requests==2.32.3
pandas==2.2.3
numpy==2.1.0
fastapi==0.115.0
"""


    file_path.write_text(
        packages.strip()
    )


    print(
        "requirements file created:",
        file_path
    )



def project_sharing_workflow():

    separator("7. Project Sharing Workflow")


    print(
        """
Developer Machine

Project
   |
   ↓
Create venv
   |
   ↓
Install packages
   |
   ↓
pip freeze
   |
   ↓
requirements.txt
   |
   ↓
GitHub


Another Developer

Clone Project
   |
   ↓
Create venv
   |
   ↓
pip install -r requirements.txt
   |
   ↓
Run Project
        """
    )



def ai_project_example():

    separator("8. AI/GenAI Project Example")


    print(
        """
RAG Application

requirements.txt

langchain
langgraph
chromadb
fastapi
streamlit
pypdf
python-dotenv


Purpose:

- Document loading
- Embeddings
- Vector database
- API service
- UI application
        """
    )



def deployment_example():

    separator("9. Deployment Usage")


    print(
        """
Production Server:

1. Clone repository

2. Create virtual environment

3. Install dependencies

pip install -r requirements.txt

4. Start application
        """
    )



def main():

    check_current_packages()

    requirements_file_concept()

    create_requirements_command()

    install_from_requirements()

    version_management()

    create_sample_requirements()

    project_sharing_workflow()

    ai_project_example()

    deployment_example()



if __name__ == "__main__":

    main()