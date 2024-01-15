package baekjoon;

import java.io.*;
import java.util.*;

public class Solution_17413_단어뒤집기2 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		while(st.hasMoreTokens()) {
			String s = st.nextToken();
			StringTokenizer st2 = new StringTokenizer(s, "<");
			while(st2.hasMoreTokens()) {
				String inner = st2.nextToken();
				StringTokenizer st3 = new StringTokenizer(inner, ">");
				String outter = st3.nextToken();
				sb.append("<").append(outter).append(">");
				//String outter2 = st3.nextToken();
				String[] str = outter.split("");
				String[] tmp = new String[str.length];
				for(int i=0; i<str.length; i++) {
					tmp[i] = str[str.length-1-i];
					sb.append(tmp[i]);
				}
				sb.append(" ");
				sb.append(outter);
			}
		}
		System.out.println(sb.toString());
		br.close();
	}
}
