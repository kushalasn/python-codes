class Solution(object):
    def uniqueMorseRepresentations(self, words):
        vari=0
       
        m = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        l=list()
        p=''
        print(m.values())
        for i in words:
            for j in i:
                p+=m[j]
            l.append(p)
            p=''
                
        return len(set(l))        
            