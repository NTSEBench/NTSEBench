Steps to run:

1. Create folder for a particular paper([example](https://www.resonance.ac.in/answer-key-solutions/NTSE/2016/Stage-1/Solutions/NTSE-Stage-1-2016-17-Gujarat-MAT-06-11-2016-Solution.pdf)) in the inputFiles folder and put into it the docx file in required format
2. In the docx file run the macro to convert numbered lists to plaintext and also convert all equations to linear latex format
3. Now run latexFix.py after putting in the correct foldername in latexFix.py          (python ./latexFix.py)
4. Now run separate.py after making necessary changes in the beginning of the code     (python ./separate.py [paperName]_fixed.pdf 1 100)
5. Finally run categories.py to complete the categoriztion of questons having no direction after changing the folder name in separate.py (python ./separate.py)