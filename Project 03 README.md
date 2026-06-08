A content-based movie recommendation system written in Python that utilizes a weighted similarity matching algorithm to suggest films based on user-defined genres, moods, and rating preferences.

Features
Weighted Matching Engine: Calculates a normalized match score (
0.0
 to 
1.0
) by giving distinct priorities to different categories (Genre match = 2 points, Mood match = 1.5 points)[cite: 4].
Dynamic Threshold Filtering: Excludes movies that fall below a user-specified minimum IMDb rating[cite: 4].
Visual Terminal UI: Displays recommendation match percentages using an elegant text-based progress bar (████░░░░)[cite: 4].
Dual-Mode Execution: Operates as an interactive command-line interface by default, with an automated fallback demo mode if the input stream is interrupted[cite: 4].
How to Run
Prerequisites: Make sure you have Python 3 installed on your system. No external libraries are required.
Open Terminal: Navigate to the folder containing the project files.
Run the Project: Execute the script by running the following command verbatim: