package Tools;

import java.util.List;

public class CommonUtils {
    public static String fillZeroBeforeString(String str , int length) {
        return fillStringBeforeString(str,"0",length);
    }
    public static String fillStringBeforeString(String str ,String fill, int length) {
        if(str.length() < length) {
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < length - str.length() ; i++) {
                sb.append(fill);
            }
            sb.append(str);
            return sb.toString();
        }else {
            return str;
        }
    }
    private static int[] getNext(char[] p)
    {
        /**
         * 已知next[j] = k, 利用递归的思想求出next[j+1]的值
         * 1.如果p[j] = p[k]，则next[j+1] = next[k] + 1;
         * 2.如果p[j] != p[k],则令k = next[k],如果此时p[j] == p[k],则next[j+1] = k+1
         * 如果不相等，则继续递归前缀索引，令k=next[k],继续判断，直至k=-1(即k=next[0])或者p[j]=p[k]为止
         */
        int plen = p.length;
        int[] next = new int[plen];
        int k = -1;
        int j = 0;
        next[0] = -1;                //这里采用-1做标识
        while(j < plen -1)
        {
            if(k == -1 || p[j] == p[k])
            {
                ++k;
                ++j;
                next[j] = k;
            }
            else
            {
                k = next[k];
            }
        }

        return next;
    }
    public static int kmpStringMatch(String source, String pattern)
    {
        int i = 0;
        int j = 0;
        char[] s = source.toCharArray();
        char[] p = pattern.toCharArray();
        int slen = s.length;
        int plen = p.length;
        int[] next = getNext(p);
        while(i < slen && j < plen)
        {
            if(j == -1 || s[i] == p[j])
            {
                ++i;
                ++j;
            }
            else
            {
                //如果j != -1且当前字符匹配失败，则令i不变，
                //j = next[j],即让pattern模式串右移j - next[j]个单位
                j = next[j];
            }
        }
        if(j == plen)
            return i - j;
        else
            return -1;
    }
}
