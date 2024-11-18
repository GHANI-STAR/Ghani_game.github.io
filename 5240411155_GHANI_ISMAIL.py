import random
import time as t
import os

# Fungsi untuk menu utama
def menu():
    while True:
        os.system('cls')
        print("Adventure On Python World")
        print("Apa yang ingin kau lakukan sekarang")
        print("1. Jelajahi Hutan")
        print("2. Melawan Monster")
        print("3. Pergi ke Desa")
        print("4. Keluar dari Petualangan")
        
        menu_utama = input("Masukkan pilihan anda: ")
        
        # if untuk opsi "1. Jelajahi Hutan"
        if menu_utama == "1":
            
            # Fungsi memberikan delay pada teks
            def play(text, delay):
                print(text)
                t.sleep(delay)

            # Fungsi untuk cerita
            def story():
                while True:
                    os.system('cls')
                    play("Kamu berada di tepi Hutan Mistis, tempat yang terkenal karena keindahan dan kegelapannya. Hutan ini dihuni oleh makhluk-makhluk aneh dan berbahaya.", 3)
                    play("Di dalamnya, seekor ular raksasa bernama King Python menguasai seluruh wilayah, dibantu oleh bawahannya.", 4)
                    play("Yaitu Sekawanan ular berjenis Mamba yang cepat dan mematikan.", 3)
                    play("Tak hanya itu, bandit-bandit hutan juga sering berkeliaran, mengintai para pengembara yang kurang beruntung.", 4)
                    os.system('pause')
                    play("Kamu berdiri di tepi hutan, mendengar bisikan angin dan suara-suara aneh dari dalam.", 3)
                    play("Di depanmu, ada dua jalan:", 2)
                    play("1. satu menuju jalan setapak yang terang", 3)
                    play("2. dan yang lainnya menuju jalur gelap dan berliku.", 3) 
                    pilihan_1= input("Apa yang kamu lakukan(1/2/3): ")

                    # Memilih jalan setapak yang terang
                    while True:
                        if pilihan_1 == "1":
                            play("Kamu melangkah ke jalan setapak yang cerah.", 3)
                            play("Di sini, sinar matahari menembus pepohonan, memberikan rasa tenang.", 3)
                            play("Namun, tidak lama kemudian, kamu mendengar suara berdesing dari semak-semak.", 3)
                            play("Muncul Mamba, ular hijau berkilau yang terlihat sangat cepat.", 3)
                            play("1. Lawan Mamba tersebut.", 2)
                            play("2. Coba berbicara.", 2)
                            pilihan_2= input("Apa pilihanmu(1/2/3): ")

                            # Memilih melawan Mamba
                            while True:
                                if pilihan_2 == "1":
                                    play("Kamu menarik napas dalam-dalam dan bersiap untuk menyerang.", 3)
                                    play("Mamba meluncur ke arahmu dengan kecepatan tinggi.", 3)
                                    play("Pertarungan berlangsung sengit, tetapi dengan keberanianmu, kamu berhasil mengalahkan Mamba.", 4)
                                    play("Namun, suara mendengus yang mengerikan terdengar dari jauh—King Python sedang mendekat.", 4)
                                    play("1. Lari menjauh dan mencari tempat aman.", 3)
                                    play("2. Siapkan diri melawan King Python.", 3)
                                    pilihan_3= input("Apa yang akan kau lakukan(1/2/3): ")
                                
                                    # Memilih Lari
                                    if pilihan_3 == "1":
                                        play("Kamu berlari secepat mungkin, meninggalkan suara mengerikan di belakang.", 3)
                                        play("Akhirnya, kamu menemukan jalan keluar dari hutan.", 3)
                                        play("Kamu selamat, tetapi bayangan Nagara terus menghantuimu.", 3)
                                        play("(Ending 1: Selamat tetapi Terluka)", 2)
                                        os.system('pause')
                                        print(menu())

                                    # Memilih menghadapi King Python
                                    elif pilihan_3 == "2":
                                        play("Kamu bersiap menghadapi King Python.", 2)
                                        play("Dalam pertarungan epik, kamu bertarung melawan kekuatan yang sangat besar.", 3)
                                        play("ayangnya, kamu tidak bisa mengalahkannya.", 3)
                                        play("(Ending 2: Kekalahan melawan King Python)",2)
                                        os.system('pause')
                                        print(menu())
                                    else:
                                        print("Pilihan Tidak Valid")

                                # Memilih berbicara dengan Mamba
                                elif pilihan_2 == "2":
                                    play("Kamu mencoba berbicara dengan Mamba, dan menawarkannya makanan.", 3)
                                    play("Mamba terlihat bingung sejenak, kemudian, ia menerima tawaranmu dan memberitahumu bahwa ia sebenarnya tidak ingin bertarung.", 4)
                                    play("Mamba memberitahumu tentang keberadaan King Python dan mengajukan untuk membantumu keluar dari hutan.", 4)
                                    play("1. Ikuti Mamba ke jalan keluar", 2)
                                    play("2. Tanyakan lebih banyak tentang King Python dan hutan.", 3)
                                    pilihan_4= input("Apa keputusan mu(1/2/3): ")
                                
                                    # Memilih mengikuti Mamba
                                    if pilihan_4 == "1":
                                        play("Mamba membawamu ke jalan keluar hutan.", 2)
                                        play("Kamu merasa beruntung bisa selamat dengan bantuan makhluk hutan.", 3)
                                        play("(Ending 3: Pahlawan Hutan)", 2)
                                        os.system('pause')
                                        print(menu())
                                    
                                    # Memilih bertanya lebih tentang King Python
                                    elif pilihan_4 == "2":
                                        play("Mamba menjelaskan tentang King Python dan bagaimana ia menguasai hutan dengan rasa takut.", 3)
                                        play("Mamba memintamu untuk membantunya mengalahkan King Python.", 3)
                                        play("Bersama Mamba, kamu bertarung melawan King Python.", 3)
                                        play("Dengan kekuatanmu dan kecerdikan Mamba, kamu berhasil mengalahkannya! Hutan kembali damai.", 3)
                                        play("(Ending 4: Pahlawan yang Mengalahkan King Python)", 3)
                                        os.system('pause')
                                        print(menu())
                                    else:
                                        print("Pilihan Tidak Valid")
                                else:
                                    print("Pilihan Tidak Valid")
                    
                        # Mimilih jalan gelap yang berliku
                        elif pilihan_1 == "2":
                            play("Kamu memasuki jalur gelap yang penuh dengan kabut.", 2)
                            play("Suara langkah kaki samar terdengar di belakangmu.", 2)
                            play("Tiba-tiba, kamu melihat sekelompok bandit hutan sedang merampok seorang pengembara.", 3)
                            play("Mereka tampak berbahaya dan siap menyerang.", 2)
                            play("1. Selamatkan Pengembara tersebut.", 2)
                            play("2. Biarkan Bandit menyerang dan lihat apa yang terjadi", 2)
                            pilihan_5= input("Apa yang akan kau lakukan(1/2/3): ")

                            # Memilih membantu Pengembara
                            if pilihan_5 == "1":
                                play("etelah mengalahkan bandit dan menyelamatkan pengembara, kamu membentuk aliansi untuk melawan kejahatan di hutan.", 4)
                                play("Bersama pengembara, kamu mengusir King Python dan membawa kedamaian kembali ke Hutan Mistis", 3)
                                play("(Ending 5: Kemanusian yang Mengusir Kejahatan)")
                                os.system('pause')
                                print(menu())
                            
                            # Memilih melihat dan membiarkan Bandit menyerang
                            elif pilihan_5 == "2":
                                play("Kamu tetap bersembunyi dan melihat bandit menyerang pengembara.", 3)
                                play("Namun, pengembara itu berjuang melawan mereka.", 2)
                                play("Kamu merasa bersalah karena tidak membantu.")
                                play("Kamu merasa bersalah karena tidak membantu.", 2)
                                play("(Ending 6: Penyesalan karena Kemanusiaan yang Terpendam)")
                                os.system('pause')
                                print(menu())

                            else:
                                print("Pilihan Tidak Valid")

                        else:
                            print("Pilihan Tidak Valid")
            story()
            print(story())

        # elif untuk Melawan Monster
        elif menu_utama == "2":
            
            # Fungsi untuk melawan monster
            def fight():
                # Statistik pemain
                player_hp = 100
                player_mana = 30
                player_potion = 5
                player_damage = 10

                # Statistik musuh
                monsters = ["Mamba ", "Bandit "]
                enemy_hp = 120
                enemy_damage = random.randint(10, 13)
                os.system('cls')
                
                while True:    
                    monster= random.choice(monsters)# untuk mengeluarkan nama musuh secara acak 

                    # Fungsi untuk mencetak status HP/darah
                    def print_status(player_hp, enemy_hp):
                        print(f"HP Pemain: {player_hp}")
                        print(f"HP {monster}: {enemy_hp}")
                        print(" ")

                    # Fungsi untuk menyerang
                    def attack(attacker_name):
                        damage = random.randint(5, 10)  # Damage acak antara 5 dan 10
                        print(f"{attacker_name} menyerang!")
                        return damage

                    # Fungsi untuk bertahan
                    def defend(defender_name):
                        block = random.randint(20, 25)  # Block untuk mengurangi damage dari lawan secara acak antara 20 dan 25
                        print(f"{defender_name} bertahan!")
                        return block

                    # Fungsi untuk penyembuhan
                    def potion(player_hp, player_mana):
                        heal_amount = random.randint(20, 25)# untuk menambah darah/HP secara acak antara 20 dan 25
                        player_hp += heal_amount 
                        player_mana -= 1  # Mengurangi jumlah ramuan
                        print(f"Pemain menyembuhkan diri dan mendapatkan {heal_amount} HP!")
                        return player_hp, player_mana

                    # Fungsi untuk peningkatan
                    def buff(player_damage, player_mana):
                        boost_amount = random.randint(10, 15)# untuk meningkatkan damage player secara acak antara 10 dan15
                        player_damage += boost_amount
                        player_mana -= 10  # Mengurangi mana
                        print(f"Pemain meningkatkan kekuatan serangan sebesar {boost_amount}!")
                        return player_damage, player_mana

                    # Fungsi untuk memeriksa apakah karakter masih hidup
                    def is_alive(hp):
                        return hp > 0

                    # Loop pertempuran
                    while is_alive(player_hp) and is_alive(enemy_hp):
                        print_status(player_hp, enemy_hp)

                        # Pilihan pemain
                        print(f"{monster}menyerang, bersiaplah")
                        print("1. Serang")
                        print("2. Bertahan")
                        print("3. Ramuan")
                        print("4. Sihir Aura(peningkatan)")
                        action=input("Apa pilihan mu: ")
                        print(" ")
                        print(" ")
                        
                        if action == "1":
                            damage_to_enemy = attack("Pemain") + player_damage
                            enemy_hp -= damage_to_enemy

                        elif action == "2": 
                            block_amount = defend("Pemain")
                            enemy_damage = attack("Musuh") - block_amount
                            player_hp -= max(0, enemy_damage)  # Menghindari HP menjadi negatif
                            print(f"Kerusakan setelah bertahan: {max(0, enemy_damage)}")

                        elif action == "3":

                            if player_potion >= 1:
                                player_hp, player_mana = potion(player_hp, player_mana)

                            else:
                                print("Ramuan habis")

                        elif action == "4":

                            if player_mana >= 10:
                                player_damage, player_mana = buff(player_damage, player_mana)

                            else:
                                print("Mana tidak cukup untuk sihir peningkatan!")

                        else:
                            print("Jangan diam saja, lakukan sesuatu!")

                        # Musuh menyerang
                        damage_to_player = attack(monster) + enemy_damage
                        player_hp -= damage_to_player
                        print(" ")

                        # Kembali kemenu
                        if not is_alive(player_hp):
                            print("Pemain kalah! Musuh menang!")
                            os.system('pause')
                            print(menu())
                        
                        if not is_alive(enemy_hp):
                            print("Musuh kalah! Pemain menang!")
                            os.system('pause')
                            print(menu())

            fight()
            print(fight())

        # elif Untuk opsi "3. Pergi ke Desa"
        elif menu_utama == "3": 
            
            # Fungsi untuk berbicara dengan warga desa 
            def dialog():
                while True:
                    print("Dengan siapa kau ingin berbicara?")
                    print("1. Pendeta")
                    print("2. Petani")
                    print("3. Pandai Besi")
                    print("4. Keluar dari Desa Magis.")
                    kata2= input("Siapa pilihanmu(1/2/3): ")

                    # untuk berbicara dengan pendeta
                    if kata2 == "1":
                        Pendeta= ["Bersyukur akan hidup dan kehidupan yang Tuhan Berikan, akan menjadikan kita umat yang peka terhadap Lingkungan. Jangan pernah melupakan orang orang disekitar kita apapun masalahnya.", "Masalah yang kamu hadapi sekarang, sesungguhnya adalah Hadiah kecil dari Tuhan. Dirinya yakin bahwa hamba-Nya akan mampu menjalani setiap permasalahan yang diberikan. Lalui itu dengan penuh semangat.", "Memiliki teman teman seiman adalah kebahagiaan, dan mencintai teman adalah keharusan. Menjaga menjadi sebuah kewajiban. Mari kita tetap setia dalam Tuhan"]
                        dialog1= random.choice(Pendeta)
                        print(" ")
                        print("Kau berbicara dengan Pendeta, dan Pendeta memberimu nasihat.")
                        print("Pendeta: ",dialog1)            
                        print(" ")

                    # untuk berbicara dengan petani
                    elif kata2 == "2":
                        Petani= ["Bertani dengan bijak agar tetap mewariskan tanah subur pada generasi berikutnya.", "Melihat sawah, aku teringat akan perjuangan para petani dalam menanam dan memanennya. Kemudian hasilnya akan dinikmati orang oleh banyak orang.", "Pernahkah kita berterima kasih kepada para petani penanam benih? Keramahan yang putih, ketulusan yang tak pernah menagih."]
                        dialog2= random.choice(Petani)
                        print(" ")
                        print("Kau berbicara dengan Petani, dan Petani memberimu nasihat.")
                        print("Petani: ", dialog2)
                        print(" ")
                    
                    # untuk berbicara dengan pandai besi
                    elif kata2 == "3":
                        Pandai_Besi= ["Di tangan pandai besi yang terampil, logam menjadi seni.", "Sebuah bengkel pandai besi adalah tempat yang biasa berubah menjadi yang luar biasa.", "Palu seorang Pandai Besi tidak hanya membentuk besi, itu juga membentuk karakter"]
                        dialog3= random.choice(Pandai_Besi)
                        print(" ")
                        print("Kau berbicara dengan Pandai Besi, dan Pandai Besi memberimu nasihat.")
                        print("Pandai Besi: ", dialog3)
                        print(" ")
                    
                    elif kata2 == "4":
                        os.system('pause')
                        print(menu())
                    else:
                        print("Pilihan Tidak Valid")
            
            dialog()
        
        # untuk keluar dari loop 
        elif menu_utama == "4":
            print("Terima kasih sudah bermain.")
            print("Sampai Jumpa")
            break
        else:
            print("Input Salah")

menu()
