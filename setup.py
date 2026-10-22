"""Packaging config for Panda3D's build_apps. Run `build_exe.bat` rather than this file.

Output: build/win_amd64/fantasygame.exe, with assets/ next to it. Copy the whole folder.
"""

from setuptools import setup

setup(
    name="fantasygame",
    options={
        "build_apps": {
            "gui_apps": {"fantasygame": "src/fantasygame/__main__.py"},
            "include_patterns": ["assets/**/*"],
            "plugins": ["pandagl"],
            "platforms": ["win_amd64"],
            # Written by build_exe.bat from uv.lock, so the build uses the same versions.
            "requirements_path": "build/requirements.txt",
            # A windowed app has no console, so messages and crashes go to this file
            # (%LOCALAPPDATA%\fantasygame\output.log on Windows).
            "log_filename": "$USER_APPDATA/fantasygame/output.log",
            "log_append": False,
        }
    },
)
