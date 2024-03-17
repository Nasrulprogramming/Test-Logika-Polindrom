def cek_palindrom(kata):
  """
  Fungsi untuk mengecek apakah suatu kata adalah palindrom.

  Args:
    kata: Kata yang ingin diperiksa.

  Returns:
    True jika kata adalah palindrom, False jika bukan.
  """

  panjang_kata = len(kata)
  if panjang_kata == 0 or panjang_kata == 1:
    return True

  for i in range(panjang_kata):
    if kata[i] != kata[panjang_kata - i - 1]:
      return False

  return True

kata = input("Masukkan kata: ")
if cek_palindrom(kata):
  print(f"Kata '{kata}' adalah palindrom.")
else:
  print(f"Kata '{kata}' bukan palindrom.")
