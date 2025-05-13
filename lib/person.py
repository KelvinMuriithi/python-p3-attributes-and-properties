#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
    def __init__(self, name="Kelvin", job="Engineer"):
        self.name = name
        self.job = job
    
    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance (name, str) and (1<= len(name)<=25):
            self._name = name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    name = property(get_name, set_name)
    
    # job
    
    def get_job(self):
        print("Retrieving job.")
        return self._job

    def set_job(self, job):
        if job in Person.APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
    pass
    pass
