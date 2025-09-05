
valid_categories = {"ADMIN", "LECTURERS", "STUDENTS"}

class SecurityLabel:
    def __init__(self, categories):
        for category in categories:
            if category not in valid_categories:
                raise PermissionError(f"Invalid category: {category}")
        self.categories = set(categories)

    def subset_check(self, other):
        return self.categories.issubset(other.categories)


class Subject:
    def __init__(self, name, label):
        self.name = name
        self.label = SecurityLabel(label)



class Object:
    def __init__(self, name, label):
        self.name = name
        self.label = SecurityLabel(label)


def can_access(subject: Subject, obj: Object):
    if subject.label.categories == {'ADMIN'}:
        return True
    else:
      return subject.label.subset_check(obj.label)

