# Dungeon Escape: Stealth Master 🏰👻

Este é um projeto de jogo estilo **Roguelike/Adventure** desenvolvido em Python utilizando a biblioteca **Pygame Zero**. O projeto foi estruturado para demonstrar conceitos de Programação Orientada a Objetos (POO), manipulação de estados de jogo e lógica de colisão em grid.

## 🎮 O Jogo
O objetivo é guiar o herói através de uma masmorra perigosa até o portal ciano. O caminho é patrulhado por inimigos implacáveis, mas o herói possui uma habilidade mística de sobrevivência.

### 🌑 Mecânica Única: Invisibilidade e Imunidade
Diferente de jogos de ação comuns, aqui o herói ganha vantagem ao ficar parado:
* **Estado Móvel (Walk):** Ao se mover entre as células do grid, o herói fica visível e vulnerável a ataques.
* **Estado Imóvel (Idle):** Quando o jogador não pressiona nenhuma tecla, o herói entra em "Modo Invisível". 
    * O sprite desaparece da tela.
    * O herói torna-se **imune a qualquer dano** de colisão.
    * Útil para observar o padrão de patrulha dos inimigos sem ser derrotado.

## 🛠️ Especificações Técnicas
* **Sistema de Vidas:** O herói inicia com **7 pontos de vida**. Cada colisão enquanto visível remove 1 ponto e reseta a posição para o início da fase.
* **Animação de Sprites:** Implementada uma lógica de 4 frames cíclicos para todos os estados (`idle` e `walk`), garantindo que o mundo pareça "vivo" mesmo quando o herói está parado.
* **Movimentação Suave:** Apesar da lógica ser baseada em um grid (matriz), o deslocamento visual utiliza interpolação suave de pixels para uma melhor experiência de usuário.
* **Patrulha de IA:** Os inimigos seguem rotas pré-definidas (Waypoints) de forma cíclica.

## 📁 Estrutura de Arquivos
- `main.py`: Gerencia o loop principal, entradas do usuário e renderização de interface.
- `game_logic.py`: Contém as classes base `Entity`, `Hero` e `Enemy`, isolando a lógica física da visual.
- `/images`: Armazena os sprites organizados por prefixo e estado (ex: `hero_walk_1.png`).
- `/music`: Contém a trilha sonora `fundo.mp3`.

## 🚀 Como Executar
1. Certifique-se de ter o Python e o Pygame Zero instalados.
2. No terminal, navegue até a pasta do projeto.
3. Execute o comando:
   ```bash
   python main.py