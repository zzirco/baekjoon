import java.io.*;
import java.util.*;

public class Main_10799 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    ArrayDeque<Character> stack = new ArrayDeque<>();
    int size = s.length();
    int ans = 0;
    for(int i=0; i<size; i++) {
      if(s.charAt(i)=='(') {
        stack.offerLast(s.charAt(i));
      }
      else {
        stack.pollLast();
        if(s.charAt(i-1)=='(') {
          ans += stack.size();
        } else {
          ans += 1;
        }
      }
    }
    System.out.println(ans);
	}
}

