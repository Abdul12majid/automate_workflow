import re


def insert(value, context):

    if not isinstance(value, str):
        return value

    pattern = r"{{(.*?)}}"

    matches = re.findall(pattern, value)

    for match in matches:

        key = match.strip()

        replacement = str(
            context.get(key, "")
        )

        value = value.replace(
            "{{" + match + "}}",
            replacement
        )

    return value