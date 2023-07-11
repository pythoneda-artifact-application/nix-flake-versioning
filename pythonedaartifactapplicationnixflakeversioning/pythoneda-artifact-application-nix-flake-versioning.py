#!/usr/bin/env python3
"""
pythonedaartifactapplicationnixflakeversioning/pythoneda-artifact-application-nix-flake-versioning.py

This file defines NixFlakeVersioning.

Copyright (C) 2023-today rydnr's pythoneda-artifact-application/nix-flake-versioning

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythonedaapplication.pythoneda import PythonEDA

class NixFlakeVersioning(PythonEDA):
    """
    PythonEDA application that runs Nix Flake Versioning artifact space.

    Class name: NixFlakeVersioning

    Responsibilities:
        - Runs Nix Flake Versioning artifact space.

    Collaborators:
        - asyncio: To manage asynchronous threads.
    """
    def __init__(self):
        """
        Creates a new NixFlakeVersioning instance.
        """
        super().__init__(__file__)

if __name__ == "__main__":

    asyncio.run(NixFlakeVersioning.main())
