README_Q3.md
RBAC System with Role Hierarchies

This RBAC system implements role-based access control with hierarchical roles (Admin > Lecturer > TA > Student). The implementation uses three core classes: Permission (actions), Role (groups permissions with parent-child relationships), and User (assigned roles). The has_permission() function checks access by recursively traversing the role hierarchy - if a permission isn't found in the user's immediate role, it checks parent roles until reaching the top level.

Run `python test_rbac.py` to see the prepared test results

To test:
1. Describe permissions with, Permission("name")
2. Create roles with, Role("role_name", [list_of_permissions])
3. To assign a parent role, Role("child_name", [permissions], parent_role)
4. To create a user, User("username")
5. To assign a role to a user, user.assign_role(role)
6. To check access of a user, has_permission(user, "permission_name")