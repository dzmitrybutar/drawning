# Drawning tool
    In accordance with the task, all the required functionality of the application was implemented. In the implementation of the application, classes and modules were used for the future expansion of the program’s functionality.
To use the application, you must run the script app.py with two required arguments, such as the name of the input and output files and if needed you can add directions to the name. The input file must contain instructions for the drawing application. If the output file does not exist in the folder, it will be created, if the output file with the same name already exists the application will add the result to the end of the file.

Launch Example:
```$xslt
python app.py input.txt output.txt
python app.py examples/in.txt examples/out.txt
```

    To verify the correctness of the result based on the instructions of the task, run the test.py with two arguments.
In the examples folder are the results of different input and output files with various instructions.