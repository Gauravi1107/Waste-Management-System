Waste-Management-System
OVERVIEW
The Smart Waste Sorting System operates through a Python command-line interface which performs automatic waste classification for Plastic Paper Metal Glass and Compost categories. The program uses keyword detection to analyse item descriptions which helps it determine the proper sorting bin for each item. If the item cannot be identified, it marks it as Unknown and rejects it.

The project provides a basic understanding of AI logic and string processing and decision-making techniques through Python programming.

FEATURES
Automatic item classification based on description keywords

Five waste categories + Unknown category

Smart bin assignment with bin numbers

Clear console messages for each item

Allows the user to enter multiple items at once

Simple to test and modify

TECHNOLOGIES USED
Python 3.13

Built-in functions (input, print, conditionals, loops)

No external libraries required

Installation & Running the Project

PREREQUISITES
Install Python 3.13

Clone the Repository git clone

Navigate to the Project Folder

Run the Program

waste-generator.py

TESTING INSTRUCTIONS
Run the script.

Enter the number of items you want to test.

Provide a description for each item, for example:

"red crinkly bottle" → Plastic

"newspaper" → Paper

"shiny can" → Metal

"transparent jar" → Glass

"banana peel" → Compost

"stone" → Unknown

Observe the classification messages printed by the system.

HOW IT WORKS
The program does the following:

Stores bin numbers for each waste category

Asks the user for multiple items

For each item:

. Converts to lowercase

. Checks keywords

. Finds the matching waste category

. Looks up bin number

. Prints whether item is accepted and where to send it

Repeats for all items

CUSTOMIZATION IDEAS
After all items are classified, display a final summary showing how many items were sorted into each category.
This makes the output clearer and helps users understand the overall distribution of waste.

What it adds:

Gives a clean final report

Helps users track sorting efficiency.

Makes the project look more complete and professional.

OUTPUT:
Screenshot 2025-11-25 010026
LICENSE
Free to use and modify for personal and educational purposes