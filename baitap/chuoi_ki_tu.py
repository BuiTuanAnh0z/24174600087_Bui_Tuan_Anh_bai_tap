dem_tu <- function(cau) {
  # Loại bỏ khoảng trắng thừa giữa các từ
  cau <- gsub("\\s+", " ", cau)
  
  # Xóa khoảng trắng đầu và cuối
  cau <- trimws(cau)
  
  # Tách câu thành danh sách các từ
  tu <- unlist(strsplit(cau, " "))
  
  # Đếm số lượng từ
  so_luong_tu <- length(tu)
  
  # Trả về số lượng từ và danh sách từ
  list(so_luong_tu = so_luong_tu, cac_tu = tu)
}

# Ví dụ sử dụng
chuoi <- "Hom nay    troi mua   mua"
ket_qua <- dem_tu(chuoi)
print(ket_qua)
