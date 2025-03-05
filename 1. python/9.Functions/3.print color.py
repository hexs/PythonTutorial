from hexss.constants.terminal_color import *

if __name__ == "__main__":
    # Basic Text Styles
    print(f"{BOLD}This is bold text!{END}")
    print(f"{ITALIC}This is italic text!{END}")
    print(f"{UNDERLINED}This is underlined text!{END}")
    print(f"{REVERSE}This text has reversed colors!{END}")

    # Text Colors
    print(f"{RED}This is red text!{END}")
    print(f"{GREEN}This is green text!{END}")
    print(f"{BLUE}This is blue text!{END}")
    print(f"{YELLOW}This is yellow text!{END}")

    # Background Colors
    print(f"{BG_RED}This is text with a red background!{END}")
    print(f"{BG_GREEN}This is text with a green background!{END}")
    print(f"{BG_BLUE}This is text with a blue background!{END}")
    print(f"{BG_YELLOW}This is text with a yellow background!{END}")

    # Combining Text Color and Background Color
    print(f"{RED.BG_YELLOW}Red text on a yellow background!{END}")
    print(f"{WHITE.BG_BLUE}White text on a blue background!{END}")

    # Combining Multiple Styles
    print(f"{BOLD.UNDERLINED.GREEN}Bold, underlined and green text!{END}")