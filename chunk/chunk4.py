# ============================
# CHUNKING PRACTICE - BÀI 4
# Structure-based Chunking
# ============================


# 1. Fake document (giữ nguyên)
fake_doc = """
QUY ĐỊNH CHO VAY SME

1. Điều kiện CIC
Khách hàng thuộc CIC nhóm 1 và nhóm 2 được xem xét cấp tín dụng bình thường.
Khách hàng thuộc CIC nhóm 3 có thể được xem xét cấp tín dụng nếu có tài sản đảm bảo có giá trị và được phê duyệt bởi hội đồng tín dụng.
Khách hàng thuộc CIC nhóm 4 và nhóm 5 không đủ điều kiện vay.

2. Tài sản đảm bảo
Ngân hàng chấp nhận bất động sản, ô tô và tiền gửi tiết kiệm.
Tài sản phải được định giá bởi đơn vị thẩm định độc lập.

3. Lãi suất
Lãi suất vay SME dao động từ 8% đến 12% mỗi năm tùy hồ sơ.

4. Quy trình phê duyệt
Hồ sơ được tiếp nhận, thẩm định, phê duyệt và giải ngân trong vòng 10 ngày làm việc.
"""


# 2. Structure-based chunking
def structure_chunk(text):
    chunks = []

    # split theo heading level 1 (số + dấu chấm)
    sections = text.split("\n\n")

    current_title = None
    current_content = []

    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue

        # detect heading (1., 2., 3., ...)
        if sec[0].isdigit() and "." in sec[:3]:
            # lưu chunk cũ
            if current_title:
                chunks.append(current_title + "\n" + "\n".join(current_content))

            # reset chunk mới
            current_title = sec
            current_content = []
        else:
            current_content.append(sec)

    # add chunk cuối
    if current_title:
        chunks.append(current_title + "\n" + "\n".join(current_content))

    return chunks


# 3. Run test
print("\n" + "=" * 60)
print("STRUCTURE-BASED CHUNKING")
print("=" * 60)

chunks = structure_chunk(fake_doc)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
    print("\n" + "-" * 40)
    print(f"[Length: {len(chunk)}]")

print(f"\nTổng số chunk: {len(chunks)}")


# 4. Test question
question = "CIC nhóm 3 có được vay SME không?"

print("\n" + "=" * 60)
print("QUESTION TEST")
print("=" * 60)
print(question)

print("""
Quan sát:

1. CIC nhóm 3 nằm trọn trong chunk nào?
2. Chunk có còn bị cắt câu không?
3. So với recursive, retrieval dễ hơn hay khó hơn?
""")