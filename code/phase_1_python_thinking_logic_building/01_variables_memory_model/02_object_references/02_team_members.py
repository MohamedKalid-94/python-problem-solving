"""
Topic: Object References

Concept:
Both variables point to the same list.
"""

team_members = ["Alice", "Bob"]

development_team = team_members

development_team.append("Charlie")

print("Team Members")
print(team_members)

print()

print("Development Team")
print(development_team)