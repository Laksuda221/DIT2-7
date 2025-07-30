def sort_five_numbers():
    nums = []
    print("กรุณาใส่จำนวนเต็ม 5 จำนวน:")
    for i in range(5):
        while True:
            try:
                n = int(input(f"ตัวที่ {i+1}: "))
                nums.append(n)
                break
            except ValueError:
                print("กรุณาใส่จำนวนเต็มเท่านั้น!")
    nums.sort()
    print("เรียงจากน้อยไปมาก:", nums)

if __name__ == "__main__":
    sort_five_numbers()