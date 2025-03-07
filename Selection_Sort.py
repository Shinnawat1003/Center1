import time

# เริ่มต้นการจับเวลา
start = time.time()

# เปิดไฟล์และอ่านข้อมูล
with open("community_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

def selection_sort(data):
    length = len(data)

    for i in range(length - 1):
        min_index = i

        for j in range(i + 1, length):
            if data[j] > data[min_index]:
                min_index = j

        # สลับตำแหน่ง
        data[i], data[min_index] = data[min_index], data[i]

    return data

# เรียงลำดับข้อมูล
sorted_lines = selection_sort(lines)

# จบการจับเวลา
end = time.time()
time = end - start

# แสดงข้อมูลที่เรียงลำดับแล้ว
for line in sorted_lines:
    print(line.strip())  # ลบ \n ออกเมื่อแสดงผล

# แสดงเวลาที่ใช้ในการประมวลผล
print(f" {time:.2f} / S ")