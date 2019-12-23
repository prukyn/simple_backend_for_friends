from datetime import date

def transform_to_json(headers: list, query_result: list):
    result = []
    for item in query_result:
        res = {}
        for header, val in zip(headers, item):
            if isinstance(val, date):
                val = f"{val.day}-{val.month}-{val.year}"
            res[header] = val
        result.append(res)

    return result
