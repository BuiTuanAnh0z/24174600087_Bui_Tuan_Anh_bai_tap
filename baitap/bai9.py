# Nhập loại xe
loai_xe = int(input("Nhập loại xe (4 hoặc 7): "))

# Kiểm tra loại xe hợp lệ
if loai_xe == 4 or loai_xe == 7:
    # Nhập khoảng cách di chuyển (km) và thời gian chờ (phút)
    khoang_cach = float(input("Nhập khoảng cách di chuyển (km): "))
    thoi_gian_cho = float(input("Nhập thời gian chờ (phút): "))

    # Tính cước taxi
    if loai_xe == 4:
        # Cước cho xe 4 chỗ
        cuoc_mo_cua = 11000  # đồng
        cước_km_1_20 = 12100  # đồng/km
        cước_km_tren_21 = 10000  # đồng/km
        
        if khoang_cach <= 0.8:
            cuoc = cuoc_mo_cua
        elif khoang_cach <= 20:
            cuoc = cuoc_mo_cua + (khoang_cach - 0.8) * cước_km_1_20
        else:
            cuoc = cuoc_mo_cua + (20 - 0.8) * cước_km_1_20 + (khoang_cach - 20) * cước_km_tren_21
            
    elif loai_xe == 7:
        # Cước cho xe 7 chỗ
        cuoc_mo_cua = 13000  # đồng
        cước_km_1_30 = 14100  # đồng/km
        cước_km_tren_31 = 12000  # đồng/km
        
        if khoang_cach <= 0.8:
            cuoc = cuoc_mo_cua
        elif khoang_cach <= 30:
            cuoc = cuoc_mo_cua + (khoang_cach - 0.8) * cước_km_1_30
        else:
            cuoc = cuoc_mo_cua + (30 - 0.8) * cước_km_1_30 + (khoang_cach - 30) * cước_km_tren_31

    # Tính tiền chờ
    if thoi_gian_cho > 5:
        thoi_gian_cho_tinh = thoi_gian_cho - 5  # phút được tính tiền
        tien_cho = thoi_gian_cho_tinh * 800  # đồng
    else:
        tien_cho = 0  # miễn phí

    # Tổng cước
    tong_cuoc = cuoc + tien_cho

    # In kết quả
    print(f"Tổng cước taxi là: {tong_cuoc:.0f} đồng.")
else:
    print("Loại xe không hợp lệ. Vui lòng nhập 4 hoặc 7.")
