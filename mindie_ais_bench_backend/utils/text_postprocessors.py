from ais_bench.benchmark.registry import TEXT_POSTPROCESSORS
from ais_bench.benchmark.utils.text_postprocessors import first_capital_postprocess

@TEXT_POSTPROCESSORS.register_module('bool_q_postprocess')
def bool_q_postprocess(pred: str):
    processed_pred = first_capital_postprocess(pred)
    if processed_pred in ["A", "B"]:
        return processed_pred
    import re
    pattern = r'\b(Yes|No)\b'
    match = re.search(pattern, pred)
    
    # 如果匹配成功，返回匹配到的字符串；否则返回None
    if match:
        return match.group(1)
    else:
        return "Answer Not Found"
