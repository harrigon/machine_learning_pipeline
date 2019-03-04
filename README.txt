Preprocessor Code.
Harrigan Davenport
Note: Python2.7 is used for this project, as it had the widest library support

This code base is used as a preprocessor for replicating the study performed in the paper "Automatic extraction of Design
Decisions from Issue Management Systems: A Machine Learning Based Approach"

Link to the paper: https://wwwmatthes.in.tum.de/pages/yz9xr3h201j0/Automatic-extraction-of-design-decisions-from-issue-management-systems-a-machine-learning-based-approach
Link to the data: https://server.sociocortex.com/typeDefinitions/1vk4hqzziw3jp/Task

Section 5 of the paper explains the point of the preprocessor, as well as an easy to understand illustration on page 10.
-----------------------------------------------------
-No parameters are required for the code
-Tasks.xls must be in the same directory(Download link above)

This preprocessor code is described as "the first part - process documents", where the labeled dataset is the input which
generates the term frequency of the issues. This output is then to be passed to "the second part - Model Generation" to
produce the classification model. For each issue, every word is tokenized and transformed to lowercase. Stop words such as
articles, conjunctions and prepositions are removed. The remaining words are then stemmed using the Porter stemming algorithm.
The python library nltk was used to remove stopwords and stem the words. Since the python3.5 version of nltk is not considered
stable, python 2.7 was used for the project.

After the words have been stemmed, the term frequency-inverse document frequency was calculated. Note that the implementation
of the tf-idf is not overly efficient. It is not noticeable with ~1500 inputs, but if the project is expanded in the future
this may be a point of concern.

The project outputs:
    outputfile.csv : csv containing taskId, summary+description string, design decision, decision category
    outputFrequency.csv: csv containing taskId followed by tf-idf for each word in the summary+description string
