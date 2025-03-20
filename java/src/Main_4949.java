import java.io.*;
import java.util.*;

public class Main_4949 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    while (true) {
      String s = br.readLine();
      if(s.equals(".")) break;
      int size = s.length();
      ArrayDeque<Character> q = new ArrayDeque<>();
      boolean flag = true;
      for(int i=0; i<size; i++) {
        char c = s.charAt(i);
        if(c=='('||c=='[') {
          q.offerLast(c);
        } else if(c==')') {
          if(q.isEmpty()) {
            flag = false;
            break;
          }
          if(q.peekLast()=='(') q.pollLast();
          else {
            flag = false;
            break;
          }
        } else if(c==']') {
          if(q.isEmpty()) {
            flag = false;
            break;
          }
          if(q.peekLast()=='[') q.pollLast();
          else {
            flag = false;
            break;
          }
        }
      }
      if(!q.isEmpty()) flag = false;
      if(flag) sb.append("yes\n");
      else sb.append("no\n");
    }
    System.out.println(sb);
	}
}
