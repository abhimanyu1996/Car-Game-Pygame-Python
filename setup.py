import cx_Freeze

executables = {cx_Freeze.Executable("RealGame - Distance.py")}

cx_Freeze.setup(
    name = "Car Game",
    options ={"build_exe":{"packages":["pygame"],"include_files":["sunshine.ttf","hitcar1.png","hitcar2.png","hitcar3.png","maincar.png","Tree.png","Mainmenu.jpg","sub.jpg"]}},
    description = "Car Game",
    executables = executables
    )
