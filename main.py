import json
from pathlib import Path

KB_FILE = Path(__file__).with_name("kb_wifi.json")
with KB_FILE.open("r", encoding="utf-8") as file:
    KB = json.load(file)
ATURAN = KB["aturan"]

# FORWARD CHAINING
def forward_chaining(fakta_awal):
    """ Forward chaining: fakta awal -> cocokkan aturan -> fakta baru -> ulangi sampai tidak ada aturan baru. """
    # Memori kerja
    memori = list(fakta_awal)
    # Menyimpan asal setiap fakta
    # None berarti fakta berasal langsung dari user
    asal = {fakta: None for fakta in fakta_awal}
    siklus = 0
    while True:
        siklus += 1
        # Mencari aturan yang cocok
        konflik = []

        for aturan in ATURAN:
            # Jika mode AND
            if aturan["mode"] == "dan":
                terpenuhi = all(fakta in memori for fakta in aturan["jika"])

            # Jika mode OR
            elif aturan["mode"] == "atau":
                terpenuhi = any(fakta in memori for fakta in aturan["jika"])

            else:
                terpenuhi = False

            # Aturan hanya masuk konflik jika:
            # syaratnya terpenuhi
            # hasilnya belum ada di memori
            if (terpenuhi and aturan["maka"] not in memori):
                konflik.append(aturan)

        # Kriteria berhenti
        if not konflik:
            print(f"Siklus {siklus}: "  "himpunan konflik kosong -> berhenti")
            break

        # Conflict resolution
        aturan = konflik[0]
        print(
            f"Siklus {siklus}: " f"konflik = {[r['id'] for r in konflik]} " f"-> jalankan {aturan['id']}")

        # Eksekusi aturan
        fakta_baru = aturan["maka"]
        memori.append(fakta_baru)

        # Catat dari aturan mana fakta berasal
        asal[fakta_baru] = (aturan["id"], aturan["jika"])
    return memori, asal

# BAGIAN PENJELASAN
def jelaskan(fakta, asal, tingkat=0):
    """Menjelaskan bagaimana sebuah fakta diperoleh sampai kembali ke fakta user."""
    indent = "  " * tingkat

    # Jika fakta berasal langsung dari user
    if asal[fakta] is None:
        print(f"{indent}{format_fakta(fakta)}: " "fakta dari user")
        return
    id_aturan, premis = asal[fakta]

    print(
        f"{indent}{format_fakta(fakta)}, "
        f"karena {id_aturan}: " 
        f"{' AND '.join(format_fakta(p) for p in premis)}")

    # Telusuri premis yang merupakan fakta hasil aturan lain
    for premis in premis:
        if premis in asal:
            jelaskan(premis, asal, tingkat + 1)

# FORMAT FAKTA
def format_fakta(fakta):
    return fakta.replace("_", " ")

def tanya_user():
    fakta_awal = []
    print("\nJawab dengan y = ya, t = tidak.\n")

    for nomor, pertanyaan in enumerate(KB["pertanyaan"], start=1):
        while True:
            jawaban = input(f"{nomor}. {pertanyaan['teks']} (y/t): ").strip().lower()
            if jawaban in ("y", "t"):
                break
            print("Input tidak valid. Masukkan y atau t.")
        if jawaban == "y":
            fakta_awal.append(pertanyaan["fakta"])
    return fakta_awal

def main():
    print("=" * 60)
    print(KB["judul"])
    print("=" * 60)
    print("\nMetode: Forward Chaining")
    print("Basis pengetahuan: kb_wifi.json")

    fakta_awal = tanya_user()
    print("\n" + "-" * 60)
    print("FAKTA AWAL")
    print("-" * 60)

    if fakta_awal:
        for fakta in fakta_awal:
            print("- " + format_fakta(fakta))
    else:
        print("- Tidak ada fakta yang dipilih.")

    # Forward chaining
    memori, asal = forward_chaining(fakta_awal)
    # Kesimpulan
    kesimpulan = []

    for fakta in memori:
        # Kesimpulan adalah fakta yang dihasilkan oleh aturan
        if fakta in asal and asal[fakta] is not None:
            kesimpulan.append(fakta)

    print("\n" + "-" * 60)
    print("HASIL")
    print("-" * 60)

    if kesimpulan:
        print("Kesimpulan:")
        for fakta in kesimpulan:
            print("- " + format_fakta(fakta))

        print("\nAlasan:")
        jelaskan(kesimpulan[-1],asal)
    else:
        print("Tidak ditemukan kesimpulan berdasarkan fakta yang diberikan dan aturan yang tersedia.")

    # Batas keberlakuan
    print("\n" + "-" * 60)
    print("BATAS KEBERLAKUAN")
    print("-" * 60)
    print(KB["batas"])
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()