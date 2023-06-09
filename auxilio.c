{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Uso de OBJDUMP para inspección de binarios"
      ],
      "metadata": {
        "id": "RuTlwQPaIdLw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "! lscpu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AvC50XRZKxcE",
        "outputId": "47d09c73-33ed-43fb-a66c-5832aa5707bd"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Architecture:                    x86_64\n",
            "CPU op-mode(s):                  32-bit, 64-bit\n",
            "Byte Order:                      Little Endian\n",
            "Address sizes:                   46 bits physical, 48 bits virtual\n",
            "CPU(s):                          2\n",
            "On-line CPU(s) list:             0,1\n",
            "Thread(s) per core:              2\n",
            "Core(s) per socket:              1\n",
            "Socket(s):                       1\n",
            "NUMA node(s):                    1\n",
            "Vendor ID:                       GenuineIntel\n",
            "CPU family:                      6\n",
            "Model:                           79\n",
            "Model name:                      Intel(R) Xeon(R) CPU @ 2.20GHz\n",
            "Stepping:                        0\n",
            "CPU MHz:                         2199.998\n",
            "BogoMIPS:                        4399.99\n",
            "Hypervisor vendor:               KVM\n",
            "Virtualization type:             full\n",
            "L1d cache:                       32 KiB\n",
            "L1i cache:                       32 KiB\n",
            "L2 cache:                        256 KiB\n",
            "L3 cache:                        55 MiB\n",
            "NUMA node0 CPU(s):               0,1\n",
            "Vulnerability Itlb multihit:     Not affected\n",
            "Vulnerability L1tf:              Mitigation; PTE Inversion\n",
            "Vulnerability Mds:               Vulnerable; SMT Host state unknown\n",
            "Vulnerability Meltdown:          Vulnerable\n",
            "Vulnerability Mmio stale data:   Vulnerable\n",
            "Vulnerability Retbleed:          Vulnerable\n",
            "Vulnerability Spec store bypass: Vulnerable\n",
            "Vulnerability Spectre v1:        Vulnerable: __user pointer sanitization and use\n",
            "                                 rcopy barriers only; no swapgs barriers\n",
            "Vulnerability Spectre v2:        Vulnerable, IBPB: disabled, STIBP: disabled, PB\n",
            "                                 RSB-eIBRS: Not affected\n",
            "Vulnerability Srbds:             Not affected\n",
            "Vulnerability Tsx async abort:   Vulnerable\n",
            "Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtr\n",
            "                                 r pge mca cmov pat pse36 clflush mmx fxsr sse s\n",
            "                                 se2 ss ht syscall nx pdpe1gb rdtscp lm constant\n",
            "                                 _tsc rep_good nopl xtopology nonstop_tsc cpuid \n",
            "                                 tsc_known_freq pni pclmulqdq ssse3 fma cx16 pci\n",
            "                                 d sse4_1 sse4_2 x2apic movbe popcnt aes xsave a\n",
            "                                 vx f16c rdrand hypervisor lahf_lm abm 3dnowpref\n",
            "                                 etch invpcid_single ssbd ibrs ibpb stibp fsgsba\n",
            "                                 se tsc_adjust bmi1 hle avx2 smep bmi2 erms invp\n",
            "                                 cid rtm rdseed adx smap xsaveopt arat md_clear \n",
            "                                 arch_capabilities\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Archivo de código C en el que suman los elementos de dos vectores de enteros, y el resultado se almacena en otro vector"
      ],
      "metadata": {
        "id": "S4yi_hnxJEBE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%file vec_sum.c\n",
        "\n",
        "void vec_sum(int* a, int* b, int* c, int N){\n",
        "    for(int i = 0; i < N; i++){\n",
        "        c[i] = a[i] + b[i];\n",
        "    }\n",
        "}"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HdHattRsIr41",
        "outputId": "aeaa48ea-c2b9-4c9c-b0d1-708d70df4f49"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting vec_sum.c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Se compila con las siguientes opciones:\n",
        "\n",
        "\n",
        "\n",
        "*   `-Os` para que ocupe menos espaico\n",
        "*   `-c` para que cree un `object file`\n",
        "*   `-o` para indicar el archivo de salida\n",
        "\n"
      ],
      "metadata": {
        "id": "MGidn9ZbJOTs"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "! gcc -Os -c vec_sum.c -o vec_sum.o"
      ],
      "metadata": {
        "id": "DM4o845KI35g"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Usar `objdump` para ver las instrucciones del `object file` generado con las siguientes opciones:\n",
        "\n",
        "\n",
        "\n",
        "*   `-M intel` para que use sintaxis de intel\n",
        "*   `-j .text` para que solo muestre el segmento de código\n",
        "*   `-D` para que muestre el disassembly\n",
        "\n"
      ],
      "metadata": {
        "id": "DswnwUFvJdOf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "! objdump -M intel -j .text -D vec_sum.o"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NzrPI-G8I76Q",
        "outputId": "406d6345-66ce-4955-a9a4-455debf1fea8"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "vec_sum.o:     file format elf64-x86-64\n",
            "\n",
            "\n",
            "Disassembly of section .text:\n",
            "\n",
            "0000000000000000 <vec_sum>:\n",
            "   0:\tf3 0f 1e fa          \tendbr64 \n",
            "   4:\t31 c0                \txor    eax,eax\n",
            "   6:\t39 c1                \tcmp    ecx,eax\n",
            "   8:\t7e 11                \tjle    1b <vec_sum+0x1b>\n",
            "   a:\t44 8b 04 86          \tmov    r8d,DWORD PTR [rsi+rax*4]\n",
            "   e:\t44 03 04 87          \tadd    r8d,DWORD PTR [rdi+rax*4]\n",
            "  12:\t44 89 04 82          \tmov    DWORD PTR [rdx+rax*4],r8d\n",
            "  16:\t48 ff c0             \tinc    rax\n",
            "  19:\teb eb                \tjmp    6 <vec_sum+0x6>\n",
            "  1b:\tc3                   \tret    \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ahora usted analice la salida de `objdump` y cuente cuantas instrucciones ha ejecutado este código. Tenga en cuenta que la cantidad de instrucciones ejecutadas cambian con el valor de `N`."
      ],
      "metadata": {
        "id": "SQcVRaKOJyBv"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Luego de hacer una inspección para unos valores pequeños de N, se llega a la siguiente tabla.\n",
        "\n",
        "| N | #instrucciones |\n",
        "|:-:|:--------------:|\n",
        "| 0 |        5       |\n",
        "| 1 |       12       |\n",
        "| 2 |       19       |\n",
        "| 3 |       26       |\n",
        "\n",
        "Se podría decir que, en general, para este código la cantidad de instrucciones es `#instrucciones = 7 * N + 5`. Con esto, ya es posible calcular el CPI asociado a un tamaño `N`."
      ],
      "metadata": {
        "id": "USis8kWp2A5o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%file test.c\n",
        "\n",
        "#include <x86intrin.h>\n",
        "#include <stdio.h>\n",
        "#include <stdlib.h>\n",
        "#include <time.h>\n",
        "\n",
        "int* crear_arr(int N){\n",
        "    int* v = (int*)malloc(sizeof(int)*N);\n",
        "    for(int i = 0; i < N; i++){\n",
        "        v[i] = rand() % 9;\n",
        "    }\n",
        "    return v;    \n",
        "}\n",
        "\n",
        "void fill_arr(int* v, int N){\n",
        "    for(int i = 0; i < N; i++){\n",
        "        v[i] = rand() % 9;\n",
        "    }\n",
        "}\n",
        "\n",
        "\n",
        "void vec_sum(int* a, int* b, int* c, int N){\n",
        "    for(int i = 0; i < N; i++){\n",
        "        c[i] = a[i] + b[i];\n",
        "    }\n",
        "}\n",
        "\n",
        "int calc_num_instr(int N){\n",
        "    return 7*N+5;\n",
        "}\n",
        "\n",
        "double calcular_CPI(long int num_cic, int num_inst){\n",
        "    return (double)num_cic / (double)num_inst;\n",
        "}\n",
        "\n",
        "int main(){\n",
        "    \n",
        "    srand(time(NULL));\n",
        "\n",
        "    int N = 8;\n",
        "\n",
        "    int* a = crear_arr(N);\n",
        "    int* b = crear_arr(N);\n",
        "    int* c = crear_arr(N);\n",
        "\n",
        "    long int tic, toc, ciclos;\n",
        "\n",
        "    tic = __rdtsc();\n",
        "    vec_sum(a, b, c, N);\n",
        "    toc = __rdtsc();\n",
        "\n",
        "    ciclos = toc - tic;\n",
        "\n",
        "    int num_instr = calc_num_instr(N);\n",
        "\n",
        "    double CPI = calcular_CPI(ciclos, num_instr);\n",
        "\n",
        "    printf(\"#instrucciones:%d\\n\", num_instr);\n",
        "    printf(\"ciclos:%ld\\n\", ciclos);\n",
        "    printf(\"CPI:%lf\\n\",CPI);\n",
        "\n",
        "    return 0;\n",
        "}\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PbXu7A7g1IL2",
        "outputId": "1ee51920-a901-4b7b-ee01-ba32ec501efa"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting test.c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "! gcc test.c -o test"
      ],
      "metadata": {
        "id": "iDEX9nW73MOo"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "! ./test"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PL1xBk8T3Plk",
        "outputId": "a0f8be93-ec01-4648-e65b-dc21ddad81f4"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "#instrucciones:61\n",
            "ciclos:282\n",
            "CPI:4.622951\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Note que esto es una aproximación muy ingenua, porque para medir el CPI deberíamos probar la función más de una vez y realizar un cálculo promedio."
      ],
      "metadata": {
        "id": "-D1AF4ng70jV"
      }
    }
  ]
}