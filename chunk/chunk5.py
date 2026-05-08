# ============================
# CHUNKING PRACTICE - BÀI 5
# Semantic Chunking (simple version)
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


# 2. Split sentences
sentences = [s.strip() for s in fake_doc.split("\n") if s.strip()]


# 3. Convert sentences to vectors (TF-IDF demo)
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)


# 4. Semantic chunking
threshold = 0.3
chunks = []

current_chunk = [sentences[0]]

for i in range(1, len(sentences)):
    sim = cosine_similarity(
        vectors[i - 1],
        vectors[i]
    )[0][0]

    if sim > threshold:
        current_chunk.append(sentences[i])
    else:
        chunks.append(" ".join(current_chunk))
        current_chunk = [sentences[i]]

# add last chunk
if current_chunk:
    chunks.append(" ".join(current_chunk))


# 5. Print result
print("\n" + "=" * 60)
print("SEMANTIC CHUNKING")
print("=" * 60)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
    print("-" * 40)


print(f"\nTổng số chunk: {len(chunks)}")