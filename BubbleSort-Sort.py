import time

start = time.time()

with open("province.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    
# ฟังก์ชันสำหรับการจัดเรียงแบบ Bubble Sort
def bubble_sort(data):
    length = len(data)
    for passnum in range(length - 1):
        swapped = False
        for i in range(length - 1 - passnum):
            if data[i] < data[i + 1]:  # เปรียบเทียบและสลับถ้าจำเป็น
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        if not swapped:  # ถ้าไม่มีการสลับ แสดงว่าจัดเรียงเสร็จแล้ว
            break
    return data

sorted_lines = bubble_sort(lines)

end = time.time()
time_use = end - start

for line in sorted_lines :
    print(line.strip()) 

print(f"{time_use} / S")
