"""Question1 : create a function break down the a sentence to words, and put adjcent words together in a tuple, we want to output all the piars."""
sentence = """Have free hours and love children? Drive kids to school, soccer practice and other activities."""

def foundpairs(str):
    str=str.replace('?', '').replace(',', '').replace(',', '')
    arr=str.split(' ')
    Out=[]
    for i in range(0,len(arr)-2):
        s=(arr[i],arr[i+1])
        Out.append(s)
    return Out
result=foundpairs(sentence)
print(result)




"""Question2 : Replace words with stems
In data science, there exists the concept of stemming, which is the heuristic of chopping off the end of a word to clean and bucket it into an easier feature set. 
Given a dictionary consisting of many roots and a sentence, write a function replace_words to stem all the words in the sentence with the root forming it. If a word has many roots that can form it, replace it with the root with the shortest length.
"""


roots = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
def split(sentence):
    return sentence.split(' ')
def replaceword(root,arr):
    
    for i in range(0,len(arr)):
        for j in root:
            if j in arr[i]:
                arr[i]=j
                
r=split(sentence)
replaceword(roots, r)
print(r)