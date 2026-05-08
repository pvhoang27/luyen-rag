from datasets import Dataset

data = {
    "question": [
        "CIC nhóm 3 có được vay SME không?"
    ],

    "contexts": [[
        "Khách hàng CIC nhóm 3 có thể vay nếu có tài sản đảm bảo.",
        "CIC nhóm 1 là nhóm nợ đủ tiêu chuẩn.",
        "Lãi suất vay mua nhà là 8%.",
        "CIC nhóm 3 thuộc nhóm nợ dưới tiêu chuẩn.",
        "Ngân hàng yêu cầu đánh giá tài sản thế chấp."
    ]],

    "ground_truth": [
        "Khách hàng CIC nhóm 3 có thể vay trong một số trường hợp nếu có tài sản đảm bảo."
    ]
}

dataset = Dataset.from_dict(data)

contexts = data["contexts"][0]

relevant = [
    contexts[0],
    contexts[3],
    contexts[4]
]

precision = len(relevant) / len(contexts)

print("Context Precision:", precision)