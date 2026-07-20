import pygame

class Button:
    def __init__(
        self,
        rect,                      # pygame.Rect o tuple (x,y,w,h)
        text="",
        on_click=None,             # callable opcional
        font=None,
        bg_color=(230, 222, 180),
        border_color=(80, 80, 80),
        text_color=(25, 25, 25),
        hover_color=(245, 236, 195),
        border_width=1
    ):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.on_click = on_click
        self.font = font or pygame.font.SysFont(None, 36)

        self.bg_color = bg_color
        self.border_color = border_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.border_width = border_width

        self.enabled = True
        self.hovered = False

    def draw(self, screen):
        color = self.hover_color if (self.hovered and self.enabled) else self.bg_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

        if self.text:
            txt = self.font.render(self.text, True, self.text_color)
            txt_rect = txt.get_rect(center=self.rect.center)
            screen.blit(txt, txt_rect)

    def handle_event(self, event):
        if not self.enabled:
            return False

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click()
                return True
        return False

# On click for buttons
def act_reset(game_board, objective_board):
    game_board.setup()
    objective_board.setup_solvable(game_board)

def act_undo():
    print("Undo clicked")

def act_do():
    print("Do clicked")

def act_flip():
    print("Flip clicked")