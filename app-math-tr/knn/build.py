import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py knn2.ipynb -f latex")
    os.system("pdflatex knn2.tex")
    os.system("evince knn2.pdf")
    exit()
