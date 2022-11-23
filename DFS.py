class SearchOneInMatriz: 
    def valor1(self, mat) :
        m = len(mat)
        n = len(mat[0])
        if mat == None or m == 0 or n == 0:
            return 0
        count = 0;    
        visitar = [[False for i in range(n)] for j in range(m)]
        for i in range(0, m):
            for j in range (0, n):
                if mat[i][j] == 1:
                    count+=1
                    self.dfs(mat, i, j, visitar)
        return count

    def dfs(self, mat, i, j, visitar) :
        m = len(mat)
        n = len(mat[0])
        if i < 0 or j < 0 or i > m-1 or j > n-1 or visitar[i][j]:
            return
        if mat[i][j] != 1:
            return    
        mat[i][j] = 0
        visitar[i][j] = True
        self.dfs(mat, i-1, j, visitar); #esquerda
        self.dfs(mat, i+1, j, visitar); #direita
        self.dfs(mat, i, j-1, visitar); #acima
        self.dfs(mat, i, j+1, visitar); #baixo
        self.dfs(mat, i-1, j+1, visitar); #diagonal cima
        self.dfs(mat, i+1, j-1, visitar); #diagonal baixo
        self.dfs(mat, i+1, j+1, visitar); #diagonal geral
matriz = [[1,0,0,0,0,0,0],	
          [1,0,1,1,0,0,0],
          [0,0,1,1,1,0,0],
          [0,1,1,1,1,1,0],
          [1,0,1,0,0,1,0]] 
casas = SearchOneInMatriz()
print("Linhas e coluna: ")
print("Numero de valores unidos com 1: " + str(casas.valor1(matriz)))