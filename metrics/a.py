from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy
)

# dữ liệu test
data = {
    "question": [
        "CIC nhóm 3 có vay SME được không?"
    ],

    "answer": [
        "Khách hàng CIC nhóm 3 có thể vay nếu có tài sản đảm bảo."
    ],

    "contexts": [[
        "Theo chính sách ngân hàng, khách hàng có CIC nhóm 3 trở lên không đủ điều kiện vay SME."
    ]],

    "ground_truth": [
        "Khách hàng có CIC nhóm 3 không đủ điều kiện vay SME."
    ]
}

dataset = Dataset.from_dict(data)

# evaluate
result = evaluate(
    dataset,
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy
    ]
)

print(result)