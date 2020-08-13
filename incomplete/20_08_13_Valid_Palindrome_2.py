# Andre Doumad
#TODO: speed this up, it works, but it's too slow.
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
    def validPalindrome(self, s: str) -> bool:
        backwards = ''
        for letter in reversed(s):
            backwards += letter
        if backwards == s:
            return True
        for i in range(0, len(backwards)):
            temp_backwards = ''
            for j in range(0, len(backwards)):
                if j != i:
                    temp_backwards += backwards[j]
            temp_forwards = ''
            for letter in reversed(temp_backwards):
                temp_forwards += letter
            if temp_backwards == temp_forwards:
                return True
        return False

import unittest, time
class UnitTest(unittest.TestCase):
    def test_a(self):
        solution = Solution()

        # start_time = time.time()
        # result = solution.validPalindrome('aba')
        # print('result ', result)
        # print('processing time: ', time.time() - start_time)

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
