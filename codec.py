def find_name_by_code(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    code, name = parts
                    if code == n:
                        return name
        return "ไม่พบข้อมูลในไฟล์"
    except FileNotFoundError:
        return "ไม่พบไฟล์ที่กำหนด"
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {e}"

file_path = "countries.txt"
n = "12345"
result = find_name_by_code(file_path, n)
print(f"ผลลัพธ์: {result}")