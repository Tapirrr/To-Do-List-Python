todo_list = []
next_id = 1


def main():
    while True:
        print("=== Aplikasi Todo List ===")
        print("1. Tambah Task")
        print("2. Lihat Task")
        print("3. Ubah Task")
        print("4. Hapus Task")
        print("5. Keluar")
        print("==========================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_task()
        elif pilihan == "2":
            munculkan_task()
        elif pilihan == "3":
            edit_task()
        elif pilihan == "4":
            hapus_task()
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            return
        else:
            print("Pilihan tidak valid, coba lagi.\n")


def tambah_task():
    global next_id
    judul = input("Masukkan nama task baru: ").strip()
    if not judul:
        print("Task tidak boleh kosong!\n")
        return
    todo_list.append({"id": next_id, "judul": judul})
    next_id += 1
    print("Task berhasil ditambahkan!\n")


def munculkan_task():
    if not todo_list:
        print("Belum ada task.\n")
        return
    print("Daftar Task:")
    for task in todo_list:
        print(f"{task['id']}. {task['judul']}")
    print()


def edit_task():
    munculkan_task()
    if not todo_list:
        return
    try:
        task_id = int(input("Masukkan ID task yang ingin diubah: "))
    except ValueError:
        print("ID tidak valid!\n")
        return

    task = next((t for t in todo_list if t["id"] == task_id), None)
    if not task:
        print("Task tidak ditemukan!\n")
        return

    judul_baru = input("Masukkan judul baru: ").strip()
    if not judul_baru:
        print("Task tidak boleh kosong!\n")
        return

    task["judul"] = judul_baru
    print("Task berhasil diubah!\n")


def hapus_task():
    munculkan_task()
    if not todo_list:
        return
    try:
        task_id = int(input("Masukkan ID task yang ingin dihapus: "))
    except ValueError:
        print("ID tidak valid!\n")
        return

    index = next((i for i, t in enumerate(todo_list) if t["id"] == task_id), -1)
    if index == -1:
        print("Task tidak ditemukan!\n")
        return

    todo_list.pop(index)
    print("Task berhasil dihapus!\n")


main()