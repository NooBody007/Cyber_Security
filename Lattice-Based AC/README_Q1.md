README_Q1.md

Lattice-Based Access Control System

This system implements a lattice-based access control where access is granted only if the subject's security label is a subset of the object's security label.
Only 'ADMIN' can reach every object no matter what the security label is.

Run `python test_cases.py` to see the prepared test results
For testing:
1. Describe subject with Subject("name", {"CATEGORY"})
2. Describe object with Object("name", {"CATEGORY"})
3. Use can_access(subject, object) to find if subject has access to object and print it.
