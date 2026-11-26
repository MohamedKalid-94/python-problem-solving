"""
=========================================================
Topic : pip Package Management in Python

Covered:

1. Understanding pip
2. Installing packages
3. Checking installed packages
4. Package information
5. Using external libraries
6. Dependency management

=========================================================
"""


import subprocess
import sys



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def python_version():

    separator("1. Python Version Information")


    print(
        "Python Version:"
    )


    print(
        sys.version
    )



def check_installed_packages():

    separator("2. Check Installed Packages")


    print(
        "Installed Packages:"
    )


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



def install_package_command():

    separator("3. Install Package Command")


    print(
        "Install package example:"
    )


    print(
        "pip install requests"
    )


    print(
        "pip install pandas"
    )


    print(
        "pip install numpy"
    )



def uninstall_package_command():

    separator("4. Uninstall Package Command")


    print(
        "Remove package:"
    )


    print(
        "pip uninstall package_name"
    )



def package_information():

    separator("5. Package Information")


    print(
        "Show package details:"
    )


    print(
        "pip show package_name"
    )


    print(
        "Example:"
    )


    print(
        "pip show requests"
    )



def upgrade_package():

    separator("6. Upgrade Package")


    print(
        "Upgrade package:"
    )


    print(
        "pip install --upgrade package_name"
    )



def freeze_requirements():

    separator("7. Generate requirements.txt")


    print(
        "Command:"
    )


    print(
        "pip freeze > requirements.txt"
    )


def real_world_usage():

    separator("8. Real World Package Usage")


    examples = [

        "requests - API communication",

        "pandas - Data processing",

        "numpy - Numerical computing",

        "fastapi - Backend APIs",

        "langchain - AI applications",

        "pytest - Testing"

    ]


    for item in examples:

        print(
            "-",
            item
        )



def dependency_management_flow():

    separator("9. Dependency Management Flow")


    print(
        """
Create Project
      |
      ↓
Create Virtual Environment
      |
      ↓
Install Packages using pip
      |
      ↓
Freeze Dependencies
      |
      ↓
requirements.txt
      |
      ↓
Install on Another Machine
        """
    )



def main():

    python_version()

    check_installed_packages()

    install_package_command()

    uninstall_package_command()

    package_information()

    upgrade_package()

    freeze_requirements()

    real_world_usage()

    dependency_management_flow()



if __name__ == "__main__":

    main()