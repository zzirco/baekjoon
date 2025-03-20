import java.io.*;
import java.util.*;

public class Main_2504 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();
    ArrayDeque<Character> stack = new ArrayDeque<>();
    int size = s.length();
    int ans = 0;
    int tmp = 1;
    for(int i=0; i<size; i++) {
      if(s.charAt(i)=='(') {
        stack.offerLast(s.charAt(i));
        tmp *= 2;
      } else if(s.charAt(i)=='['){
        stack.offerLast(s.charAt(i));
        tmp *= 3;
      } else if(s.charAt(i)==')') {
        if(stack.isEmpty()||stack.peekLast()!='(') {
          System.out.println(0);
          return;
        }
        if(s.charAt(i-1)=='(') {
          ans += tmp;
        }
        stack.pollLast();
        tmp /= 2;
      } else {
        if(stack.isEmpty()||stack.peekLast()!='[') {
          System.out.println(0);
          return;
        }
        if(s.charAt(i-1)=='[') {
          ans += tmp;
        }
        stack.pollLast();
        tmp /= 3;
      }
    }
    if(!stack.isEmpty()) System.out.println(0);
    else System.out.println(ans);
	}
}