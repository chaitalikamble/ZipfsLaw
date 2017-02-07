#Description:   This program reads in a text file and applies a Zipfs law to the text contained in it.
#               It then outputs a chart consisting of Words, their frequencies, Rank and Probabilities.
#               Course homework for Topics in Data Management
#Author:        Chaitali Sudam Kamble (csk3565)
#Date:          02/05/2017
#Version:       1.0
import matplotlib.pyplot as plt
class ZipfsLaw:
    '''
    This class shows a chart for Zipfs Law
    '''
    global dict
    dict = {}
    def process(word):
        '''
        This method reads the word one by one and update the dictionary to maintain word frequency
        :param Word: A word to process
        :return:None
        '''
        if word not in dict:
            word = word
            dict.update({word : 1})
        else:
            value = dict.get(word)
            value = value + 1
            dict.update({word : value})

    def applyLaw(sorted_dict, TotalWords):
        '''
        :param TotalWords: Total number of words in a text file
        :param sorted_dict: Sorted dictionary in descending order
        :return: None
        '''
        rank = 1
        print("Zipfs Law results:")
        f = []
        r = []
        for word,frequency in sorted_dict:
            if rank == 11:
                break
            probability = frequency/TotalWords
            f.append(frequency)
            r.append(rank)
            rankProb = rank * probability
            print("| WORD: ", word, "| Frequency: ", frequency,"| Rank: ", rank,"| Probability: ", probability, "| rPr: " , rankProb)
            rank = rank + 1
        plt.plot(f, r, 'ro')
        plt.show()

def main():
        '''
        Main method, execution starts here
        :return: None
        '''
        fileName = input("Enter your input filename : ") #Read input file(full path) from user
        TotalWords = 0
        list = (None, " ", "", '',' ')
        with open(fileName) as f:
            for line in f:
                line = line.strip()
                line = line.split(" ")
                for word in line:
                    if word in list:
                        pass
                    else:
                        word = ''.join(e for e in word if e.isalnum()) #Remove special characters
                        if word in list:
                            pass
                        else:
                            ZipfsLaw.process(word.lower())
                            TotalWords = TotalWords + 1
        sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse = True) #Sort dictionary in descending order
        ZipfsLaw.applyLaw(sorted_dict, TotalWords)

if __name__ == '__main__':
    main()







