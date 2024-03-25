from generate_latex import generate_table

data = [
    ["Header1", "Header2", "Header3"],
    ["sample", "text", "1"],
    ["sample", "asdf", "2"],
]

latex_table_code = generate_table(data)

latex_document = f"""
\\documentclass{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{array}}
\\usepackage{{longtable}}
\\usepackage{{multirow}}
\\usepackage{{multicol}}
\\usepackage{{graphicx}}
\\usepackage{{float}}

\\begin{{document}}


{latex_table_code}


\\end{{document}}
"""

with open("artifacts/document.tex", "w", encoding='utf-8') as f:
    f.write(latex_document)
