import display
import random 
import pygame
import constants

pygame.init()

done = False

# 650 , 150
def check_events():
    for event in pygame.event.get(): # User did something
        
        if event.type == pygame.QUIT: # If user clicked close
            global done
            done = True # Flag that we are done so we exit this loop
        
        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            pygame.mixer.music.play()   
            
        elif event.type == 25:
            current_display.timer_event()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_display.key_left()
            if event.key == pygame.K_RIGHT:
                current_display.key_right()
            if event.key == pygame.K_UP:
                current_display.key_up()
            if event.key == pygame.K_DOWN:
                current_display.key_down()
            if event.key == pygame.K_RETURN:
                current_display.key_enter()
            if event.key == pygame.K_ESCAPE:
                current_display.key_esc()
            if event.key == pygame.K_p:
                current_display.p_key()
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                current_display.key_down_upd()            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            current_display.left_mousebtn()
                

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
display.update_music()
display_game = display.DisplayGame()
display_main = display.DisplayMain(display_game)
display_score = display.DisplayScore()
current_display = display_main
pygame.key.set_repeat(200, 70)
# -------- Main Program Loop -----------

while not done:
    
    check_events() 
    
    if display.screen_no == constants.MAIN and current_display != display_main :
        if current_display != display_score :
            display.update_music()
        current_display = display_main
        
    elif display.screen_no == constants.NEW and current_display != display_game:
        display_game.new_game()
        current_display = display_game
        display.update_music()
        
    elif display.screen_no == constants.CONTINUE and current_display != display_game :
        current_display = display_game
        display.update_music()
    
    if display.screen_no == constants.SCORE and current_display != display_score :
            current_display = display_score
        
    elif display.screen_no == constants.EXIT:
        done = True
        
        
    # --- Game logic should go here
    current_display.logic()
    
    display.screen.fill(constants.OFF_WHITE)
 
    current_display.draw()
    
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
    
pygame.quit()
