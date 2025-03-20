import java.io.*;
import java.util.*;

public class Main_2178 {
  static int[] di = {-1,1,0,0};
  static int[] dj = {0,0,-1,1};
  static int N, M;
  static int[][] map;
  static boolean[][] v;

  static int bfs(int i, int j, int cnt) {
    ArrayDeque<int[]> q = new ArrayDeque<>();
    q.offer(new int[]{i,j,cnt});
    v[i][j] = true;
    while(!q.isEmpty()) {
      int[] cur = q.poll();
      i = cur[0];
      j = cur[1];
      cnt = cur[2];
      if(i==N-1&&j==M-1) return cnt;
      for(int d=0; d<4; d++) {
        int ni = i + di[d];
        int nj = j + dj[d];
        if(ni>=0&&ni<N&&nj>=0&&nj<M&&!v[ni][nj]&&map[ni][nj]==1) {
          v[ni][nj] = true;
          q.offer(new int[] {ni,nj,cnt+1});
        }
      }
    }
    return 0;
  }
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    map = new int[N][M];
    v = new boolean[N][M];
    for(int i=0; i<N; i++) {
      String[] sarr = br.readLine().split("");
      for(int j=0; j<M; j++) {
        map[i][j] = Integer.parseInt(sarr[i]);
      }
    }
    System.out.println(bfs(0,0,1));
  }
}
