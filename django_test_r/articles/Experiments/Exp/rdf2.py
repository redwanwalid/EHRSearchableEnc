"""
This file is used to make the patient instance in the owl file to 11208 as per the existing SQLite3 file.

"""

from owlready2 import *

onto = get_ontology("/Users/redwanwalid/Desktop/redwan/django_test_r/EHROntology.owl").load()

