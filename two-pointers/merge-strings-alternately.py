class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        i = len(word1.strip())
        j = len(word2.strip())
        ran = (min(i,j))

        for k in range(ran):
            string =  string + word1[k] + word2[k]
            print(string)

        if (len(string)) != (i + j):
            if j > i:
                string = string + word2[j-(j-i):]

            elif i > j:
                string = string + word1[i - (i-j):]
         
        return(string)