# 4751. 다솔이의 다이아몬드 장식 D3
# https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWSNw5jKzwMDFAUr&categoryId=AWSNw5jKzwMDFAUr&categoryType=CODE
for tc in range(1,int(input())+1):
    s=input()
    n=len(s)
    print(".."+"#"+"...#"*(n-1)+"..\n"+"."+"#."*(2*n)+"\n"+"#."+".#.".join(s)+".#\n"+"."+"#."*(2*n)+"\n"+".."+"#"+"...#"*(n-1)+"..")