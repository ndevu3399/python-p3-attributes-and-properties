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
    def __init__(self, name=None, job=None):
        self._name = None
        self._job = None

        # Validate and set name
        if name is not None:
            if isinstance(name, str) and 1 <= len(name) <= 25:
                self._name = name.title()
            else:
                print("Name must be string between 1 and 25 characters.")
                return  # Stop execution if name is invalid
        
        # Only set job if name is valid
        if job is not None and self._name is not None:
            if job not in APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
            else:
                self._job = job
