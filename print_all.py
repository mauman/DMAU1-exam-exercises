import os
import subprocess

#requires an installation of asciidoctor-web-pdf
exe_path = "C:\\Program Files\Asciidoctor Web PDF\\asciidoctor-web-pdf.exe"
options = '-a stylesheet="adoc-DMA.css"'

[*map(lambda f: subprocess.run(f'"{exe_path}" "{f.name}" {options}'), filter(lambda p: p.name.endswith('.adoc'), os.scandir(os.getcwd())))]
