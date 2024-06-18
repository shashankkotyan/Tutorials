import nbformat as nbf
ntbk = nbf.read("Tutorial.ipynb", nbf.NO_CONVERT)
new_ntbk = ntbk
new_ntbk.cells = [cell for cell in ntbk.cells if cell.cell_type != "markdown"]
nbf.write(new_ntbk, "Tutorial_colab.ipynb", version=nbf.NO_CONVERT)