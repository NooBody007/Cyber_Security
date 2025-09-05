class Permission:
    def __init__(self, name):
        self.name = name


class Role:
    def __init__(self, name, permissions=None, parent=None):
        self.name = name
        self.permissions = set(permissions) if permissions else set()
        self.parent = parent

    def has_permission(self, permission_name):
        # Check current role's permissions
        if any(perm.name == permission_name for perm in self.permissions):
            return True

        # Check parent role's permissions recursively
        if self.parent:
            return self.parent.has_permission(permission_name)

        return False

class User:
    def __init__(self, username, roles=None):
        self.username = username
        self.roles = set(roles) if roles else set()

    def assign_role(self, role):
        self.roles.add(role)

def has_permission(user, permission_name):
    return any(role.has_permission(permission_name) for role in user.roles)