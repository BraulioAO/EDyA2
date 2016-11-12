#include <stdio.h>
#include <stdlib.h>

typedef struct nodo nodo;

struct nodo{
  int key;
  nodo *next;
};

nodo *head = NULL;
nodo *tail = NULL;

nodo* crear(int e){
  nodo *nuevo =  malloc(sizeof(nodo));
  //(*nuevo).key = e;
  nuevo->key = e;
  return nuevo;
}

void enq(int v){
  nodo *nodo = crear(v);

  if(head==NULL){
    head = nodo;
    tail = nodo;
  }
  else{
    tail->next = nodo;
    tail = tail->next;
    //tail = nodo;
  }
}

int deq(){
  if(head != NULL){
    nodo *tmp = head;
    head = head->next;
    if(head == NULL)
      tail = NULL;

    return tmp->key;
  }
  else
    return -1;
}

void imprimir_cola(){
  nodo *aux = head;
  printf("Contenido de la cola { ");
  while (aux != NULL) {
    printf("%i , ",aux->key );
    aux = aux->next;
  }
  printf("}");
}

int main() {
  #pragma omp parallel num_threads(5)
  {
      int id = omp_get_thread_num();
      int i;
      for ( i = 0; i < id; i++) {
            #pragma omp critical
            {

                enq(id);
            }

          }

      #pragma omp critical
      {
        imprimir_cola();
        printf("Eliminando: %d thread: %d\n",deq(),id );

      }
      
  }

  return 0;
}
