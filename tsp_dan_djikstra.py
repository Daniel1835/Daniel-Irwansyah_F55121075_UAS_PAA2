import tkinter as tk
import time

# Fungsi untuk menghitung shortest path menggunakan algoritma TSP
def tsp_algorithm(graph, start_vertex):
    num_vertices = len(graph)
    vertex_set = set(range(num_vertices))
    memo = {}

    # Rekursif dengan memoization
    def tsp_helper(curr_vertex, vertex_set):
        # Base case
        if len(vertex_set) == 1:
            return graph[curr_vertex][start_vertex]

        # Mengecek memoization
        memo_key = (curr_vertex, tuple(vertex_set))
        if memo_key in memo:
            return memo[memo_key]

        min_distance = float('inf')
        for next_vertex in vertex_set:
            if next_vertex == start_vertex or next_vertex == curr_vertex:
                continue
            distance = graph[curr_vertex][next_vertex] + tsp_helper(next_vertex, vertex_set - {next_vertex})
            min_distance = min(min_distance, distance)

        # Menyimpan hasil ke dalam memo
        memo[memo_key] = min_distance
        return min_distance

    # Panggil fungsi rekursif
    shortest_path = tsp_helper(start_vertex, vertex_set)
    return shortest_path

# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra_algorithm(graph, start_vertex):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start_vertex] = 0
    visited = [False] * num_vertices

    # Proses iteratif untuk mencari shortest path
    for _ in range(num_vertices):
        min_dist = float('inf')
        min_vertex = -1

        # Mencari vertex dengan jarak terpendek
        for v in range(num_vertices):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v

        visited[min_vertex] = True

        # Update jarak terpendek untuk tetangga yang belum dikunjungi
        for v in range(num_vertices):
            if not visited[v] and graph[min_vertex][v] > 0:
                new_dist = dist[min_vertex] + graph[min_vertex][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    shortest_path = dist
    return shortest_path

# Fungsi untuk mengupdate hasil pada GUI
def update_result(result_text, result):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Fungsi untuk menjalankan algoritma TSP
def run_tsp(graph, result_text):
    start_time = time.time()
    shortest_path = tsp_algorithm(graph, 0)
    end_time = time.time()

    result = f"Jalur terpendek: {shortest_path}\n"
    result += f"Waktu komputasi: {end_time - start_time} detik"

    update_result(result_text, result)

import tkinter as tk
import time

# Fungsi untuk menghitung shortest path menggunakan algoritma Dijkstra
def dijkstra_algorithm(graph, start_vertex):
    num_vertices = len(graph)
    dist = [float('inf')] * num_vertices
    dist[start_vertex] = 0
    visited = [False] * num_vertices

    # Proses iteratif untuk mencari shortest path
    for _ in range(num_vertices):
        min_dist = float('inf')
        min_vertex = -1

        # Mencari vertex dengan jarak terpendek
        for v in range(num_vertices):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v

        visited[min_vertex] = True

        # Update jarak terpendek untuk tetangga yang belum dikunjungi
        for v in range(num_vertices):
            if not visited[v] and graph[min_vertex][v] > 0:
                new_dist = dist[min_vertex] + graph[min_vertex][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist

    shortest_path = dist
    return shortest_path

# Fungsi untuk mengupdate hasil pada GUI
def update_result(result_text, result):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, result)

# Fungsi untuk menjalankan algoritma Dijkstra
def run_dijkstra(graph, start_vertex, result_text):
    start_time = time.time()
    shortest_path = dijkstra_algorithm(graph, start_vertex)
    end_time = time.time()

    result = "Jarak terpendek dari vertex awal:\n"
    for i in range(len(shortest_path)):
        result += f"Vertex {i}: {shortest_path[i]}\n"
    result += f"Waktu komputasi: {end_time - start_time:.6f} detik"

    update_result(result_text, result)

# Fungsi untuk membuat GUI
def create_gui():
    root = tk.Tk()
    root.title("Perhitungan TSP dan Djikstra ")
    root.geometry("400x400")

    # Frame utama
    main_frame = tk.Frame(root, bd=2)
    main_frame.pack(expand=True, padx=20, pady=20)

    # Label judul
    title_label = tk.Label(main_frame, text="Program Perhitungan Shortest Path", font=("Helvetica", 14))
    title_label.pack(pady=10)

    # Label pilihan
    choice_label = tk.Label(main_frame, text="Pilihan:", font=("Helvetica", 12))
    choice_label.pack()

    # Frame hasil
    result_frame = tk.Frame(main_frame, bd=2, relief=tk.SUNKEN)
    result_frame.pack(expand=True, padx=20, pady=20)

    # Textbox hasil
    result_text = tk.Text(result_frame, height=20, width=50)
    result_text.pack()

    # Graph
    graph = [
        [0, 12, 10, 0, 0, 0, 12],
        [12, 0, 0, 12, 0, 0, 0],
        [10, 0, 0, 11, 3, 0, 9],
        [0, 12, 11, 0, 11, 10, 0],
        [0, 0, 3, 11, 0, 6, 7],
        [0, 0, 0, 10, 6, 0, 9],
        [12, 0, 9, 0, 7, 9, 0]
    ]

    # Fungsi untuk menjalankan pilihan
    def run_choice(choice):
        if choice == 1:
            run_tsp(graph, result_text)
        elif choice == 2:
            run_dijkstra(graph, 0, result_text)

    # Button TSP
    tsp_button = tk.Button(main_frame, text="Travelling Salesman Problem (TSP)", command=lambda: run_choice(1))
    tsp_button.pack(pady=5)

    # Button Dijkstra
    dijkstra_button = tk.Button(main_frame, text="Dijkstra", command=lambda: run_choice(2))
    dijkstra_button.pack(pady=5)

    # Button Keluar
    exit_button = tk.Button(main_frame, text="Keluar", command=root.destroy)
    exit_button.pack(pady=10)

    # Button NAMA_NIM
    exit_button = tk.Button(main_frame, text="DANIEL IRWANSYAH_F55121075", command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()

# Fungsi utama
def main():
    create_gui()

if __name__ == '__main__':
    main()
