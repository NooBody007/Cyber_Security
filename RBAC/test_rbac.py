from rbac_system import *
# Define permissions
create_course = Permission('create_course')
grade_students = Permission('grade_students')
submit_assignment = Permission('submit_assignment')
view_materials = Permission('view_materials')

# Create role hierarchy
student = Role('Student', [submit_assignment, view_materials])
teaching_assistant = Role('TeachingAssistant', parent=student)
lecturer = Role('Lecturer', [grade_students], parent=teaching_assistant)
admin = Role('Admin', [create_course], parent=lecturer)

# Create test users
student_user = User("S", [student])
ta_user = User("TA", [teaching_assistant])
lecturer_user = User("L", [lecturer])
admin_user = User("A", [admin])

# Run tests
print("1. Student viewing materials:", "Access" if has_permission(student_user, 'view_materials') else "Denied")
print("2. TA grading students:", "Access" if has_permission(ta_user, 'grade_students') else "Denied")
print("3. Lecturer grading students:", "Access" if has_permission(lecturer_user, 'grade_students') else "Denied")
print("4. Admin creating course:", "Access" if has_permission(admin_user, 'create_course') else "Denied")
print("5. Student creating course:", "Access" if has_permission(student_user, 'create_course') else "Denied")