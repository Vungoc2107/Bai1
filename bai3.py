# Khởi tạo danh sách điểm của lớp Vin_2021
diem_thi = ['C', 'B', 'D', 'A', 'F', 'A', 'B', 'F', 'B', 'B', 'C', 'A', 'D', 'F', 'B']

# Tính số sinh viên trong lớp
so_sinh_vien = len(diem_thi)

# Tính số sinh viên phải học lại (điểm F)
so_sinh_vien_hoc_lai = diem_thi.count('F')

# Tính số sinh viên có điểm từ B trở lên
so_sinh_vien_B_trở_lên = diem_thi.count('B') + diem_thi.count('A')

# Tìm vị trí của sinh viên đầu tiên và cuối cùng đã nghỉ học
vi_tri_sinh_vien_dau_tien_da_nghi_hoc = diem_thi.index('F')
vi_tri_sinh_vien_cuoi_cung_da_nghi_hoc = len(diem_thi) - 1 - diem_thi[::-1].index('F')

# Tạo một bảng điểm mới loại bỏ điểm của các sinh viên đã nghỉ học
diem_thi_moi = diem_thi[:vi_tri_sinh_vien_dau_tien_da_nghi_hoc] + diem_thi[vi_tri_sinh_vien_cuoi_cung_da_nghi_hoc + 1:]

# In thông tin
print("Số sinh viên trong lớp:", so_sinh_vien)
print("Số sinh viên phải học lại (điểm F):", so_sinh_vien_hoc_lai)
print("Số sinh viên có điểm từ B trở lên:", so_sinh_vien_B_trở_lên)
print("Bảng điểm mới sau khi loại bỏ điểm của sinh viên đầu tiên và cuối cùng đã nghỉ học:", diem_thi_moi)

