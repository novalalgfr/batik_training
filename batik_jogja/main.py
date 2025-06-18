import os

# Ganti ini ke folder tempat file kamu
folder_path = 'batik_truntum'

# Nama dasar file
base_name = 'batik_truntum'

# List semua file dalam folder
files = os.listdir(folder_path)

# Sort file asal saja
files.sort()

# Loop dan rename
for idx, filename in enumerate(files, start=1):
    # Ambil ekstensi file
    ext = os.path.splitext(filename)[1]
    
    # Buat nama baru dengan format batik_truntum_0001.png
    new_name = f"{base_name}_{idx:04d}{ext}"
    
    # Path lama dan baru
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename file
    os.rename(old_path, new_path)

print("Semua file berhasil di-rename!")
