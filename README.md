# `cmos-tools`

A repository to store all software tools for the CMOS system used for the FOXSI mission.

This repository will hopefully contain all code that proves useful in the working/analysis of CMOS (at least from FOXSI-4). Several languages might be used and so the top level will be to contain language specific packages.

For example, the `cmos-tools-py` folder will be a Python package containing all the necessary `.py` files. If other languages are to be included, like `IDL`, then a folder called `cmos-tools-idl` should be created and used to contain all the `IDL`-ness of the repository. This standard can be applied to the inclusion of other languages (e.g., C++ as `cmos-tools-cpp`, etc.).

Every `cmos-tools-<?>` folder should have an "examples" and a "tests" folder. The "examples" folder is a great place to include scripts that show how some of the code in the repository works and the "tests" folder is a fantastic place to put code that tests the tools that have been created.

Additionally, there is also an "examples" and "tests" folder in the top level of the repository so there is a place for anything that fits these folders that spans across code from multiple languages.
