# 1. append(x)
my_list = [1, 2, 3]
my_list.append(4)
print("append:", my_list)  

# 2. extend(iterable)
my_list.extend([5, 6])
print("extend:", my_list)  

# 3. insert(i, x)
my_list.insert(2, 10)  # Sisipkan 10 di indeks 2
print("insert:", my_list)  

# 4. remove(x)
my_list.remove(10)  # Hapus elemen pertama yang bernilai 10
print("remove:", my_list)  #

# 5. pop([i])
last_element = my_list.pop()  # Menghapus elemen terakhir
print("pop (last element):", last_element)  
print("pop (after removing last):", my_list)  

# Menggunakan pop dengan indeks tertentu
third_element = my_list.pop(2)  # Menghapus elemen di indeks 2
print("pop (third element):", third_element)  
print("pop (after removing third):", my_list)  

# 6. clear()
my_list.clear()
print("clear:", my_list)  

# Membuat ulang list untuk contoh selanjutnya
my_list = [1, 2, 3, 2]

# 7. index(x[, start[, end]])
index_of_2 = my_list.index(2)  # Mencari indeks elemen pertama bernilai 2
print("index of 2:", index_of_2)  

# 8. count(x)
count_of_2 = my_list.count(2)  # Menghitung jumlah kemunculan angka 2
print("count of 2:", count_of_2)  

# 9. sort(*, key=None, reverse=False)
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort()  # Mengurutkan secara menaik
print("sort (ascending):", my_list)  
my_list.sort(reverse=True)  # Mengurutkan secara menurun
print("sort (descending):", my_list)  

# 10. reverse()
my_list.reverse()  # Membalik urutan elemen
print("reverse:", my_list)  

# 11. copy()
my_list_copy = my_list.copy()  # Membuat salinan dangkal dari list
print("copy:", my_list_copy)  