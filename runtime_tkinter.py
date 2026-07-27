"""Configura las bibliotecas Tcl/Tk incluidas por PyInstaller."""
import os
import sys

base = getattr(sys, "_MEIPASS", "")
if base:
    os.environ["TCL_LIBRARY"] = os.path.join(base, "_tcl_data")
    os.environ["TK_LIBRARY"] = os.path.join(base, "_tk_data")
