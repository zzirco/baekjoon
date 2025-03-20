import java.io.*;
import java.util.*;

public class Main_10828 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringBuilder sb = new StringBuilder();
    int N = Integer.parseInt(br.readLine());
    ArrayDeque<Integer> q = new ArrayDeque<>();
    for(int i=0; i<N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      String command = st.nextToken();
      if(command.equals("push")) {
        int n = Integer.parseInt(st.nextToken());
        q.add(n);
      } else if(command.equals("pop")) {
        if(!q.isEmpty()) sb.append(q.pollLast() + "\n");
        else sb.append(-1 + "\n");
      } else if(command.equals("size")) {
        sb.append(q.size() + "\n");
      } else if(command.equals("empty")) {
        sb.append(q.isEmpty()?1:0);
        sb.append("\n");
      } else {
        if(!q.isEmpty()) sb.append(q.peekLast() + "\n");
        else sb.append(-1 + "\n");
      }
    }
    System.out.println(sb);
	}
}
