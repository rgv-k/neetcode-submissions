class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> set1 = new HashSet<>();
        for(int i = 0; i < 9;i++){
            for(int j = 0; j < 9; j++){
            if(set1.contains(board[i][j])) return false;
            else if(board[i][j] != '.') set1.add(board[i][j]);
            }

            set1.clear();
        }

        for(int i = 0; i < 9;i++){
            for(int j = 0; j < 9; j++){
            if(set1.contains(board[j][i])) return false;
            else if(board[j][i] != '.') set1.add(board[j][i]);
            }

            set1.clear();
        }

        int[][] start = {
            {0,0}, {0,3}, {0,6},
            {3,0}, {3,3}, {3,6},
            {6,0}, {6,3}, {6,6}};
        
        for(int[] points: start){
            for(int i = points[0]; i < points[0]+3; i++){
                for(int j = points[1]; j < points[1]+3;j++){
                    if(set1.contains(board[i][j])) return false;
                    else if(board[i][j] != '.') set1.add(board[i][j]);
                }

                

            }
            set1.clear();
        }

        return true;
    }
        
}

