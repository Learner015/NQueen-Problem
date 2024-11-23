import pygame
import sys

pygame.init()

N = int(input("enter the number N : "))

size = 50
width = N*size
height = N *size

white = (255,255,255)
black = (0,0,0)
red = (255,150,0)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("N-Queens")

def draw_board(queens):
    for row in range(N):
        for column in range(N):
            board=pygame.Rect(column*size,row*size,size,size)
            color = white if (row + column) % 2 == 0 else black
            pygame.draw.rect(screen, color, board)
            if (row,column) in queens:
                pygame.draw.circle(screen,red, board.center, size//2 -5)


def is_safe(queens,row,col):
    for r,c in queens:
        if r== row or c==col or abs(r-row) == abs(c-col):
            return False
    return True
def solve_n_queens(queens, row):
    if row ==N:
        return True
    for col in range(N):
        if is_safe(queens,row,col):
            queens.append((row, col))
            if solve_n_queens(queens, row+1):
                return True
            queens.pop()
    return False

def main():
     queens = []
     solve_n_queens(queens, 0)
     while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
         screen.fill(white)
         draw_board(queens)
         pygame.display.flip()

if __name__ == '__main__':
    main() 