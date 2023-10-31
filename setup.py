import setuptools

with open("README.md", "r", encoding="utf-8") as file_obj:
    long_description = file_obj.read()


__version__ = "0.0.0"

REPO_NAME = "End_To_End_Project_With_MLflow"
AUTHOR_USER_NAME = "Olusegun"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "ajoseolusegun@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)