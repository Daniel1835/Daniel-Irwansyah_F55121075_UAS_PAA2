****UAS PAA****

***Daniel Irwansyah_F55121075***

**Hasil analysis algorithm**

**bubble sort and insertion sort**

***a. Worst case:***
-Bubble Sort: Pada worst case, Bubble Sort memiliki kompleksitas waktu O(n^2), dimana n adalah jumlah elemen dalam array yang diurutkan. Pada kode ini, jika array memiliki ukuran n, maka Bubble Sort akan melakukan n-1 iterasi pada outer loop dan (n-1-i) iterasi pada inner loop, sehingga total iterasi adalah (n-1) + (n-2) + ... + 2 + 1 = (n-1)n/2. Dalam kasus terburuk, ketika array terurut secara terbalik, Bubble Sort akan melakukan penukaran elemen pada setiap iterasi inner loop, sehingga waktu komputasi mencapai O(n^2).
-Insertion Sort: Pada worst case, Insertion Sort juga memiliki kompleksitas waktu O(n^2). Pada kode ini, jika array memiliki ukuran n, maka Insertion Sort akan melakukan n-1 iterasi pada outer loop dan dalam setiap iterasi, melakukan pergeseran elemen pada inner loop hingga menemukan posisi yang tepat untuk elemen yang sedang diperiksa. Jika array terurut secara terbalik, maka setiap iterasi inner loop akan memindahkan elemen sebanyak j posisi, dimana j adalah indeks saat ini dalam outer loop. Sehingga waktu komputasi Insertion Sort pada worst case mencapai O(n^2).

***b. Best case:***
-Bubble Sort: Pada best case, Bubble Sort memiliki kompleksitas waktu O(n), dimana n adalah jumlah elemen dalam array yang diurutkan. Pada kode ini, jika array sudah terurut secara ascending, maka Bubble Sort hanya akan melakukan 1 iterasi pada outer loop dan tidak ada penukaran yang terjadi pada inner loop. Sehingga waktu komputasi Bubble Sort pada best case adalah O(n).
-Insertion Sort: Pada best case, Insertion Sort memiliki kompleksitas waktu O(n), dimana n adalah jumlah elemen dalam array yang diurutkan. Pada kode ini, jika array sudah terurut secara ascending, maka Insertion Sort hanya akan melakukan 1 iterasi pada outer loop dan tidak ada pergeseran elemen yang terjadi pada inner loop. Sehingga waktu komputasi Insertion Sort pada best case adalah O(n).

***c. Average case:***
-Bubble Sort: Pada average case, Bubble Sort memiliki kompleksitas waktu O(n^2), dimana n adalah jumlah elemen dalam array yang diurutkan. Pada kode ini, jika array memiliki ukuran n, Bubble Sort akan melakukan rata-rata (n-1)n/4 penukaran elemen. Jumlah penukaran ini dapat diperoleh dengan menjumlahkan kemungkinan penukaran dalam setiap iterasi inner loop dan kemudian membaginya dengan jumlah iterasi inner loop. Sehingga waktu komputasi Bubble Sort pada average case mencapai O(n^2).
-Insertion Sort: Pada average case, Insertion Sort memiliki kompleksitas waktu O(n^2), dimana n adalah jumlah elemen dalam array yang diurutkan. Pada kode ini, jika array memiliki ukuran n, Insertion Sort akan melakukan rata-rata (n^2 - n)/4 pergeseran elemen. Jumlah pergeseran ini dapat diperoleh dengan menjumlahkan kemungkinan pergeseran dalam setiap iterasi inner loop dan kemudian membaginya dengan jumlah iterasi inner loop. Sehingga waktu komputasi Insertion Sort pada average case mencapai O(n^2).

**TSP dan Djikstra**

***a. Worst Case:***
-Algoritma TSP: Pada kasus terburuk, kompleksitas waktu algoritma ini adalah O(n!), di mana n adalah jumlah vertex dalam grafik. Karena algoritma TSP menggunakan pendekatan brute force dengan pemanggilan rekursif, kompleksitas waktu eksponensial ini dapat sangat mempengaruhi kinerja algoritma ketika jumlah vertex meningkat.
-Algoritma Dijkstra: Pada kasus terburuk, kompleksitas waktu algoritma ini adalah O((V + E) log V), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam grafik. Hal ini terjadi ketika semua vertex harus dikunjungi dan setiap edge harus dipertimbangkan dalam pencarian jalur terpendek.

***b. Best Case:***
-Algoritma TSP: Pada kasus terbaik, kompleksitas waktu algoritma ini masih O(n!), karena algoritma TSP selalu harus mempertimbangkan semua kemungkinan permutasi untuk mencari jalur terpendek.
-Algoritma Dijkstra: Pada kasus terbaik, kompleksitas waktu algoritma ini adalah O(V + E), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam grafik. Hal ini terjadi ketika ada vertex yang memiliki jarak langsung yang lebih pendek ke vertex tujuan daripada melalui vertex lain.

***c. Average Case:***
-Algoritma TSP: Rata-rata kompleksitas waktu algoritma ini sulit ditentukan secara pasti karena tergantung pada struktur grafik dan bobotnya. Namun, secara umum, kompleksitas waktu algoritma TSP adalah O(n!) dalam kasus rata-rata.
-Algoritma Dijkstra: Rata-rata kompleksitas waktu algoritma ini adalah O((V + E) log V), di mana V adalah jumlah vertex dan E adalah jumlah edge dalam grafik. Algoritma Dijkstra cenderung memberikan kinerja yang baik dalam kasus rata-rata, terutama pada grafik dengan edge yang jarang dan tidak ada sirkuit negatif.
