# codes-art
Nesta pasta do GitHub estão todos os arquivos utilizados para se obter os resultados do artigo "Entendendo conservação de energia através de simulações computacionais do problema Fermi-Pasta-Ulam-Tsingou". Segue então uma enumeração dos arquivos e uma breve descrição do seu objetivo.

escritaCondiçõesIniciais.py --> Tem como função automizar a escrita de um arquivo ('fput.in') com as condições iniciais do sistema para ser dado como entrada no script do LAMMPS.

escritaTable.py --> Tem como função automizar a escrita de um arquivo ('bonds.in'), em que explicita a força de uma interação quando existe um termo quadrático ou um termo cúbico.

data.in --> Arquivo de entrada no LAMMPS com as posições iniciais dos átomos e ligações entre eles.

bonds.in --> Arquivo de entrada no LAMMPS em que explicita a força de uma interação quando existe um termo quadrático ou um termo cúbico.

fput.script --> Script utilizado pelo LAMMPS para realizar a simulação. Vale notar que o script e os arquivos de entrada devem estar na mesma pasta do sistema. Gera um arquivo res.comp com os resultados (posição e velocidade no eixo x) da simulação.

res.comp --> Arquivo de entrada para o programa análise_lammps.py. Não presente no diretório do GitHub por ser muito pesado.

análise_lammps.py --> Arquivo para analisar os resultados gerados pelo LAMMPS e desenhar gráficos de análise. Tem como entrada o arquivo res.comp.

soluçãoNumérica.py --> Programa para realizar a solução numérica do sistema e servir de comparação com os resultados do LAMMPS.

deslocamenteRelativo.py --> Programa utilizado para se desenhar a figura 2 do artigo.
