def generate_output(parsed_data):
    colors = parsed_data["colors"]
    loop_count = parsed_data["loop_count"]

    if not colors:
        return "No colors detected."

    output = ' '.join(colors * loop_count)
    return output
