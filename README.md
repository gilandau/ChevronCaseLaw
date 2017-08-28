# Files and Code Descriptions

## Articles Directory:
	Contains three files for each Chevron case
\<Case Id\>.txt – contains the text of the judgement
<Case Id>_meta.txt – contains a list of citations that the case makes
<Case Id>_struct.txt – contains the structure of the judgement

## raw_text Directory:
	Contains raw text (<Case Id>.txt) of each judgement

## meta_text Directory:
	Contains meta text (<Case Id>_meta.txt) of each judgement

## statutes Directory:
	Contains the statute frequency count for level 2 (l2) and level 3 (l3) analysis for each case
	<Case Id>.txt-l2.txt indicates it is the level 2 statute counts
	<Case Id>.txt-l3.txt indicates it is the level 3 statute counts
	<Case Id>--1.txt-l3.txt indicates it is the level 3 statute counts of an overturned case

## sorted_analyzed_cases.csv:
	Contains the current list of cases that have been analyzed by the team, sorted and with 
their respective analysis

## sorted_final_total_list.txt:
	Contains the current list of all cases that have been analyzed by the team, sorted

## grab_google_scholar.py:
	For every case in the list of cases, extracts the case id, searches for it on Google scholar,
	and extract the text, meta text, and struct text

## sort_data_sets.py:
	Sorts the cases alphabetically and counts which cases have been analyzed 
on the l2 or l3 level

## law_analysis.py:
	Contains a number of functions that analyze the law texts:
		flatten() – flattens the Article directory into a new directory
		average_length() – gets the length of the shortest judgement as well as the average 
                                                       length of the judgements and the median length of them
		footnotes() – operates on meta text files and examines the number of footnotes,
			          references, and outside citations in a text, as well as some
			          meaningful statisitics

## find_statutes() – attempts to find all the l2 and l3 statutes referenced in the raw 
               texts of the judgements. Stores them in the relevant statute file
	   and returns some meaningful statistics.
		

## case_analysis_parser.py: 
	Parses the case analysis csv, and returns meaningful statistics on the number of 
            cases that have multiple statutes under analysis as well as the statistics for each particular
            level of analysis.

## relevant_statute_analyzer:
	Analyzes whether the most frequently referenced statute is the one under inspection. 
	Done for level 2 and level 3 analysis.

