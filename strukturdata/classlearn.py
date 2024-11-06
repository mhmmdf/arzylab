class BankAccount:
    def __init__(self, owner, gender, balance=0):
        if gender == 'L':
            self.gender = "Laki-laki"
        else:
            self.gender = "Perempuan"
        self.owner = owner
        self.balance = int(balance)

        print(f"Berhasil menambahkan pengguna! \r\nNama Lengkap: {self.owner}\r\nJenis Kelamin: {self.gender}\r\nSaldo Akun: Rp{self.balance}")
    
    def deposit(self, amount):
        if amount > 10000:
            self.balance += amount
            print(f"Berhasil menambahkan deposit sejumlah Rp{amount}. Anda memiliki saldo sebesar Rp{self.balance}")
        else:
            print("Minimal top up sejumlah Rp10.000")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Saldo Anda tidak mencukupi untuk melakukan penarikan ini!")
        elif amount < 50000:
            print("Minimal penarikan Rp 50.000!")
        else:
            self.balance -= amount
            print(f"Penarikan senilai Rp{amount} berhasil!. Saldo Anda saat ini tersisa Rp{self.balance}")


fullname = input("Masukkan nama lengkap Anda: ")
gender = input("Pilih jenis kelamin: L/P ")
nominal = input("Masukan nominal uang yang akan disetor: Rp ")
account = BankAccount(fullname, gender, nominal)

while True:
    action = input(f"Hei {fullname}! Silahkan Pilih Menu Transaksi (deposit/withdraw/exit): ")

    if action == "deposit":
        amount = int(input("Masukan nominal uang yang akan disetor: Rp "))
        account.deposit(amount)
    elif action == "withdraw":
        amount = int(input("Masukan nominal penarikan: Rp "))
        account.withdraw(amount)
    elif action == "exit":
        print("Keluar aplikasi...")
        break
    else:
        print("Menu tidak tersedia pada aplikasi!")