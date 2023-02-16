# Cho một xâu X có chiều dài N ký tự. Xâu X chỉ gồm 2 loại ký tự 'A' và 'B'.
# Một xâu Y được gọi lại xâu con của X nếu thỏa mãn các tính chất sau:
#       + Y là một đoạn ký tự liên tiếp xủa xâu X
#       + Có chiều dài L<=M (M cho trước)
#       + Có K ký tự 'A'
# Ví dụ: X là : AABAA
# Với M=3 và K=2 thì xâu AAB hoặc AA là 1 xâu con của X.
# Viết chương trình python tìm xâu con của X

# X = 'AABAA'
# AA - AB -BA -AA: -> AA | AA
# AAB - ABA - BAA -> AAB | ABA | BAA
# 'AAB'.count('A') >= K
# Sử dụng 2 vòng lặp
# M = 3
# K = 2

# Y là đoạn xâu cần tìm:
# len(Y) <= 3
str_X = "AABAA"
M = int(input("Nhap gia tri M:"))
K = int(input("Nhap gia tri K:"))
for k in range(K, M+1):
    for i in range(len(str_X)-k+1):
        sub_str_X = str_X[i:i+k]
        if sub_str_X.count("A") >= K:
            print(sub_str_X)

