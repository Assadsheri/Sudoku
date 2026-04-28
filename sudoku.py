import random
import pygame
board = [[0]*9 for _ in range(9)]
nums = [1,2,3,4,5,6,7,8,9]
for i in range(9):
    random.shuffle(nums)
    board[i]=nums.copy()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sudoku Game")
Clock = pygame.time.Clock()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
        screen.fill((225,225,255))
        pygame.display.flip()
        Clock.tick(60)
pygame.quit