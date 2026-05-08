# ============================
# CHUNKING PRACTICE - BÀI 3
# Recursive Chunking (basic version)
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


# 2. Recursive chunking function
def recursive_chunk(text, max_size):
    separators = ["\n\n", "\n", ". ", " ", ""]

    def split(text, separators):
        if len(text) <= max_size:
            return [text]

        for sep in separators:
            if sep in text:
                parts = text.split(sep)
                chunks = []
                current = ""

                for part in parts:
                    # +1 để giữ separator
                    candidate = current + part + sep

                    if len(candidate) <= max_size:
                        current = candidate
                    else:
                        if current:
                            chunks.append(current.strip())
                        current = part + sep

                if current:
                    chunks.append(current.strip())

                # nếu tách được thì return luôn
                if len(chunks) > 1:
                    return chunks

        # fallback: cắt cứng
        return [text[i:i+max_size] for i in range(0, len(text), max_size)]

    return split(text, separators)


# 3. Test
chunk_size = 200

print("\n" + "=" * 60)
print(f"RECURSIVE CHUNKING - SIZE = {chunk_size}")
print("=" * 60)

chunks = recursive_chunk(fake_doc, chunk_size)

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
Quan sát và trả lời:

1. Chunk có còn bị cắt giữa câu không?
2. CIC nhóm 3 nằm trọn trong chunk nào?
3. So với fixed-size + overlap, cái nào “hiểu văn bản” tốt hơn?
""")