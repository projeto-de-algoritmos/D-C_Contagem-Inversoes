typedef int Item;

#define key(A) (A) //key(A) (A.chave)
#define less(A,B) (key(A) < key(B))
#define lesseq(A,B) (key(A) <= key(B))
#define exch(A,B) {Item t = A; A = B; B = t;}
#define cmpexch(A,B) {if(less(A,B)) exch(A,B);}  

void combine(int *V, int l, int middle, int r)
{
    int *VAux = (int *)malloc((r-l+1) * sizeof(int)); 
    int k = 0, i = l, j = middle+1;
    while ((i <= middle) && (j <= r)){
        if (lesseq(V[i], V[j])){
            VAux[k++] = V[i++];
        }
        else{
            VAux[k++] = V[j++];
        }
    }
    while (i <= middle){
        VAux[k++] = V[i++];
    }
    while (j<=r){
        VAux[k++] = V[j++];        
    }
    k = 0;
    while((l + k) <= r){
        V[l + k] = VAux[k];
        k++;
    }
    free(VAux); //Free nao funciona em arrays de uma posição
}

int count_inversions(int *V, int l, int r)
{
    if (l >= r)
        return 0;

    int middle = (r + l) / 2;
    
    int res = count_inversions(V, l, middle) + count_inversions(V, middle + 1, r);
    for (int i = l, j = middle + 1; i <= middle; i ++) {
        while (j <= r && (double)V[i] / 2.0 > V[j]) {
            j ++;
        }
        res += j - middle - 1;
    }

    combine(V, l, middle, r);
    return res; 
}

int reversePairs(int* V, int VSize) {
    return count_inversions(V , 0 , VSize-1); 
}

