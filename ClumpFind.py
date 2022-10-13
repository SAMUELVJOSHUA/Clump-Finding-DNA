def ClumpFinding(Text, k, L, t):
    """Clump Finding Problem: Find patterns forming clumps in a string.
        Input: A string Genome, and integers k (frequent k-mers), L (cluster/clumps length), and t (time/count).
        Output: All distinct k-mers forming (L, t)-clumps in Genome.
    """
    FrequentPatterns=[]
    for n in range (0,(len(Text)-L)):
        Text_L=Text[n:(n+L)]
        for i in range(0,(len(Text_L)-k)):
            Pattern = Text[i:(i+k)]
            count=PatternCount(Text_L, Pattern)
            if count == t:
                FrequentPatterns.append(Text[i:(i+k)]) #add Text(i, k) to FrequentPatterns
            FrequentPatterns=list(set(FrequentPatterns))  #remove duplicates from FrequentPatterns
    return FrequentPatterns 
 
 

#example
Text='CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
 
k=5
L=75
t=4

ClumpFinding(Text, k, L, t)
