import java.io.*;
import java.util.*;

public class Main_1406 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		LinkedList<Character> list = new LinkedList<>();
		String s = br.readLine();
		int N = s.length();
		for(int i=0; i<N; i++) {
			list.add(s.charAt(i));
		}
		int M = Integer.parseInt(br.readLine());
		ListIterator<Character> it = list.listIterator();
		while(it.hasNext()) it.next();
		for(int i=0; i<M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			char command = st.nextToken().charAt(0);
			if(command=='L') {
				if(it.hasPrevious()) it.previous();
			} else if(command=='D') {
				if(it.hasNext()) it.next();
			} else if(command=='B') {
				if(!it.hasPrevious()) continue;
				it.previous();
				it.remove();
			} else {
				char c = st.nextToken().charAt(0);
				it.add(c);;
			}
		}
		for(Character c : list) {
			bw.write(c);
		}
		bw.flush();
	}
}
