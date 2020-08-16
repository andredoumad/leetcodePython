# Andre Doumad
'''
This problem was asked by Amazon.

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution:
    def test(self, s, i, j):
        while i<j:
            if s[i] != s[j]:
                return False

            i,j = i+1, j-1
        return True

    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] != s[j]:
                return self.test(s, i+1, j) or self.test(s, i, j-1)
        return True


import unittest, time
class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        start_time = time.time()
        result = solution.validPalindrome('aba')
        print('result ', result)
        print('processing time: ', time.time() - start_time)

        start_time = time.time()
        result = solution.validPalindrome('abca')
        print('result ', result)
        print('processing time: ', time.time() - start_time)

        start_time = time.time()
        result = solution.validPalindrome('dbrlaxkecqlesjhsuqslravbmdvnlgfspcvimrtdqdcqqlaqxtrrqiuarjclkilbtkkenqgknuosqtrtrrduleffhgzszeczrnxdrwkjiudibnbfxtqmtcnxrpiicgvpxgnjjclyqkwitkswrfuqgsvzopfkjpnocrhifahjaaejmtrvczuzobqoatjwcixtcnpdggsfdyscqcllfdmysdtqpfpzrbltzsonkqtgvuidqszjgqeeglljokllcphfmpsduzjkjrodtfirpcyxpbbykmkhfmedfedjjrbycpdjlqiqywklfxzctrtbnuhpluvmoofxokyaxkcnkkvylnzjfuyoobtuymndyezxrtekfkldlijakaencgfkpikwfsyxtvzqdmvaexpdfwnsoblawlsycmvyvhnextjwjndapcpnvsnztibkjjhhrhyjrdsrfzyrtgetpxjxzcaaehjnpinqsgzykvraifdfaoggcyfrmbuhzctjzueqsiivwfquuwszjwhixonlklzvkkvgczskyseetcrcychdehshhpkouwstaeymviuursatmlliurcabuuxrmislauavikjuvjpdcfqnnzwflcepdvaqbfzdcogtuljvoebldxmlfhbgnxvxaagpepmzbzsmcemyxhrobkqbpwilkwnepubmdugssrwbmogezbttgxhdldqckivmponkbwkrjksfdpbsemmjdbsipxkdvfsvqmtshogqeufiolcndfdjyauwpxkogfjicxtktsuioecmlyxqwwgbuuzwwdktdktjldmptpfpzoivxzeuotzcwfuyhghjjhejuechcrjfcbchjijephldsamuqtryoovvdqhfeecertmjouhbfxlemtmvdpmymrfqwschttlplljzzpiqmydgcppfqdwtqbjxtlkseuklytzqniakliclvgvhhkalsttwsgcoqdxawdzrtvnybmgescvromhwndfzzfdnwhmorvcsegmbynvtrzdwaxdqocgswttslakhhvgvlcilkainqztylkueskltxjbqtwdqfppcgdymqipzzjllpltthcswqfrmympdvmtmelxfbhuojmtreceefhqdvvooyrtqumasdlhpejijhcbcfjrchceujehjjhghyufwcztouezxviozpfptpmdljtkdtkdwwzuubgwwqxylmceoiustktxcijfgokxpwuayjdfdncloifueqgohstmqvsfvdkxpisbdjmmesbpdfsqkjrkwbknopmvikcqdldhxgttbzegombwrssgudmbupenwkliwpbqkborhxymecmszbzmpepgaaxvxngbhflmxdlbeovjlutgocdzfbqavdpeclfwznnqfcdpjvujkivaualsimrxuubacruillmtasruuivmyeatswuokphhshedhcycrcteesykszcgvkkvzlklnoxihwjzswuuqfwviisqeuzjtczhubmrfycggoafdfiarvkyzgsqnipnjheaaczxjxptegtryzfrsdrjyhrhhjjkbitznsvnpcpadnjwjtxenhvyvmcyslwalbosnwfdpxeavmdqzvtxysfwkipkfgcneakajildlkfketrxzeydnmyutbooyufjznlyvkknckxaykoxfoomvulphunbtrtczxflkwyqiqljdpcybrjjdefdemfhkmkybbpxycpriftdorjkjzudspmfhpcllkojllgeeqgjzsqdiuvgtqknosztlbrzpfpqtdsymdfllcqcsydfsggdpnctxicwjtaoqbozuzcvrtmjeaajhafihrconpjkfpozvsgqufrwsktiwkqylcjjngxpvgciiprxnctmqtxfbnbiduijkwrdxnrzcezszghffeludrrtrtqsounkgqnekktblikljrauiqrrtxqalqqcdqdtrmivcpsfglnvdmbvarlsqushjselqcekxalrbd')
        print('result ', result)
        print('processing time: ', time.time() - start_time)
        

if __name__=='__main__':
    unittest.main()

'''
output:
result  True
processing time:  1.5497207641601562e-05
result  True
processing time:  3.814697265625e-06
result  False
processing time:  7.343292236328125e-05
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''