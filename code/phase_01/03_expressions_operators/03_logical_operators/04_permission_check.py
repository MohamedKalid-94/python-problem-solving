"""
Topic: Logical Operators

Concept:
Use 'or' and 'not' operators.

Real-world Example:
System permission checking.
"""


is_admin = False

is_manager = True


has_permission = is_admin or is_manager


print("Permission Check")
print("----------------")

print("Admin:", is_admin)

print("Manager:", is_manager)

print("Access Granted:", has_permission)


print()

print("Not Admin:", not is_admin)