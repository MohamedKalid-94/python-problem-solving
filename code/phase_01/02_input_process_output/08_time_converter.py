"""
Problem:
Convert hours into minutes and seconds.

Pattern:
Unit Conversion
"""


def convert_time(hours):
    minutes = hours * 60
    seconds = hours * 3600

    return {
        "minutes": minutes,
        "seconds": seconds
    }


if __name__ == "__main__":
    print(convert_time(2))