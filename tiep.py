# Hàm định nghĩa trợ lý ảo đưa ra khuyến nghị uống thuốc khi đau đầu
def tro_ly_dau_dau():
    print("Xin chào! Tôi là trợ lý của bạn. Bạn đau đầu à?")

    # Yêu cầu người dùng xác nhận có đau đầu hay không
    tra_loi = input("Bạn có đau đầu không? (có/không) ")

    if tra_loi.lower() == "có":
        print("Bạn nên uống thuốc gì?")

        # Hỏi người dùng về loại thuốc muốn uống
        print("Có thể bạn nên dùng Paracetamol hoặc Ibuprofen.")
        thuoc = input("Bạn muốn dùng Paracetamol hay Ibuprofen? ")

        # Đưa ra lời khuyên tùy thuốc được chọn
        if thuoc.lower() == "paracetamol":
            print("Uống 1 viên Paracetamol (500mg) mỗi 4-6 giờ nếu cần.")
        elif thuoc.lower() == "ibuprofen":
            print("Uống 1 viên Ibuprofen (400mg) mỗi 4-6 giờ nếu cần.")
        else:
            print("Xin lỗi, tôi không hiểu loại thuốc này.")
    else:
        print("Nếu bạn có cảm giác đau đầu, nên nghỉ ngơi và giữ sức khỏe.")

# Gọi hàm để trợ lý ảo bắt đầu tương tác
tro_ly_dau_dau()
