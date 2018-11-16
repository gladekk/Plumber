#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pygame
from Config import Config
def score_update(score,font,display):
        score_text = 'Score: {}'.format(score)
        score = font.render(score_text, True, Config['colors']['white'])
        score_rect = score.get_rect(
                 center=(
                     Config['game']['width']/2-130, 
                     Config['game']['height'] - Config['game']['bumper_size'] / 2
                 )
             )
        display.blit(score, score_rect)
def woda(self,ktora,xpos,ypos):
    #for j in range(1,4):
     #   if (time_elapsed>1000*j+1):
            if (ktora==1):
                pygame.draw.rect(self.display, Config['colors']['woda'], [xpos,ypos,35,18]) #woda dla 1
            if (ktora==2):
                pygame.draw.rect(self.display, Config['colors']['woda'], [xpos,ypos,18,35]) #woda dla 2
            if (ktora==3):
                pygame.draw.arc(self.display, Config['colors']['woda'], (xpos,ypos,52,52), 0,3.14/2, 18) #woda dla 3
            if (ktora==4):
                pygame.draw.arc(self.display, Config['colors']['woda'], (xpos,ypos,52,52), 3.14/2,3.14/2+3.14/2, 18) #woda dla 4
            if (ktora==5):
                pygame.draw.arc(self.display, Config['colors']['woda'], (xpos,ypos,52,52), 3.14,3.14/2+3.14, 18) #woda dla 5
            if (ktora==6):
                pygame.draw.arc(self.display, Config['colors']['woda'], (xpos,ypos,52,52), 1.5*3.14,3.14/2+1.5*3.14, 18) #woda dla 6
def sprawdzenie2(self,wczyt,poczatek,score):
    czyok=0
    woda(self,1, 33, 41)
    self.display.blit(poczatek,(0,25))
    p=0
    s=[0]*63
    if((wczyt[0]==1)):
           woda(self,1, 33+50,41)
           s[0]=1
    if((wczyt[0]==3)):
           woda(self,3, 33+20,41)
           s[0]=1
    if((wczyt[0]==6)):
           woda(self,6, 33+20,41-30)
           s[0]=1
    for k in range(1,63):
        if((k%7)!=0):
            if wczyt[k]==1 and (wczyt[k-1]==1 or wczyt[k-1]==4 or wczyt[k-1]==5) and s[k]==0 and s[k-1]==1:
                woda(self,1, 33 +50*(k%7+1),41+50*(k//7))
                s[k]=1
                #k=k-1
                p+=1
            if wczyt[k]==3 and (wczyt[k-1]==1 or wczyt[k-1]==4 or wczyt[k-1]==5) and s[k]==0 and s[k-1]==1:
                woda(self,3, 33 +50*(k%7+1)-25,41+50*(k//7))
                s[k]=1
                #k=k-1
                p+=1
            if wczyt[k]==6 and (wczyt[k-1]==1 or wczyt[k-1]==4 or wczyt[k-1]==5) and s[k]==0 and s[k-1]==1:
                woda(self,6, 33 +50*(k%7+1)-30,41+50*(k//7)-30)
                s[k]=1
                #k=k-1
                p+=1
        if((k%7)!=6):
            if wczyt[k]==1 and (wczyt[k+1]==1 or wczyt[k+1]==3 or wczyt[k+1]==6) and s[k]==0 and s[k+1]==1:
                woda(self,1, 33 +50*(k%7+1),41+50*(k//7))
                s[k]=1
                #k=k+1
                p+=1
            if wczyt[k]==4 and (wczyt[k+1]==1 or wczyt[k+1]==3 or wczyt[k+1]==6) and s[k]==0:
                woda(self,4, 33 +50*(k%7+1),41+50*(k//7))
                s[k]=1
                #k=k+1
                p+=1
            if wczyt[k]==5 and (wczyt[k+1]==1 or wczyt[k+1]==3 or wczyt[k+1]==6) and s[k]==0 and s[k+1]==1:
                woda(self,5, 33 +50*(k%7+1)+7,41+50*(k//7)-32)
                s[k]=1
                #k=k+1
                p+=1
        if(k>6):
            if wczyt[k]==2 and (wczyt[k-7]==2 or wczyt[k-7]==3 or wczyt[k-7]==4) and s[k]==0 and s[k-7]==1:
                woda(self,2, 33 +50*(k%7+1)+10,41+50*(k//7)-8)
                s[k]=1
                #k=k-7
                p+=1
            if wczyt[k]==5 and s[k]==0 and s[k-7]==1 and (wczyt[k-7]==2 or wczyt[k-7]==3 or wczyt[k-7]==4):
                woda(self,5, 33 +50*(k%7+1)+7,41+50*(k//7)-32)
                s[k]=1
                #k=k-7
                p+=1
            if wczyt[k]==6 and (wczyt[k-7]==2 or wczyt[k-7]==3 or wczyt[k-7]==4) and s[k]==0 and s[k-7]==1:
                woda(self,6, 33 +50*(k%7+1)-30,41+50*(k//7)-30)
                s[k]=1
                #k=k-7
                p+=1
        if(k<56):
            if wczyt[k]==2 and (wczyt[k+7]==2 or wczyt[k+7]==5 or wczyt[k+7]==6) and s[k]==0 and s[k+7]==1:
                woda(self,2, 33 +50*(k%7+1)+10,41+50*(k//7)-8)
                s[k]=1
                #k=k+7
                p+=1

            if wczyt[k]==3 and (wczyt[k+7]==2 or wczyt[k+7]==5 or wczyt[k+7]==6) and s[k]==0 and s[k+7]==1:
                woda(self,3, 33 +50*(k%7+1)-25,41+50*(k//7))
                s[k]=1
                k=k+7
                p+=1
            if wczyt[k]==4 and (wczyt[k+7]==2 or wczyt[k+7]==5 or wczyt[k+7]==6) and s[k]==0 and s[k+7]==1:
                woda(self,4, 33 +50*(k%7+1),41+50*(k//7))
                s[k]=1
                #k=k+7
                p+=1
       # else:
       #     k=-1
       # if (k==-1):

    if s[62]==1:
        woda(self,1, 33 +50*(62%7+1)+50,41+50*(62//7))
        self.display.blit(poczatek,(450,425))
        score+=p
        czyok=1
    return score,czyok
        #if ((s[62]!=1) and (time_elapsed>5000+1)):
         #   pygame.draw.rect(self.display, Config['colors']['tlo'],[0,0,500,500])

class RotatingImage:
    def __init__(self, image, xpos=0, ypos=0):
        self.image = image
        self.xpos = xpos
        self.ypos = ypos
        self.width =  image.get_width()
        self.height = image.get_height()
        self.selected = False
        self.rect = pygame.Rect(xpos, ypos, image.get_width(), image.get_height())



