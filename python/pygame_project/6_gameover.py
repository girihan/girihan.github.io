# 종료 조건
# 1. 모든 공을 없애면 종료(성공)
# 2. 캐릭터는 공에 닿으면 게임 종료(실패)
# 3. 시간 제한 99초 초과 시 게임 종료(실패)

import os
import pygame

#################################################################
# initialize (MUST)

pygame.init() #initialize(MUST)

# set screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption('Nado Pang')

#FPS
clock = pygame.time.Clock()
#################################################################

# 1. user game init(background image, game image, position, speed, font, etc..)
current_path = os.path.dirname(__file__) # return current position
image_path = os.path.join(current_path, 'images')

# background
background = pygame.image.load(os.path.join(image_path, 'background.png'))

# stage
stage = pygame.image.load(os.path.join(image_path, 'stage.png'))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# character
character = pygame.image.load(os.path.join(image_path, 'character.png'))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - stage_height - character_height

# character move
character_to_x = 0
# character speed
character_speed = 5

# weapon
weapon = pygame.image.load(os.path.join(image_path, 'weapon.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
# multiple shot
weapons = []
# weapon speed
weapon_speed = 10

# ball(4 balls)
ball_images = [
    pygame.image.load(os.path.join(image_path, 'balloon1.png')),
    pygame.image.load(os.path.join(image_path, 'balloon2.png')),
    pygame.image.load(os.path.join(image_path, 'balloon3.png')),
    pygame.image.load(os.path.join(image_path, 'balloon4.png'))]

# each ball speed per size
ball_speed_y = [ -18, -15, -12, -9] # index 0,1,2,3

# balls
balls = []
# first large ball
balls.append({
    "pos_x" : 50, # x position of ball
    "pos_y" : 50, # y position of ball
    "img_idx" : 0, # ball image index
    "to_x" : 3, # direction of x position, 3 is left, 3 is right
    "to_y" : -6, # direction of y position
    "init_spd_y" : ball_speed_y[0] # first y speed
})

# 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# 폰트 정의
game_font = pygame.font.Font(None, 40)
total_time = 100
start_ticks = pygame.time.get_ticks() #시작시간 정의

# 게임 종료 메시지/TimeOut(실패), Mission Complete(성공), Game Over(공에 맞아 실패)
game_result = "Game Over"

# event loop
running = True
while running:
    dt = clock.tick(30) # set fps
    
    # 2. handling event(keyboard, mouse, etc )
    for event in pygame.event.get(): # what kind of event is occurred??
        if event.type == pygame.QUIT: # if close windoe event is occurred??
            running = False # end game

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. character position handling
    character_x_pos += character_to_x
    if character_x_pos < 0: 
        character_x_pos = 0
    if character_x_pos > screen_width - character_width: 
        character_x_pos = screen_width - character_width

    # weapon position
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # weapon postion will be going up
    # remove weapon when touch upper
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # ball position
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # 가로벽에 닿았을때 공 이동위치 변경(튕겨나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        
        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그 외의 모든 경우에는 속도를 증가
            ball_val["to_y"] += 0.5
        
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. collision handling
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        # 공 rect 정보
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            game_result = "Game Over"
            running = False
            break

        # 공과 무기 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # 무기 rect 정보
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            
            #공과 무기 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx # 해당 무기를 없애기 위한 값 설정
                ball_to_remove = ball_idx #해당 공 없애기 위한 값 설정

                # 가장 작은 공이 아니면 다은 단계의 공으로 나누기
                if ball_img_idx < 3:
                    # 현재 공크기 정보를 가져옴
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # 나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx+1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), # x position of ball
                        "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), # y position of ball
                        "img_idx" : ball_img_idx + 1, # ball image index
                        "to_x" : -3, # direction of x position, 3 is left, 3 is right
                        "to_y" : -6, # direction of y position
                        "init_spd_y" : ball_speed_y[ball_img_idx+1] # first y speed
                    })
                    balls.append({
                        "pos_x" : ball_pos_x + (ball_width/2) - (small_ball_width/2), # x position of ball
                        "pos_y" : ball_pos_y + (ball_height/2) - (small_ball_height/2), # y position of ball
                        "img_idx" : ball_img_idx + 1, # ball image index
                        "to_x" : 3, # direction of x position, 3 is left, 3 is right
                        "to_y" : -6, # direction of y position
                        "init_spd_y" : ball_speed_y[ball_img_idx+1] # first y speed
                    })

                break
        else:#계속 게임을 진행
            continue # 안쪽 for문 조건이 맞지 않으면 continue, 바깥쪽 for 문 계속 수행
        break # 안쪽 for 문에서 break를 만나면 여기로 진입 가능, 2중 for 문을 한번에 탈출

    # 충돌된 공과 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
    
    #모든 공을 없앤경우 게임 종료
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    # 5. draw screen
    screen.blit(background, (0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
    timer = game_font.render("Time:{}".format(int(total_time - elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))

    # 시간 초과했다면
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    
    # update screen
    pygame.display.update()

# 게임 오버 메시지
msg = game_font.render(game_result, True, (255,255,0)) #yellow
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()

# pause
pygame.time.delay(2000) # delay 2 sec

# exit pygame
pygame.quit()
