import cx_Freeze

executables = [cx_Freeze.Executable("sam.py")]

cx_Freeze.setup(
    name="Snake",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["alien.png","b1.wav","background.jpg","background1.jpg","bullet.png","enemy1.png",
                                            "enemy2.png","enemy3.png","enemybullet.png","explosion.wav","shoot.wav","spaceship.png",
                                            "welcome.png"]}},
    executables = executables

    )

