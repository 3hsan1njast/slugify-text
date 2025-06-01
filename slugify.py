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

# Testcases:
input_1 = "  Hello, World! This is PYTHON!@.  "
input_2 = " Hello #World FROM  @IRan!"
print(f'Text: "{input_1}" ==> Slug: "{slugify(input_1)}"')
print(f'Text: "{input_2}" ==> Slug: "{slugify(input_2)}"')
