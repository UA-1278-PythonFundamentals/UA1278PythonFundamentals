import pygame 
import random
import Colors

pygame.init()
# FPS = 60
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Try to guess car speed")
clock = pygame.time.Clock

font = pygame.font.Font(None, 30)
done = True

curent_attempts = 0
input_num = ""
coor_car = [50, 350]
result_message = ""
STEP = 0.5
image = pygame.image.load(r"C:\Users\vladf\Downloads\car.jpg")
num = random.randint(1, 100)

while done:
    screen.fill(Colors.White)
    screen.blit(image,(coor_car))
    coor_car[0] += STEP 
    if coor_car[0] > 600:
        coor_car[0] -= 600    
    
    greetings = font.render('Hello!!! Try to guess the speed of car, it can be from 1 to 100.', True, Colors.Green)    
    greetings_rect = greetings.get_rect()
    greetings_rect.center = [450, 50]
    screen.blit(greetings, greetings_rect)
    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_num.isdigit():
                    curent_attempts +=1
                    t = int(input_num)

                
                    if t ==  num:
                        result_message = "success"
                        done = False
                    elif len(str(t)) > 2:
                        result_message = "it cant be more than 100"    
                    elif t < num:
                        result_message = "more"
                    else: result_message = "less" 
                    input_num = ""
                if curent_attempts > 10:
                    result_message = f"Lose. it was: {num}."
                    done = False    
            elif event.key == pygame.K_BACKSPACE:
                input_num = input_num[:-1]
            else:
                input_num += event.unicode

    input_text = font.render(input_num,True, Colors.Black)
    screen.blit(input_text,(450,200))

    att = font.render(f"Attempts: {curent_attempts} / 10",True, Colors.Black)
    screen.blit(att,(50,100))

    result_text = font.render(result_message,True, Colors.Black)
    screen.blit(result_text,(450,60))

    
    pygame.display.flip()   
    # clock.tick(FPS)   
