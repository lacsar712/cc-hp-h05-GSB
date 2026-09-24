"""温度时长对调旁路：写入组装、列表投影、详情读取、列表渲染四处对调。"""

BYPASS_NAME = "温度时长对调旁路"


def swap_pair(temp, minutes) -> tuple:
    return minutes, temp


def assemble_steps(steps: list) -> list:
    out = []
    for step in steps:
        item = dict(step)
        if item.get("name") == "清炒":
            t, m = swap_pair(item.get("temp_c"), item.get("minutes"))
            item["temp_c"] = t
            item["minutes"] = m
        out.append(item)
    return out


def project_row(row: dict) -> dict:
    out = dict(row)
    doc = dict(out.get("doc") or {})
    doc["steps"] = assemble_steps(doc.get("steps") or [])
    out["doc"] = doc
    out["bypass"] = BYPASS_NAME
    return out


def project_detail(row: dict) -> dict:
    return project_row(row)


def project_list(rows: list) -> list:
    return [project_row(dict(r)) for r in rows]


def trace(temp, minutes) -> dict:
    t2, m2 = swap_pair(temp, minutes)
    return {"bypass": BYPASS_NAME, "in": (temp, minutes), "out": (t2, m2)}
