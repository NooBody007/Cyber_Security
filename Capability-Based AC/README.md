README_Q2.md
Capability-Based Access Control System

This system implements capability-based access control with support for multiple owners per object. Only owners can modify capabilities for others.

Run `python test_capabilities.py` to see the prepared test results

To test:
1. Describe subjects and objects with, Subject("name"), Object("name")
2. To give capability, --> subject.capabilities.append(Capability(object,list_of_capabilities))
3. To give ownership over a file, --> object.owners.append(subject)
4. To add capability, add_capability(subject1, subject2, object, list_of_capabilities)
5. To give ownership to multiple subjects over a file, --> object.owners.extend([subject1, subject2])
6. To check access of a subject, --> check_access(subject,object,capability)
7. To remove capability, --> remove_capability(subject1, subject2, object, capability)