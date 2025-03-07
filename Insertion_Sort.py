import time

def read_file(file_path):
    """อ่านข้อมูลจากไฟล์และส่งกลับเป็นลิสต์ของบรรทัด"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()

def print_sorted_lines(sorted_list):
    """แสดงผลลัพธ์ที่จัดเรียงแล้ว"""
    for line in sorted_list:
        print(line.strip())

def bubble_sort(arr):
    """ฟังก์ชันสำหรับการจัดเรียงแบบ Bubble Sort"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # เปรียบเทียบและสลับถ้าจำเป็น
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # ถ้าไม่มีการสลับ แสดงว่าจัดเรียงเสร็จแล้ว
            break
    return arr

# เริ่มต้นการจับเวลา
start = time.time()

# อ่านข้อมูลจากไฟล์
lines = read_file("province.txt")

# จัดเรียงข้อมูล
sorted_lines = bubble_sort(lines)

# จบการจับเวลา
end = time.time()
time = end - start

# แสดงผลลัพธ์ที่จัดเรียงแล้ว
print_sorted_lines(sorted_lines)

# แสดงเวลาที่ใช้ในการจัดเรียง
print(f"{time:.6f} / S")