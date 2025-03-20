import java.io.*;
import java.util.*;

public class Main_17413 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), ">");
		while(st.hasMoreTokens()) {
			String s = st.nextToken();
			String[] sa = s.split("");
			if(sa[0].equals("<")) {
				sb.append(s).append(">");
			} else {
				StringTokenizer st2 = new StringTokenizer(s, "<");
				while(st2.hasMoreTokens()) {
					String inner = st2.nextToken();
					StringTokenizer st3 = new StringTokenizer(inner, " ");
					while(st3.hasMoreTokens()) {
						String inner2 = st3.nextToken();
						String[] str = inner2.split("");
						String[] tmp = new String[str.length];
						for(int i=0; i<str.length; i++) {
							tmp[i] = str[str.length-1-i];
							sb.append(tmp[i]);
						}
						sb.append(" ");
					}
					String outter = st2.nextToken();
					sb.append("<").append(outter).append(">");
				}
			}
		}
		System.out.println(sb.toString());
		br.close();
	}
}
