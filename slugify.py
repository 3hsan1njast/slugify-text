def slugify(_input: str):
    _input = _input.strip()
    punctuations = r""".,?!:;-–—'"()[]{}…/\\*#@^_`|"""
    removed_space_str = ""

    for charIndex in range(len(_input)):
        if _input[charIndex] not in punctuations:
            if _input[charIndex] == ' ' and charIndex != 0:
                if removed_space_str[len(removed_space_str) - 1] != '-':
                    removed_space_str += '-'
                continue
            removed_space_str += _input[charIndex].lower()

    return removed_space_str
