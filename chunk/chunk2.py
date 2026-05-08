# ============================
# CHUNKING PRACTICE - BÀI 2
# Fixed-size + Overlap Chunking
# ============================

# 1. Fake document
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


# 2. Fixed-size + overlap chunking
def chunk_with_overlap(text, chunk_size, overlap):
    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        # tránh vòng lặp vô hạn
        if end >= text_length:
            break

        start = start + chunk_size - overlap

    return chunks


# 3. Test nhiều chunk size + overlap
chunk_size = 200
overlap = 50

print("\n" + "=" * 60)
print(f"CHUNK SIZE = {chunk_size}, OVERLAP = {overlap}")
print("=" * 60)

chunks = chunk_with_overlap(fake_doc, chunk_size, overlap)

for idx, chunk in enumerate(chunks):
    print(f"\n--- Chunk {idx + 1} ---")
    print(chunk)
    print("\n" + "-" * 40)
    print(f"[Length: {len(chunk)} characters]")

print(f"\nTổng số chunk: {len(chunks)}")


# 4. Test question
question = "CIC nhóm 3 có được vay SME không?"

print("\n" + "=" * 60)
print("QUESTION TEST")
print("=" * 60)
print(question)

print("""
Quan sát output và trả lời:

1. Overlap có giúp giảm việc cắt đôi câu không?
2. Chunk nào chứa đủ thông tin CIC nhóm 3?
3. So với fixed-size, retrieval có ổn hơn không?
""")