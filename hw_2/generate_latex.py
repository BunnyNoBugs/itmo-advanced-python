def generate_table(data):
    num_columns = len(data[0])
    column_format = '|'.join(['c'] * num_columns)

    latex_table = f"\\begin{{tabular}}{{|{column_format}|}}\n\\hline\n"

    for row in data:
        latex_table += " & ".join(row) + " \\\\\n\\hline\n"

    latex_table += "\\end{tabular}"

    return latex_table
