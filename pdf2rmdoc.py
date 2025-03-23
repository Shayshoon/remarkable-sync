import os
import sys
import subprocess
from PyPDF2 import PdfWriter, PdfReader

def splitPDF(file_name, output_dir):
    inputpdf = PdfReader(file_name, strict=False)

    num_pages = inputpdf._get_num_pages()
    name = os.path.basename(file_name)[:-4]
    dir = output_dir or os.getcwd()
    files = []

    #loop through all pages
    for page_number in range(num_pages):
        output = PdfWriter()
        output.add_page(inputpdf._get_page(page_number))
        
        out_file = f"{name}_{page_number + 1}.pdf"
        # out = os.path.join(dir, out_file)

        files.append(out_file)
        output.write(out_file)

    return files

def pdf2rmdoc(file):
    new_file = file[:-4] + '.rmdoc'
    os.system(f"echo image {file} 1  0 0  0.7 | drawj2d -Trmdoc -o {new_file}")
    return new_file

def merge_rmdocs(files, dest):
    subprocess.run(f"perl ./rmcat -o {dest}.rmdoc {' '.join(files)}", shell=True)


def main():
    in_file = sys.argv[1]
    out_dir = ""

    files = splitPDF(in_file, out_dir)
    res_files = []
    
    for file in files:
        res_files.append(pdf2rmdoc(file))

    merge_rmdocs(res_files, in_file[:-4])
    
    for file in files:
        os.remove(file)
    for file in res_files:
        os.remove(file)

if __name__ == "__main__":
    main()
