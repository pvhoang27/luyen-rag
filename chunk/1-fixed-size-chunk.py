# ============================
# FIXED-SIZE CHUNKING PRACTICE
# ============================

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


# chỉnh số này thôi
chunk_size = 200


def fixed_chunk(text, chunk_size):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


chunks = fixed_chunk(fake_doc, chunk_size)

print(f"\nChunk size: {chunk_size}")
print(f"Tổng số chunk: {len(chunks)}")

for idx, chunk in enumerate(chunks):
    print("\n" + "=" * 60)
    print(f"CHUNK {idx + 1}")
    print("=" * 60)
    print(chunk)