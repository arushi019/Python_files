import unittest
from ip_hw3 import *
class sample(unittest.TestCase):
    def testobK(self):
        self.assertEqual(offbyK("power","rover",1),False)
        self.assertEqual(offbyK("power and war","rover and car",3),True)
        self.assertEqual(offbyK("1#satire","2#retire",3),True)
        self.assertEqual(offbyK("pikachu","kipachu",0),False)
        self.assertEqual(offbyK("thankstocode","sharkstocode",2),True)
    def testob(self):
        self.assertEqual(offbySwaps("pikachu","kipachu"),True)
        self.assertEqual(offbySwaps("1barn","bran1"),True)
        self.assertEqual(offbySwaps("st rw te","wt rs te"),True)
        self.assertEqual(offbySwaps("newton","wanton"),False)
        self.assertEqual(offbySwaps("#trend $blend","$brend #tlend"),True)
    def testextra(self):
        self.assertEqual(offbyKExtra("demand","dnam78ed",2),True)
        self.assertEqual(offbyKExtra("bulba saur@","saur tyrant@",2),False)
        self.assertEqual(offbyKExtra("may i help?","help? may i think",6),True)
        self.assertEqual(offbyKExtra("mango pick","pickled@mango",2),False)
        self.assertEqual(offbyKExtra("arduinos on roll","rollon $ arduinos",1),True)
    def testcomp(self):
        self.assertEqual(compare_distr([6,9,8,11,3,1,4,6,7],[32,21,31,26,34,21,30,22,27],3),False)
        self.assertEqual(compare_distr([17,15,14,11,13,16],[66,67,71,75,65,78],1),False)
        self.assertEqual(compare_distr([21,24,26,27,29,23],[76,82,84,79,81,78],4),True)
        self.assertEqual(compare_distr([45,56,34,78,67,89,23],[90,68,57,35,24,79,46],9),True)
        self.assertEqual(compare_distr([66,89,87,99,110,71,67,72],[121,112,101,131,119,137,104,108],4),False)
    def testnearstring(self):
        l1=[]
        l2=[]
        l3=[]
        l4=[]
        l5=[]
        l1=fileToStringList("EnglishWords.txt","ab")
        l2=fileToStringList("EnglishWords.txt","tre")
        l3=fileToStringList("EnglishWords.txt","str")
        l4=fileToStringList("EnglishWords.txt","is")
        l5=fileToStringList("EnglishWords.txt","the")
        self.assertEqual(ListOfNearStrings("absolve",l1,2),['abalone', 'abalones', 'ablates', 'ables', 'ablest', 'abodes', 'abolish', 'above', 'absolute', 'absolvers', 'abusive'])
        self.assertEqual(ListOfNearStrings("treble",l2,5),['treachery', 'treasonable', 'treasurable', 'treasured', 'treasurer', 'treasures', 'treatises', 'treatment', 'trematode', 'trenchers', 'trendiest', 'trepanned', 'trephined', 'trephines', 'tressiest'])
        self.assertEqual(ListOfNearStrings("straight",l3,2),['straighted', 'straighten', 'straighter', 'straightly', 'strait', 'straiten', 'straiter', 'straitly', 'strategic', 'strategy', 'strath', 'stratify', 'strawhat', 'strength', 'striate', 'striated', 'striates', 'striating'])
        self.assertEqual(ListOfNearStrings("isomer",l4,5),['islanded', 'islanders', 'islands', 'isoclines', 'isolators', 'isomerizing', 'isometrical', 'isopropyl', 'isosceles', 'isostasy', 'isotonic', 'isotopic', 'isotropic', 'israelite', 'issuable', 'issuance', 'issuant', 'issuing', 'isthmian', 'isthmuses'])
        self.assertEqual(ListOfNearStrings("theta",l5,2),['the', 'theater', 'theatre', 'theft', 'thefts', 'their', 'theist', 'them', 'theme', 'then', 'thens', 'there', 'thereat', 'therm', 'these', 'thew', 'thews', 'thewy', 'they'])
if __name__=='__main__':
    unittest.main()
