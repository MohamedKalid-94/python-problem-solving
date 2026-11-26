"""
Topic: while Loop

Problem:
Allow only three guessing attempts.
"""

attempt = 1

while attempt <= 3:
    print("Guess Attempt:", attempt)
    attempt = attempt + 1

print("No attempts remaining.")