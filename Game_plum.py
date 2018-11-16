#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pygame, sys, random, RotIm
from Config import Config
from RotIm import RotatingImage
from Levels import levels
pygame.init()
class Game:
   def __init__(self, display):
        self.display = display 
        self.score=0
        self.level=1
   def loop(self):
            angle=[0]*63
            wczyt2=[0]*63
            time_elapsed = 0
            text='' 
            clock = pygame.time.Clock()
            counter = 20
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            self.display.fill(Config['colors']['black'])
            self.display.fill(Config['colors']['tlo'])
            pygame.draw.rect(
                    self.display, 
                 Config['colors']['black'],
                 [
                     Config['game']['bumper_size'],
                     Config['game']['bumper_size'],
                     Config['game']['height'] - Config['game']['bumper_size'] * 2,
                     Config['game']['width'] - Config['game']['bumper_size'] * 2
                 ]
             )

            for i in range(9):
                     pygame.draw.rect(self.display, Config['colors']['tlo'],[25,50*i+75,50,50])
                     pygame.draw.rect(self.display, Config['colors']['tlo'],[425,50*i-25,50,50])

            #pygame.font.init()
            font = pygame.font.SysFont('arial', 28)
             
            score_text = 'Score: {}'.format(self.score)
            text = 'Time:{}'.format(counter)
            score = font.render(score_text, True, Config['colors']['white'])
            title = font.render('Plumber', True, Config['colors']['white'])
            title_rect = title.get_rect(
                 center=(
                     Config['game']['width'] / 2, 
                     Config['game']['bumper_size'] / 2
                 )
             )
 
            score_rect = score.get_rect(
                 center=(
                     Config['game']['width']/2-130, 
                     Config['game']['height'] - Config['game']['bumper_size'] / 2
                 )
             )
            time_rect = score.get_rect(
                            center=(
                     Config['game']['width']/2+80, 
                     Config['game']['height'] - Config['game']['bumper_size'] / 2
                         )
                    )
            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)
            self.display.blit(font.render(text, True, Config['colors']['white']),time_rect)
            if self.level<4:
                RotIm.score_update(self.score,font,self.display)
            krzywa=pygame.image.load('/media/sf_linux/gra/rurki/krzywa.png').convert_alpha()
            krzywa=pygame.transform.scale(krzywa,(50,50))
            prosta=pygame.image.load('/media/sf_linux/gra/rurki/prosta.png').convert_alpha()
            prosta=pygame.transform.scale(prosta,(50,50))             
            obrazki=list([prosta,pygame.transform.rotate(prosta,90),krzywa,pygame.transform.rotate(krzywa,90),pygame.transform.rotate(krzywa,180),pygame.transform.rotate(krzywa,270)])
            poczatek=pygame.image.load('/media/sf_linux/gra/items/wheel.png').convert_alpha()
            poczatek=pygame.transform.scale(poczatek,(50,50))
            self.display.blit(obrazki[0],(25,25))
            self.display.blit(poczatek,(0,25))
            self.display.blit(obrazki[0],(425,425))
            self.display.blit(poczatek,(450,425))
            #arr_coord=numpy.zeros(shape=(Config['board']['rows'],Config['board']['columns']))
            coord=[0]*63
            wczyt=[0]*63 
#            for i in range(63):
#                if(levels['level1']['1'][i]>0):
#                        czyt=obrazki[levels['level1']['1'][i]-1]
#                        x = RotatingImage(czyt, 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
#                        coord.append(x)
#                        self.display.blit(czyt,(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
#                else:
#                        x=0
#                        coord.append(x)


            if self.level==1:
                for i in list(range(63)):
                        if levels['level1']['1'][i]>0:
                            if levels['level1']['1'][i]<=2:
                                ran=random.randint(0,1)
                                x = RotatingImage(obrazki[ran], 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
                                self.display.blit(obrazki[ran],(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
                                wczyt2[i]=ran+1
                            if levels['level1']['1'][i]>2:
                                ran=random.randint(2,5)
                                x = RotatingImage(obrazki[ran], 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
                                self.display.blit(obrazki[ran],(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
                                wczyt2[i]=ran+1
                            coord[i]=x
                        else:
                            x=0
                            coord[i]=x                        
            if self.level==2:
                for i in list(range(63)):
                        if levels['level2']['2'][i]>0:
                            if levels['level2']['2'][i]<=2:
                                ran=random.randint(0,1)
                                x = RotatingImage(obrazki[ran], 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
                                self.display.blit(obrazki[ran],(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
                                wczyt2[i]=ran+1
                            if levels['level2']['2'][i]>2:
                                ran=random.randint(2,5)
                                x = RotatingImage(obrazki[ran], 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
                                self.display.blit(obrazki[ran],(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
                                wczyt2[i]=ran+1
                            coord[i]=x
                        else:
                            x=0
                            coord[i]=x   
            if self.level==3:
                counter=25
                for i in list(range(63)):
                        if levels['level3']['3'][i]>0:
                            if levels['level3']['3'][i]<=2:
                                ran=random.randint(0,1)
                                x = RotatingImage(obrazki[ran], 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
                                self.display.blit(obrazki[ran],(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
                                wczyt2[i]=ran+1
                            if levels['level3']['3'][i]>2:
                                ran=random.randint(2,5)
                                x = RotatingImage(obrazki[ran], 3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size'])
                                self.display.blit(obrazki[ran],(3*Config['game']['bumper_size']+(i%7)*2*Config['game']['bumper_size'],Config['game']['bumper_size']+(i//7)*2*Config['game']['bumper_size']))
                                wczyt2[i]=ran+1
                            coord[i]=x
                        else:
                            x=0
                            coord[i]=x
            for i in range(63):
                wczyt[i]=wczyt2[i]
            pygame.mixer.music.load('sound.mp3')
            pygame.mixer.music.play(-1)
            on=pygame.transform.scale(pygame.image.load('/media/sf_linux/gra/on.png').convert_alpha(),(50,50))
            off=pygame.transform.scale(pygame.image.load('/media/sf_linux/gra/off.png').convert_alpha(),(50,50))
            self.display.blit(on,(430,30))
            self.display.blit(off,(430,95))
            czytrue=True
            if self.level>3:
                czytrue=False

            while czytrue:
                dt=clock.tick() 
                time_elapsed += dt
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    print(event)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        x, y = event.pos
                        if(counter>0):
                            for i in range(63):
                               if(type(coord[i])!=int):
                                   if coord[i].width+coord[i].xpos>x>coord[i].xpos and coord[i].height+coord[i].ypos>y>coord[i].ypos:
                                       angle[i] += 90                                          
                                       if (wczyt2[i]==1 or wczyt2[i]==2):                                         
                                           angle[i] %= 180 
                                           wczyt[i]+=1
                                           if wczyt[i]==3:
                                               wczyt[i]=1
                                       if (wczyt2[i]==3 or wczyt2[i]==4 or wczyt2[i]==5 or wczyt2[i]==6):                                          
                                           angle[i] %= 360 
                                           wczyt[i]+=1
                                           if wczyt[i]==7:
                                               wczyt[i]=3
                                       surf = pygame.transform.rotate(coord[i].image, angle[i])
                                       pygame.draw.rect(self.display, Config['colors']['black'],[coord[i].xpos,coord[i].ypos,coord[i].width,coord[i].height])
                                       self.display.blit(surf, (coord[i].xpos,coord[i].ypos))
                                       
                        if(((x>430) and (x<480)) and ((y>30) and (y<80))):
                            pygame.mixer.music.unpause()
                        if(((x>430) and (x<480)) and ((y>95) and (y<145))):
                            pygame.mixer.music.pause()
                    if event.type == pygame.USEREVENT: 
                        counter -= 1
                        if counter > 0:
                            text = 'Time:{}'.format(counter)  
                        else: 
                            text='Czas minal!'
                            RotIm.sprawdzenie2(self,wczyt,poczatek,self.score)
                            if(RotIm.sprawdzenie2(self,wczyt,poczatek,self.score)[1]):
                                self.score=RotIm.sprawdzenie2(self,wczyt,poczatek,self.score)[0]
                                pygame.draw.rect(self.display, Config['colors']['green'],[150, 150, 200, 200])
                                self.level+=1
                                Game.loop(self)
                                if self.score>60:
                                    pygame.quit
                                pygame.draw.rect(self.display, Config['colors']['green'],[150, 150, 200, 200])
    
                            else:
                                pygame.draw.rect(self.display, Config['colors']['red'],[150, 150, 200, 200])
                                
                                           
                else:
                    pygame.draw.rect(self.display, Config['colors']['tlo'],[230,475,230,25])
                    self.display.blit(font.render(text, True, Config['colors']['white']), time_rect)
                    pygame.display.flip()
                    continue
                break
                pygame.display.update()
                if czytrue==False:
                    break
            

