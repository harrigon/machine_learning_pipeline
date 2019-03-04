from __future__ import unicode_literals
from __future__ import division
import csv
import xlrd
from transformations import *

def termFreqInvDocFreq(workingList):
    returnList = []
    numberOfDocs = len(workingList)
    frequencyDict = dict()
    for row in workingList:
        for word in row[1].split(' '):
            if (word in frequencyDict) is False:
                frequencyDict[word] = 1
            else:
                frequencyDict[word] += 1


    for row in workingList:
        # rowWithFreq = [] #use if returning as list
        rowWithFreqString = ''
        tF = termFrequency(row[1])
        iDF = inverseDocumentFrequency(row[1], numberOfDocs, frequencyDict)
        for i in range(len(tF)):
            assert(tF[i][0] == iDF[i][0]) #checking to make sure nothing dumb has happend
            #rowWithFreq.append([tF[i][0], tF[i][1] * iDF[i][1]]) #Use if returning as list
            rowWithFreqString += str(tF[i][1] * iDF[i][1]) + ", "
        returnList.append(row[0] + ', ' + rowWithFreqString)

    return returnList


def termFrequency(row):
    """Measures how frequently a term occurs in a document, relative to document size"""
    row_list = row.split(' ')
    totalLength = len(row_list)
    returnValues = []
    for word in row_list:
        if word == '':
            pass ##final check because of weird things
        else:
            returnValues.append((word, row_list.count(word)/totalLength))
    return returnValues

def inverseDocumentFrequency(row, numberOfDocs, frequencyDict):
    """How important a term is to a document"""
    row_list = row.split(' ')
    returnValues = []
    for word in row_list:
        if word == '':
            pass ##final check because of weird things
        else:
            returnValues.append((word, numberOfDocs/frequencyDict[word]))
    return returnValues





def main():
    nvalue = 5
    writer = csv.writer(open("outputFile.csv", 'wb'))
    workbook = xlrd.open_workbook('Tasks.xls', on_demand=True)
    sheet = workbook.sheet_by_index(0)
    row_dict = {}
    for row_number in range(sheet.nrows):
        row_dict[row_number] = (sheet.cell(row_number, 2).value.encode('ascii', 'ignore'),
                                sheet.cell(row_number, 3).value.encode('ascii', 'ignore'),
                                sheet.cell(row_number, 4).value.encode('ascii', 'ignore'),
                                sheet.cell(row_number, 5).value.encode('ascii', 'ignore'),
                                sheet.cell(row_number, 0).value.encode('ascii', 'ignore'))


    tokenized_rows = tokenize_words(row_dict)
    workingList = []
    for row in tokenized_rows:
        summaryString = ' '.join(str(x) for x in tokenized_rows[row][0])
        descriptionString = ' '.join(str(x) for x in tokenized_rows[row][1])
        designDecision = row_dict[row][2]
        decisionCategory = row_dict[row][3]
        taskID = row_dict[row][4]
        workingList.append([taskID, summaryString + ' ' + descriptionString, designDecision, decisionCategory])
        writer.writerow((taskID, summaryString + ' ' + descriptionString, designDecision, decisionCategory))

    writer = csv.writer(open("outputFrequency.csv", 'wb'))
    for i in termFreqInvDocFreq(workingList):
        writer.writerow(i.split(','))


##########
    ##Code that was used for the ngrams
    # for row in tokenized_rows:
    #     summary_ngrams = ngram_generator(tokenized_rows[row][0], nvalue)
    #     description_ngram = ngram_generator(tokenized_rows[row][1], nvalue)
    #     generated_ngrams = (summary_ngrams, description_ngram)
    #     for ngram in generated_ngrams:
    #         writer.writerow(list(ngram))

        # print(generated_ngrams)



if __name__ == "__main__":
    main()