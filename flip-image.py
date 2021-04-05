class Solution(object):
    def flipAndInvertImage(self, image):
        
        rows=len(image)
        print(image[0][:][::-1])
        for i in range(rows):
            image[i][:]=image[i][:][::-1]
            
        for i in range(rows):
            for j in range(rows):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
                    
                
                
                
                
                
                
                
                
        return image       