from lattice_mac import *

print("Lattice-Based Access Control Tests")


sbj1 = Subject("Student1", {"STUDENTS"})
obj1 = Object("LectureNotes", {"STUDENTS"})
result = can_access(sbj1, obj1)
print("1. Access:" , result ,"  | {STUDENTS} --> {STUDENTS}")  # True


sbj2 = Subject("Student2", {"STUDENTS"})
obj2 = Object("SharedDocs", {"STUDENTS", "LECTURERS"})
result = can_access(sbj2, obj2)
print("2. Access:" , result , "  | {STUDENTS} --> {STUDENTS, LECTURERS}")  # True


sbj3 = Subject("Student3", {"STUDENTS"})
obj3 = Object("FacultyMeeting", {"LECTURERS"})
result = can_access(sbj3, obj3)
print("3. Access:", result, " | {STUDENTS} --> {LECTURERS}")  # False


sbj4 = Subject("Guest", set())
obj4 = Object("PublicInfo", {"STUDENTS"})
result = can_access(sbj4, obj4)
print("4. Access:", result, "  | {} --> {STUDENTS}")  # True


sbj5 = Subject("Student4", {"STUDENTS"})
obj5 = Object("EmptyResource", set())
result = can_access(sbj5, obj5)
print("5. Access:", result, " | {STUDENTS} --> {}" )  # False


sbj6 = Subject("Student5", {"STUDENTS"})
obj6 = Object("EmptyResource", {"ADMIN"})
result = can_access(sbj6, obj6)
print("6. Access:", result, " | {STUDENTS} --> {ADMIN}")  # False


sbj7 = Subject("Admin", {"ADMIN"})
obj7 = Object("LecturerDocs", {"LECTURERS"})
result = can_access(sbj7, obj7)
print("7. Access:", result, " | {ADMIN} --> {LECTURERS}")  # True