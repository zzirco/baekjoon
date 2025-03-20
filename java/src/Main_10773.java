import java.io.*;
import java.util.*;

public class Main_10773 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    ArrayDeque<Integer> q = new ArrayDeque<>();
    for(int i=0; i<N; i++) {
      int num = Integer.parseInt(br.readLine());
      if(num==0) q.pollLast();
      else q.add(num); 
    }
    int sum = 0;
    for(int n : q) {
      sum += n;
    }
    System.out.println(sum);
	}
}

