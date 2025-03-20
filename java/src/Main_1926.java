import java.io.*;
import java.util.*;

public class Main_1926 {
  static int[] di = {-1,1,0,0};
  static int[] dj = {0,0,-1,1};
  static int N, M;
  static int[][] map;
  static boolean[][] v;
  static int max = 0;

  static void bfs(int i, int j) {
    ArrayDeque<int[]> q = new ArrayDeque<>();
    q.offer(new int[] {i,j});
    v[i][j] = true;
    int cnt = 1;
    while(!q.isEmpty()) {
      int[] cur = q.poll();
      i = cur[0];
      j = cur[1];
      for(int d=0; d<4; d++) {
        int ni = i + di[d];
        int nj = j + dj[d];
        if(ni>=0&&ni<N&&nj>=0&&nj<M&&!v[ni][nj]&&map[ni][nj]==1) {
          v[ni][nj] = true;
          q.offer(new int[]{ni,nj});
          cnt++;
        }
      }
    }
    max = Math.max(max, cnt);
  }
  public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());
    map = new int[N][M];
    v = new boolean[N][M];
    for(int i=0; i<N; i++) {
      st = new StringTokenizer(br.readLine());
      for(int j=0; j<M; j++) {
        map[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    int cnt = 0;
    for(int i=0; i<N; i++) {
      for(int j=0; j<M; j++) {
        if(map[i][j]==1&&!v[i][j]) {
          bfs(i,j);
          cnt++;
        }
      }
    }
    System.out.println(cnt);
    System.out.println(max);
	}
}

