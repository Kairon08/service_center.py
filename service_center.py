import datetime

def main():
    queue = [] # Mijozlar ro'yxati
    print("--- Servis Markazi Navbat Tizimi ---")

    while True:
        print("\n1. Yangi mijoz qo'shish")
        print("2. Navbatni ko'rish")
        print("3. Mijozni qabul qilish (Navbatdan o'chirish)")
        print("4. Chiqish")
        
        choice = input("\nTanlang (1-4): ")

        if choice == '1':
            name = input("Mijoz ismi: ")
            device = input("Qurilma modeli (masalan, iPhone 13): ")
            problem = input("Muammo nima: ")
            time = datetime.datetime.now().strftime("%H:%M")
            
            # Mijoz ma'lumotlarini lug'at (dictionary) shaklida saqlaymiz
            customer = {
                "ism": name,
                "model": device,
                "muammo": problem,
                "vaqt": time
            }
            queue.append(customer)
            print(f"\n✅ {name} navbatga qo'shildi!")

        elif choice == '2':
            print("\n--- Hozirgi Navbat ---")
            if not queue:
                print("Navbat bo'sh.")
            else:
                for i, c in enumerate(queue, 1):
                    print(f"{i}. {c['ism']} | {c['model']} | {c['vaqt']}")

        elif choice == '3':
            if not queue:
                print("\nNavbatda hech kim yo'q.")
            else:
                served = queue.pop(0) # Birinchi turgan mijozni oladi
                print(f"\n🛠 Hozirgi mijoz: {served['ism']} ({served['model']})")
                print(f"Muammo: {served['muammo']}")
                print("Ushbu mijoz navbatdan chiqarildi.")

        elif choice == '4':
            print("Dastur tugatildi. Xayr!")
            break
        else:
            print("Noto'g'ri buyruq!")

if __name__ == "__main__":
    main()
    
