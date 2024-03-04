import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="5ive",
    options={"build_exe": {"packages":["pygame", "pygame_widgets", "threading", "socket", "pickle", "random", "os"],
                           "include_files":[]}},
    executables = executables

    )