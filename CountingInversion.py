class CountingInversion:
    def __init__(self):
        self.total_inversions = 0

    def combine(self, left, right):
        i, j = 0, 0
        temp = len(left)
        sorted_result = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_result.append(left[i])
                temp -= 1
                i += 1
            else:
                sorted_result.append(right[j])
                self.total_inversions += temp
                j += 1

        sorted_result += left[i:]
        sorted_result += right[j:]

        print("Conquer")
        print(sorted_result)

        return sorted_result

    def count_inversions(self, arr):
        print("Divide")
        print(arr)
        if len(arr) <= 1:
            return arr

        half_arr = len(arr) // 2

        left = self.count_inversions(arr[:half_arr])
        right = self.count_inversions(arr[half_arr:])

        combined_array = self.combine(left, right)

        return combined_array

def main():
    counting_inversions = CountingInversion()

    n = int(input("Digite o tamanho da sequência: "))
    seq = list(map(int, input("Digite a sequência separada por espaços: ").split()))

    sorted_seq = counting_inversions.count_inversions(seq)
    print("Total de inversões:", counting_inversions.total_inversions)

if __name__ == "__main__":
    main()

# Exemplo:    
# 13
# 2 3 5 7 10 11 1 4 6 8 9 12 13
