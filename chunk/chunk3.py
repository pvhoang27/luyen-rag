# ============================
# CHUNKING PRACTICE - BÀI 5 (FIXED)
# Semantic Chunking - rõ ràng từng bước
# ============================

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


# 1. Fake document
fake_doc = """
QUY ĐỊNH CHO VAY SME

Khách hàng thuộc CIC nhóm 1 và nhóm 2 được xem xét cấp tín dụng bình thường.
Khách hàng thuộc CIC nhóm 3 có thể được xem xét cấp tín dụng nếu có tài sản đảm bảo.

Tài sản phải được định giá bởi đơn vị thẩm định độc lập.

Lãi suất vay SME dao động từ 8% đến 12% mỗi năm tùy hồ sơ.

Hồ sơ được tiếp nhận, thẩm định, phê duyệt và giải ngân trong vòng 10 ngày làm việc.
"""


# 2. Split sentences rõ ràng
sentences = [s.strip() for s in fake_doc.split("\n") if s.strip()]


# 3. Vector hóa
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)


# 4. Semantic chunking (debug version)
threshold = 0.3

chunks = []
current_chunk = [sentences[0]]

print("\n===== SENTENCES =====")
for i, s in enumerate(sentences):
    print(f"{i+1}. {s}")

print("\n===== BUILDING CHUNKS =====")

for i in range(1, len(sentences)):

    prev_vec = vectors[i - 1]
    curr_vec = vectors[i]

    sim = cosine_similarity(prev_vec, curr_vec)[0][0]

    print(f"\nSo sánh:")
    print(f"- Câu trước: {sentences[i-1]}")
    print(f"- Câu hiện tại: {sentences[i]}")
    print(f"- Similarity: {sim:.4f}")

    if sim > threshold:
        print("=> GỘP vào chunk hiện tại")
        current_chunk.append(sentences[i])
    else:
        print("=> TẠO chunk mới")
        chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i]]

# add chunk cuối
if current_chunk:
    chunks.append(" ".join(current_chunk))


# 5. In kết quả rõ ràng
print("\n" + "=" * 60)
print("FINAL CHUNKS")
print("=" * 60)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
    print("-" * 40)

print(f"\nTổng số chunk: {len(chunks)}")