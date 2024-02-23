from re import Pattern

# Enums
from enums.color import Color


def rgb_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


def reset_color():
    return "\033[0m"


def colorize_match(pattern: Pattern, text: str, color: Color):
    if color == Color.RED:
        return pattern.sub(f"{rgb_color(255, 0, 0)}\\g<0>{reset_color()}", text)

    if color == Color.GREEN:
        return pattern.sub(f"{rgb_color(0, 255, 0)}\\g<0>{reset_color()}", text)

    if color == Color.BLUE:
        return pattern.sub(f"{rgb_color(0, 0, 255)}\\g<0>{reset_color()}", text)

    return text
