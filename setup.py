from setuptools import setup, find_packages

setup(name="department-app",
	  version="0.1",
	  description="Django app for human resourse management.",
	  lond_description=open("README.md").read(),
	  packages=find_packages(),
	  url="https://github.com/krisstinkou/human-resource-management.git",
	  install_requires=[
		  "Django>=3.0",
	  ]
	  )
