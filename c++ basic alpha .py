#divulgada no git hub(nao confunda com essas besteiras que tu esta pensando)
#isso e uma beta lançarei mais versões com mais paginas
#creditos gracye
#veja tbm nosso site,em breve vou lançar doom no pygame,e depois warm hands beta 1(tbm vao tar no git hub)
#agradecimentos ao alisson
import flet as ft

def main(page: ft.Page):
    page.title = "C++ BASICO"
    page.bgcolor = "#181818"

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    bgcolor="#181818",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Column([
                            ft.Text("Olá, hoje ensinaremos C++ básico", size=40, color="white"),
                            ft.Text(
                                    "C++ é uma linguagem de programação de uso geral, conhecida por sua eficiência, velocidade "
                    "e capacidade de trabalhar tanto em alto nível quanto em baixo nível.",
                                    size=15, color="white"
                                ),
                                ft.Text("Informações do C++:", size=30, font_family="Arial", color="white"),

                ft.Text(
                    "Se você perguntar para qualquer pessoa que programa qual é a linguagem “mais difícil”, "
                    "muitos vão dizer: C++. Mas a parte curiosa é que, ao mesmo tempo, ela também é uma das "
                    "linguagens mais importantes e presentes na nossa vida, mesmo que a gente nem perceba. "
                    "C++ permite trabalhar bem perto da máquina, manipulando memória e otimizando o desempenho "
                    "ao máximo, mas também permite criar sistemas grandes, motores de jogos, simulações, robôs "
                    "e muito mais. É isso que o C++ faz.",
                    size=15,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text("Mão na massa", size=30, font_family="Arial", color="white"),
                ft.Text("Vamos imprimir um texto em C++:", size=15, font_family="Arial", color="white"),

                ft.Text(
                    "#include <iostream>\n\nint main() {\n    std::cout << \"Olá, mundo!\";\n    return 0;\n}",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),

                ft.Text(
                    "Para incluir qualquer biblioteca em C++ usamos '#include'. A biblioteca 'iostream' permite "
                    "usar funções como std::cout e std::cin. Outras bibliotecas podem ser adicionadas conforme a necessidade.",
                    size=15,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "'int main()' é o ponto de entrada do programa, ou seja, onde tudo começa. 'return 0;' indica "
                    "que o programa terminou corretamente — e em C++ moderno, esse retorno já é automático.",
                    size=15,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "Dentro das {} escrevemos o código que será executado. O 'std' é um namespace que organiza funções "
                    "e evita conflitos de nomes. Por isso usamos std:: antes de funções como cout.",
                    size=15,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "Se você quiser usar apenas 'cout' sem escrever 'std::', basta usar 'using namespace std;'.",
                    size=15,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "O ponto e vírgula ';' marca o fim de uma instrução. Depois disso, é só fechar as {} e o programa "
                    "imprimirá 'Olá, mundo!'.",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "Podemos adicionar comentários no código usando '//'. Tudo que vier depois disso é ignorado pelo compilador:",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "//exemplo\n#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Olá, mundo!\"; // imprimir o ola mundo\n    return 0;\n} // fim do código",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),

                ft.Text(
                    "Se você escrever 'Olá, mundo!' sem '\\n', o próximo texto aparecerá na mesma linha. "
                    "Por isso usamos '\\n' para quebrar a linha:",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Olá, mundo!\\nBem-vindo ao C++!\";\n    return 0;\n}",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),

                ft.Text("para indentificar se algo e igual ou menor que alguma coisa usamos os sinais: <> que são operadores relacionais, Eles é usado para comparar dois valores e retorna um resultado verdadeiro (true) se forem diferentes, ou falso (false) se forem iguais.",size=15, font_family="Arial", color="white"),

                ft.Text("null//nulo < 0 //ele retorna falando se e verdadeiro que ele e maior ou nao" \
                "null > 0 //a mesma coisa so que menor que 0",font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="yellow"),
 
                ft.Text("Variáveis", size=30, font_family="Arial", color="white"),

                ft.Text(
                    "Imagine que você tem várias caixinhas na sua mesa. Cada caixinha tem um nome e guarda algum tipo "
                    "de informação: números, palavras, letras… o que você quiser. Em C++, essas caixinhas são chamadas "
                    "de variáveis.",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "Antes de criar uma variável, você precisa dizer qual tipo de dado ela vai guardar. Aqui estão alguns "
                    "dos tipos mais comuns:",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "int → números inteiros (10, -3, 0…)\n"
                    "float → números quebrados (1.75, 3.14…)\n"
                    "double → parecido com float, mas maior\n"
                    "char → uma única letra ('A', 'b')\n"
                    "string → textos \\ necessario usar a biblioteca <string> \n"
                    "bool → verdadeiro ou falso",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="yellow"
                ),

                ft.Text(
                    "#include <iostream>\nusing namespace std;\n\nint main() {\n    int idade = 16;\n    float altura = 1.72;\n    char inicial = 'L';\n    string nome = \"paulo\";\n    bool estudando = true;\n\n    cout << \"Nome: \" << nome << \"\\n\";\n    cout << \"Idade: \" << idade << \"\\n\";\n    cout << \"Altura: \" << altura << \"\\n\";\n    cout << \"Inicial: \" << inicial << \"\\n\";\n    cout << \"Estudando? \" << estudando << \"\\n\";\n\n    return 0;\n}",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),

                ft.Text(
                    "No exemplo acima mostramos como dar valor a uma variável e imprimir seu conteúdo. O tipo bool indica se a variável é verdadeira ou falsa.",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "Variáveis podem mudar de valor também, como no exemplo abaixo:",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "int x = 10;\nx = 20; // agora x vale 20",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),

                ft.Text("Estruturas condicionais", size=30, font_family="Arial", color="white"),

                ft.Text(
                    "A estrutura condicional 'if' permite que o programa tome decisões com base em uma condição. "
                    "'else' e 'else if' completam esse processo.",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "• if = se\n• else = senão\n• else if = senão se",
                    size=16,
                    font_family="Arial",
                    color="white"
                ),

                ft.Text(
                    "#include <iostream>\nusing namespace std;\n\nint main() {\n    int x = 10;\n\n    if (x > 5) {\n        cout << \"x é maior que 5\\n\";\n    } else {\n        cout << \"x é menor ou igual a 5\\n\";\n    }\n\n    return 0;\n}",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),

                ft.Text(
                    "No exemplo acima, verificamos se a variável x (que vale 10) é maior que 5. "
                    "Se for, mostramos a mensagem correspondente; caso contrário, mostramos outra.", size=16,
                    font_family="Arial",
                    color="white"
                    
                ),

                ft.Text("tbm temos o else if caso o if anterior for falso usamos o else if, como no exemplo abaixo:"

                ,size=16,font_family="arial",color="white"),

                ft.Text("""#include <iostream>
using namespace std;

int main() {
    int idade = 20;

    if (idade < 18) {
        cout << "Menor de idade" << endl;
    }
    else if (idade < 65) {
        cout << "Adulto" << endl;
    }
    else {
        cout << "Idoso" << endl;
    }

    return 0;
}
""",font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"),

                    ft.Text("tbm podemos usar o swift,caso seja muitos if,else podemos usar o swift:",size=16,font_family="arial",color="white"),

                   ft.Text("""#include <iostream>
using namespace std;

int main() {
    int opcao;

    cout << "Escolha uma opção:\n";
    cout << "1 - Jogar\n";
    cout << "2 - Carregar jogo\n";
    cout << "3 - Sair\n";
    cin >> opcao;

    switch(opcao) {
        case 1:
            cout << "Iniciando o jogo..." << endl;
            break;
        case 2:
            cout << "Carregando jogo salvo..." << endl;
            break;
        case 3:
            cout << "Saindo do programa. Até logo!" << endl;
            break;
        default:
            cout << "Opção inválida. Tente novamente!" << endl;
    }

    return 0;
}

                           """,font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"),

                    ft.Text("""cin >> opcao; → o usuário digita um número correspondente à escolha" \
                    switch(opcao) verifica o valor digitado.

Cada case corresponde a uma opção possível:

1 → Jogar

2 → Carregar jogo

3 → Sair

Break

Para evitar que os próximos cases sejam executados mesmo que não correspondam.

Default

Captura qualquer valor que não seja 1, 2 ou 3, mostrando mensagem de erro.""",size=16,font_family="arial",color="white"),


                ft.Text("dados de repetição e leitura do input",size=30,font_family="arial",color="white"),
                ft.Text(
                    "para ler o input(entrada),usamos cin , O cin é um objeto em C++ usado para entrada de dados. Ele utiliza o operador de extração (>>) para capturar valores do teclado e armazená-los em variáveis. É amplamente utilizado para leitura de dados simples como inteiros, floats e strings.", size=16,
                    font_family="Arial",
                    color="white"
                ),
                ft.Text(
                    """#include <iostream>
using namespace std;
int main() {
   int idade;
   cout << "Digite sua idade: ";
   cin >> idade; // Lê a entrada do usuário
   cout << "Sua idade é " << idade << endl;
   return 0;
}""",font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),
                ft.Text("o primeiro dado de repetição que faremos e o for,O for é usado quando sabemos exatamente quantas vezes queremos repetir algo." \
                "ai nos botamos como no exemplo abaixo",size=16,font_family="arial",color="white"),

                ft.Text("""#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) { // repete 5 vezes
        cout << "Olá!" << endl;
    }
    return 0;
}
""",font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"),
                    ft.Text("nos imprimimos o texto 'ola' 5 vezes "),

                    ft.Text("tbm temos o while,O while é usado quando não sabemos exatamente quantas vezes vamos repetir, mas temos uma condição que decide quando parar como no exemplo abaixo:",size=16,font_family="arial",color="white"),
                    ft.Text("""#include <iostream>
using namespace std;

int main() {
    int numero = 1; // começamos do número 1

    while (numero <= 5) { // enquanto numero for menor ou igual a 5
        cout << "Número: " << numero << endl;
        numero++; // aumentamos numero em 1
    }

    return 0;
}
""",font_family="Courier New",size=16,
                    selectable=True,
                    color="blue"),
                    ft.Text("""temos por ultimo o do-while, O do...while é um tipo de loop em C++.
Ele serve para repetir um bloco de código várias vezes, mas com uma diferença importante:
O bloco de código é executado pelo menos uma vez, antes de checar a condição.""",size=16,font_family="arial",color="white"),
                    ft.Text("""do {
    // código que será repetido
} while (condição);
O código dentro do { } é executado uma vez primeiro.

Depois, a condição while(condição) é verificada:

Se verdadeira, o loop repete.

Se falsa, o loop termina.""",font_family="Courier New",size=16,
                    selectable=True,
                    color="yellow"),
                     ft.Text("""#include <iostream>
using namespace std;

int main() {
    int numero = 6;

    do {
        cout << "Número: " << numero << endl;
        numero++;
    } while (numero <= 5);

    return 0;
}
""",font_family="Courier New",size=16,
                    selectable=True,
                    color="blue"),


                                ft.Text(
                                    "acho que eu já te ensinei um básico...",
                                    size=15, color="white"
                                ),

                                ft.Text(
                                    "obs: várias das coisas ensinadas aqui servem em Python, C, Java...",
                                    size=10, color="white"
                                ),
                            ft.ElevatedButton("biblioteca stream", width=260, height=45,
                                              bgcolor="#2b2b2b", color="#006EFF",
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),
                                                                    side=ft.BorderSide(width=1, color="#00FF00"),
                                                                    elevation=0),
                                              on_click=lambda _: page.go("/stream")),
                            ft.ElevatedButton("stl", width=260, height=45,
                                              bgcolor="#2b2b2b", color="#0B74ED",
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),
                                                                    side=ft.BorderSide(width=1, color="#5900FF"),
                                                                    elevation=0),
                                              on_click=lambda _: page.go("/stl")),
                            ft.ElevatedButton("orientações de objetos", width=260, height=45,
                                              bgcolor="#2b2b2b", color="#3763BB",
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),
                                                                    side=ft.BorderSide(width=1, color="#27006F83"),
                                                                    elevation=0),
                                              on_click=lambda _: page.go("/poo")),
                            ft.ElevatedButton("funções", width=260, height=45,
                                              bgcolor="#2b2b2b", color="#1800F1",
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),
                                                                    side=ft.BorderSide(width=1, color="#004570"),
                                                                    elevation=0),
                                              on_click=lambda _: page.go("/funcoes")),
                            ft.ElevatedButton("frameworks", width=260, height=45,
                                              bgcolor="#2b2b2b", color="#00FFAA",
                                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),
                                                                    side=ft.BorderSide(width=1, color="#00FFAA"),
                                                                    elevation=0),
                                              on_click=lambda _: page.go("/frameworks"))
                        ], spacing=10)
                    ]
                )
            )

        elif page.route == "/stream":
            page.views.append(
                ft.View(
                    route="/stream",
                    bgcolor="#181818",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                         ft.Text("Biblioteca Stream", size=35, color="white"),
                ft.Text(
                    "A biblioteca iostream é fundamental em C++ para a entrada e saída de dados. "
                    "Ela fornece as funções cout e cin para imprimir e ler dados, respectivamente.",
                    size=18,
                    color="white"
                ),
                ft.Text(
                    "Mas eu não vou falar da iostream e sim falar sobre outras bibliotecas de stream que existem em C++ como: fstream, ofstream, sstream",
                    size=18,
                    color="white"
                ),
                ft.Text("fstream", size=30, color="white"),
                ft.Text(
                    "A biblioteca <fstream> permite trabalhar com arquivos em C++, tanto para criar quanto para ler e excluir arquivos.",
                    size=18,
                    color="white"
                ),
                ft.Text("Classes principais", size=30, color="white"),
                ft.Text(
                    """std::ifstream → input file stream → leitura de arquivos
std::ofstream → output file stream → escrita em arquivos
std::fstream → leitura e escrita em arquivos (combina ifstream + ofstream)
""",
                    font_family="Courier New",
                    size=18,
                    color="white"
                ),
                ft.Text("Exemplo de uso do ofstream para escrever em um arquivo:", size=18, color="white"),
                ft.Text(
                    """#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ofstream arquivoSaida("teste.txt"); // criar/abrir arquivo para escrever
    if (arquivoSaida.is_open()) {
        arquivoSaida << "Linha 1\\n";
        arquivoSaida << "Linha 2\\n";
        arquivoSaida.close();
    }

    std::ifstream arquivoEntrada("teste.txt"); // abrir arquivo para ler
    std::string linha;
    if (arquivoEntrada.is_open()) {
        while (getline(arquivoEntrada, linha)) {
            std::cout << linha << std::endl;
        }
        arquivoEntrada.close();
    }

    return 0;
}
""",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),
                ft.Text(
                    "No exemplo acima, usamos ofstream para criar um arquivo chamado teste.txt e escrever duas linhas nele. "
                    "Depois usamos ifstream para abrir o mesmo arquivo e ler seu conteúdo linha por linha, imprimindo no console. "
                    "Lembre-se de fechar os arquivos após o uso com close().",
                    size=18,
                    color="white"
                ),
                ft.Text("sstream", size=30, color="white"),
                ft.Text(
                    "<sstream> — fluxos em memória\nA biblioteca <sstream> permite trabalhar com strings como se fossem arquivos ou streams.",
                    size=18,
                    color="white"
                ),
                ft.Text("Classes principais", size=30, color="white"),
                ft.Text(
                    """std::istringstream → ler dados de uma string
std::ostringstream → escrever dados em uma string
std::stringstream → ler e escrever na mesma string
""",
                    font_family="Courier New",
                    size=18,
                    color="white"
                ),
                ft.Text(
                    """#include <iostream>
#include <sstream>
#include <string>

int main() {
    std::string dados = "10 20 30";
    std::istringstream iss(dados);

    int a, b, c;
    iss >> a >> b >> c; // lê valores da string como se fosse input
    std::cout << a + b + c << std::endl; // saída: 60

    std::ostringstream oss;
    oss << "Soma: " << (a + b + c);
    std::cout << oss.str() << std::endl; // saída: "Soma: 60"

    return 0;
}
""",
                    font_family="Courier New",
                    size=16,
                    selectable=True,
                    color="blue"
                ),
                ft.Text(
                    "No exemplo acima, usamos istringstream para ler números de uma string e armazená-los em variáveis inteiras. "
                    "Depois usamos oostringstream para escrever uma mensagem formatada em outra string.",
                    size=18,
                    color="white"
                ),
                ft.Text(
                    "Observação:\n- Útil para conversão entre strings e números\n- Funciona muito bem para manipulação de dados CSV ou linhas de arquivos de texto",
                    size=18,
                    color="white"
                ),
                # Botão Voltar
                ft.ElevatedButton(
                    "Voltar",
                    bgcolor="#020936",
                    on_click=lambda e: page.go("/")
                )
                    ]
                )
            )

        elif page.route == "/stl":
            page.views.append(
                ft.View(
                    route="/stl",
                    bgcolor="#181818",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text("STL", size=35, color="white"),
                        ft.ElevatedButton("Voltar", bgcolor="#020936", on_click=lambda _: page.go("/"))
                    ]
                )
            )

        elif page.route == "/poo":
            page.views.append(
                ft.View(
                    route="/poo",
                    bgcolor="#181818",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text("Orientações de Objetos", size=35, color="white"),
                        ft.ElevatedButton("Voltar", bgcolor="#020936", on_click=lambda _: page.go("/"))
                    ]
                )
            )

        elif page.route == "/funcoes":
            page.views.append(
                ft.View(
                    route="/funcoes",
                    bgcolor="#181818",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text("Funções", size=35, color="white"),
                        ft.Text("Uma função é um bloco de código que executa alguma operação. Opcionalmente, uma função pode definir parâmetros de entrada que permitem que os chamadores passem argumentos para a função. Uma função também pode retornar um valor como saída",size=18,color="white"),
                    
                       ft.Text("A função a seguir aceita dois inteiros de um chamador e retorna sua soma; a e b são parâmetros do tipo int",size=18,color="white"),
                       ft.Text(""" int sum(int a, int b)
{
    return a + b;
} """,font_family="Courier New",size=16,
                    selectable=True,
                    color="blue"),
                    ft.Text("A função pode ser invocada ou chamada de qualquer número de locais no programa. Os valores que são passados para a função são os argumentos, cujos tipos devem ser compatíveis com os tipos de parâmetro na definição de função",size=18,color="white"),
                    ft.Text(""" int main()
{
    int i = sum(10, 32);
    int j = sum(i, 66);
    cout << "The value of j is" << j << endl; // 108
}""",font_family="courier New",size=16,color="yellow",selectable=True),
ft.Text("No exemplo acima, a função sum é chamada duas vezes: primeiro com os argumentos 10 e 32, e depois com o valor retornado i e 66. O resultado final é impresso na tela.",size=18,color="white"),
                        ft.ElevatedButton("Voltar", bgcolor="#020936", on_click=lambda _: page.go("/"))
                    ]
                )
            )

        elif page.route == "/frameworks":
            page.views.append(
                ft.View(
                    route="/frameworks",
                    bgcolor="#181818",
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text("Frameworks", size=35, color="white"),
                        ft.Text("""Frameworks em C++ fornecem estruturas reutilizáveis e bibliotecas prontas para desenvolvimento. 
Principais frameworks:
- Qt: GUI multiplataforma
- Boost: bibliotecas gerais e utilitárias
- POCO: aplicações de rede e internet
- Cinder: multimídia e gráficos
- JUCE: áudio e música digital
- OGRE: motor gráficco 3D
- SDL: desenvolvimento de jogos 2D/3D
- SFML: multimídia e jogos 2D/3D
- wxWidgets: GUI multiplataforma
- DROGON: criação de servidores web em http/https
                                
Vantagens: mais rápido para desenvolver, código organizado e funcionalidades avançadas.
""",size=18,color="white"),
                        ft.ElevatedButton("Voltar", bgcolor="#020936", on_click=lambda _: page.go("/"))
                    ]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
