#Khai bao danh sachs hoc_sinh gom cac chuoi ten cua hoc sinh
hoc_sinh=['Lê Thùy Dung','Trần Đức Hùng','Nguyễn Lan Anh','Mai Phương Thúy']
print(hoc_sinh)

#Khai bao danh sach diem_chu gom cac chuoi ky tu
diem=['A+','A','B+','B','C+','C','D+','D','F']
print(diem)

#Khai bao danh sach gom các so nguyen
list_so=[9,5,8,13,0,4,7,-9,11]
print(list_so)

#Khai bao danh sach voi nhieu kieu du lieu khac nhau
person_info=['Mary',1998,'Tokyo,Japan',1.70,65]
print(person_info)

#Khai bao danh sach rỗng
list_rong=[]
print(list_rong)

#Truy xuat du lieu trong danh sach:
#Hien thi ten hoc sinh ơ vi tri thu 3
print('Học sinh vị trí thứ 3: ',hoc_sinh[2])

#hien thi ten nguoi-chieu cao trong bien person_info
print('Họ tên: ', person_info[0],'---Chiều cao: ',person_info[3])

#Truy xuất nhiều phần tử trong danh sách
print(list_so[3:8])

#Thay đổi giá trị của một phần tử trong danh sách
hoc_sinh=['Lê Thùy Dung','Trần Đức Hùng','Nguyễn Lan Anh','Mai Phương Thúy']
print('Ban đầu: ',hoc_sinh)
hoc_sinh[2]='Nguyễn Thị Lan Anh'
print('Thay đổi: ',hoc_sinh)

list_so=[9,5,8,13,0,4,7,-9,11]
print('Ban đầu: ',list_so)

#Thay giá trị của phần tử cuối cùng trong lits=0
list_so[-1]=0
print('Thay đổi: ',list_so)

list_a=[8,4,8,2]
list_b=[3,0,7,6,5]
#----Cộng hai danh sach (+) ----:
list_ab=list_a +list_b
print('List mới: ',list_ab)

#lấy độ dàu của danh sách list_ab: len(list_ab)
print(list_ab,'Có số phần là: ', len(list_ab))

#Kiểm tra phần tử có thuộc danh sách không?
print(list_ab)

#Kiểm tra phần thử 0:
bol_0=0 in list_ab
print('Phần tử 0 có thuộc list_ab ?', bol_0)

#Kiểm tra phần tử 9:
bol_9=9 in list_ab
print('Phần tử 9 có thuộc list_ab?',bol_9)

print('Danh sách ban đầu: \n',list_ab)

#Thêm phần tử vào cuối danh sách
list_ab.append(10)
print('Danh sách thêm với append:',list_ab)

#Thêm vào vị trí bất kỳ trong danh sách
list_ab.insert(1,100)
print('Thêm phần tử với insert: ',list_ab)
list_ab.extend([7,8,0])
print('Thêm phần tử với extend:',list_ab)

#Xóa phần tử khởi danh sách:
print('Danh sách ban đầu: \n',list_ab)

#Xóa phần tử cuối
list_ab.pop()
print('Danh sách xóa phần tử cuối: \n',list_ab)

#Xóa phần tử tại vị trí số 2
del list_ab[1]
print('Danh sách xóa phần tử ở vị trí số 2:\n', list_ab)

#Xóa phần tử có giá trị 0 xuât hiện đầu tiên
list_ab.remove(0)
print('Xóa phần tử có giá trị 0 đầu tiên: \n', list_ab)

#Đếm số lần xuất hiện của một phần tử trong danh sách
print('Danh sách ban đầu: \n',list_ab)


#Số lần xuất hiện số 1 trong danh sách
print('Số 1 xuất hiện: ', list_ab.count(1))

#Sắp xếp danh sách list_ab: Tăng dần
list_ab=[8,4,8,2,3,0,8,6,5,8]
print('Danh sách ban đầu       :',list_ab)
list_ab.sort()
print('Dnah sách sắp xếp tăng dần:',list_ab)

#Sắp xếp danh sách list_ab: Giảm dần
list_ab=[8,4,8,2,3,0,8,6,5,8]
print('Danh sách ban đầu    :',list_ab)
list_ab.sort(reverse=True)
print('Danh sách sắp xếp giảm dần:',list_ab)

#Đảo ngược danh sách list_ab
list_ab=[8,4,8,2,3,0,8,6,5,8]
print('Danh sách ban đầu   :',list_ab)
list_ab.reverse()
print('Danh sách sau khi đảo ngược:',list_ab)

#Sao chép một danh sách độc lập:
ds_a = [4,5,8,9]
ds_b = ds_a.copy()
ds_b[1] =10
print('Biến ds_a:',ds_a)
print('Biến ds_b:',ds_b)

#Khai báo biến kiểu dữ liệu Boolean:
x=True
y=False
#Khai báo biểu diễn kiểu dữ liệu Boolean qua biểu thức
z=5>8
w=12==12
print('Kiểu dữ liệu của biến x:',type(x),',Giá trị: ',x)
print('Kiểu dữ liệu của biến y:',type(y),',Giá trị: ',y)
print('Kiểu dữ liệu của biến z:',type(z),',Giá trị: ',z)
print('Kiểu dữ liệu của biến w:',type(w),',Giá trị: ',w)
