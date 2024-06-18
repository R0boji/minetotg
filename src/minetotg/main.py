PREFIX = "§"
COLORS = "0123456789abcdef"

TEXT_FORMATTING: dict[str, list[str]] = {f"{PREFIX}k": ["<tg-spoiler>", "</tg-spoiler>"],
                                         f"{PREFIX}l": ["<b>", "</b>"],
                                         f"{PREFIX}m": ["<s>", "</s>"],
                                         f"{PREFIX}n": ["<u>", "</u>"],
                                         f"{PREFIX}o": ["<i>", "</i>"]
                                         }


def reformation_cycle(used_formatting: list[str], mine_string: str, formatter: str | None = None) -> str:
    selector = ""
    for symbol_index in range(1, len(mine_string)):
        if f"{mine_string[symbol_index - 1]}{mine_string[symbol_index]}" in used_formatting:

            if formatter:
                if len(mine_string) - 1 >= symbol_index + 1:
                    return (TEXT_FORMATTING[formatter][0] +
                            selector[:-1] +
                            reformation_cycle(used_formatting,
                                              mine_string[symbol_index + 1:],
                                              f"{mine_string[symbol_index - 1]}{mine_string[symbol_index]}") +
                            TEXT_FORMATTING[formatter][1])
                else:
                    return TEXT_FORMATTING[formatter][0] + selector[:-1] + TEXT_FORMATTING[formatter][1]
            else:
                if len(mine_string) - 1 >= symbol_index + 1:
                    return (
                            selector[:-1] +
                            reformation_cycle(used_formatting,
                                              mine_string[symbol_index + 1:],
                                              f"{mine_string[symbol_index - 1]}{mine_string[symbol_index]}"))
                else:
                    return selector[:-1]
        if symbol_index == 1:
            selector += f"{mine_string[symbol_index - 1]}{mine_string[symbol_index]}"
        else:
            selector += mine_string[symbol_index]
    if formatter:
        return TEXT_FORMATTING[formatter][0] + (selector if len(mine_string) >= 2 else mine_string) + \
            TEXT_FORMATTING[formatter][1]
    else:
        return selector if len(mine_string) >= 2 else mine_string


def reformat(mine_string: str) -> str:
    """Reformat string with Minecraft text formatting to Telegram HTML.
    :param mine_string: String with Minecraft text formatting.
    :return: String with Telegram-oriented HTML formatting."""

    # Screening < and >
    mine_string = mine_string.replace("<", "&lt;").replace(">", "&gt;")

    # Deleting all colors because it is unsupported in Telegram messages
    for color_number in COLORS:
        color = f"{PREFIX}{color_number}"
        mine_string = mine_string.replace(color, "")

    # Creating a list of all used formatting symbols
    used_formatting: list[str] = []
    for formation_symbol in TEXT_FORMATTING.keys():
        if mine_string.find(formation_symbol) > -1:
            used_formatting.append(formation_symbol)

    # Main formation algorithm
    mine_string_list = mine_string.split("§r")
    tg_string_list = []
    for el in mine_string_list:
        tg_string_list.append(reformation_cycle(used_formatting, el))

    return "".join(tg_string_list)
