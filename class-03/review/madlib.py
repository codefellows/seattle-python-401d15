def read_template(path):
    with open(path) as file:
        content = file.read()
        stripped_content = content.strip()

    return stripped_content

def parse_template(string_template):

    capturing = False
    dissected_string = ""
    parts = []
    current_speech_part = ""

    # "A {Noun}."
    # "A {}.", ["Noun"]

    #  "A {Adjective} and {Adjective} {Noun}."
    #               ^
    # capturing = False
    # dissected_string = "A {} and {} {}."
    # current_speech_part = "Noun"  - should build up to Adjective, then add it to the parts list
    # push to parts - ["Adjective","Adjective","Noun"]

    for char in string_template:
        if not capturing:
            dissected_string += char

            if char == "{":
                capturing = True

        else:
            if char == "}":
                capturing = False
                parts.append(current_speech_part)
                dissected_string += char
                current_speech_part = ""
            else:
                current_speech_part += char


    return (dissected_string, parts) # Could also be list, but tuple preferred when it isn't mean to be modified, aka immutable


def merge(bare_template, responses):
    # "A {} and {} {}.", ["dark", "stormy", "night"]
    #    ^
    # merged = bare_template
    # for response in responses:
    #    merged = merged.replace("{}", response, 1)

    # return merged

    return bare_template.format(*responses)
