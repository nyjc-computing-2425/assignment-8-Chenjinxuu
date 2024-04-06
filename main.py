# Built-in imports
def reverse(text):
    """
    Parameters
    ----------
    str 
        the text you want to reverse
    Returns
    -------
    str
        a reversed text that was inputted
    Example output:
    input: "Tom"
    output: "mot"
    """
    a = len(text) - 1
    if a == -1:
        return ""
    else:
        return f"{text[a]}{reverse(text[:a])}"
#print(reverse("amatiaS > ukoG"))
def is_palindrome(text):
    """
    Parameters
    ----------
    str
        a text for checking whether it is a palinedrome.
    Returns
    -------
    Boolean
        Returns either True or False depending on whether the text is a palindrome
    """
    text = text.strip(" ,.")
    a = len(text) - 1
    if a == -1:
        return True
    elif text[0] == text[a]:
        text = text.replace(text[0], "")
        return is_palindrome(text)
    else:
        return False
