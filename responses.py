"""This module provides responses to user made input text"""


def sample_responses(input_text):
    """To make testing a bit more fun"""
    msg = str(input_text).lower()

    if msg == "hello":
        return "Hey, how is it going"
    return "Sorry, i did not understand that"
