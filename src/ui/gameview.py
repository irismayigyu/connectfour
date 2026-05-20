import pygame


class Pelinäkymä:
    '''Luokka, jolla piirretään pelinäkymä'''

    def __init__(self, screen, matrix):
        '''Luokan konstruktori, jolla alustetaan pelinäkymä ja luokan argumentit

        Args:
        matrix: peliruudukko, Matrix-luokan olio
        gap: väliruudukon ruutujen välissä
        '''
        self.matrix = matrix
        self.font = pygame.font.SysFont("Comic Sans", 17)
        self.screen = screen
        self.cell_size = 87
        self.gap = 7

    def run_loop(self):
        is_running = True
        while is_running:
            self.screen.fill((125, 158, 192))
            self.draw_cells()
            if self.matrix.game_over:
                self.announce_winner(current_player)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not self.matrix.game_over:
                    x = event.pos[0]
                    col = x // 80
                    col = (x - 20) // (self.cell_size + self.gap)

                    if 0 <= col <= 6:
                        current_player = self.matrix.player
                        self.matrix.turn(col)
                        if self.matrix.checker(current_player):
                            self.matrix.game_over = True
                            self.announce_winner(current_player)

    def announce_winner(self, player):
        winner_message = self.font.render(
            f"{player} has won!", True, (0, 0, 0))
        self.screen.blit(winner_message, (34, 160))

    def draw_cells(self):
        for row in range(6):
            for col in range(7):
                x = col * (self.cell_size + self.gap) + 20
                y = row * (self.cell_size + self.gap) + 20
                # pygame.draw.rect(
                #     self.screen,
                #     (0, 0, 255),
                #     (x, y, self.cell_size, self.cell_size)
                # )
                value = self.matrix.grid[row][col]
                if value == "X":
                    color = (255, 0, 0)
                elif value == "O":
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)

                pygame.draw.circle(
                    self.screen,
                    color,
                    (x + self.cell_size // 2, y + self.cell_size // 2),
                    30
                )
