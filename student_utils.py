# -*- coding: utf-8 -*-



def parse_student(line):
    """把一行 "name,score" 解析成字典；无效记录抛 ValueError。"""
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量应为2，实际 {len(parts)}")
    name, score_str = parts[0].strip(), parts[1].strip()
    if name == "":
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError(f"成绩不是整数: {score_str!r}")
    if not 0 <= score <= 100:
        raise ValueError(f"成绩超出 0-100: {score}")
    return {"name": name, "score": score}
