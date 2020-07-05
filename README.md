# Password-Generator
Generates password of given length.
The 'PasswordGeneratorTerminal.py' generates a terminal based password suggestor and the 'PasswordGeneratorGUI.py' creates a GUI (Graphical User Interface) for the same purpose. 
To make an .exe file of the GUI code, the steps are:
1. Open the terminal (or command prompt).
2. Install 'pyinstaller' by 'pip install pyinstaller' or some other way.(This is an one time work, just need to do it for the very first time).
3. After installing that, go to the directory(folder) where the 'PasswordGenerator.py' file is. Or for windows, we may directly go to the folder and 'shift + right_click' there and open 'Windows Power Shell'. 
3. There we have to write this code: 
        pyinstaller PasswordGeneratorGUI.py 
   This will create many files including the .exe file.
   If we need just one file i.e .exe then do this:
        pyinstaller --onefile PasswordGeneratorGUI.py
        
   This should generate the file. But while running this will open an termial file along with the maijn GUI window. T remove this, use this command in place of the prevvious one:
        pyinstaller --onefile --windowed PasswordGeneratorGUI.py
        
   If none of these works(This may not work for several reasons which I don't kbnow clearly), try this:
         pyinstaller --hidden-import=pkg_resources.py2_warn PasswordGeneratorGUI.py
