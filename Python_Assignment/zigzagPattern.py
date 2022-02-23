class Solution(object):
    def convert(self, s, numRows):
        start=0
        ch_str=""
        l_str=""
        m_str=""
        for ch in range(start,len(s),numRows):
            ch_str = ch_str+s[ch]+" "
            start=start+1
            for l in range(start,len(s),numRows):
                l_str =l_str+s[l]
                start=start+1
                l_str =l_str+s[start]
                start=start+1
                break
            for m in range(start,len(s),numRows):
                m_str =m_str+s[m]+" "
                start=start+1
                break




        print(ch_str)
        print(l_str)
        print(m_str)



sol=Solution()
sol.convert("Rameswari",3)

