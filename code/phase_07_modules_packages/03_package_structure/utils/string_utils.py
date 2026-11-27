"""
String Utility Module
"""


def clean_text(text):

    return text.strip()



def word_count(text):

    return len(
        text.split()
    )