#include <stdio.h>
#include <stdlib.h>
#include <windows.h> // necessário no Windows

int main() {
    // Define UTF-8 para entrada e saída
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    float num1, num2, media;

    printf("Digite o primeiro número: ");
    scanf("%f", &num1);

    printf("Digite o segundo número: ");
    scanf("%f", &num2);

    media = (num1 + num2) / 2;
    printf("A média é: %.2f\n", media);

    getchar(); getchar();
    return 0;
}
