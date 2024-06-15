import datetime

birthday_message = "Happy birthday, Rayanne. Panjang umur bro, semooga makin sukses, jangan nakal-nakal sama emak lo, UANG KAS JANGAN LUPA BAYAR!!!! Happy terus pokoknya!"

birthday = datetime.datetime(2007, 6, 17)

today = datetime.datetime.now()
if today.month == birthday.month and today.day == birthday.day:
    print(birthday.message)
else:
    print("Hari ini bukan ultah lo!")
