import pygame as pg
import random as r

class Danmaku:

  def __init__(self,img,size):
    self.img_raw = pg.image.load(img)
    self.size = pg.Vector2(size)

  def display(self,dir):
    dir_img_raw = pg.transform.rotate(self.img_raw, 90*dir)
    return pg.transform.scale(dir_img_raw,self.size)

  def shot(self,dir,speed,pos):
    self.pos = pg.Vector2(pos)
    if dir == 0:
      self.pos += pg.Vector2(0,-speed)
    elif dir == 1:
      self.pos += pg.Vector2(speed,0)
    elif dir == 2:
      self.pos += pg.Vector2(0,speed)
    elif dir == 3:
      self.pos += pg.Vector2(-speed,0)
    return self.pos

def main():

  # 初期設定
  chip_s = 48 # マップチップの基本サイズ
  map_s  = pg.Vector2(11,11) # マップの横・縦の配置数 

  pg.init() 
  pg.display.set_caption('ぼくのかんがえたさいきょうのげーむ II')
  disp_w = int(chip_s*map_s.x)
  disp_h = int(chip_s*map_s.y)
  screen = pg.display.set_mode((disp_w,disp_h))
  clock  = pg.time.Clock()
  font   = pg.font.Font(None,24)
  font_key = pg.font.Font(None,36)
  font_finish = pg.font.Font(None,48)
  setting = True
  exit_flag = False
  exit_code = '000'
  roop = 5

  # グリッド設定
  grid_c = '#bbbbbb'

  # 妖精の画像読込み
  yousai_left_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_left_raw = pg.image.load('./yousei.png')
  yousai_left_p = pg.Vector2(24,32) # 前向き・2番目のポーズの位置　
  yousai_left_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_left_tmp = yousai_left_raw.subsurface(pg.Rect(yousai_left_p,yousai_left_pose_s))
  yousai_left_img = pg.transform.scale(yousai_left_tmp,yousai_left_s) 

  yousai_right_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_right_raw = pg.image.load('./yousei.png')
  yousai_right_p = pg.Vector2(96,96) # 前向き・2番目のポーズの位置　
  yousai_right_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_right_tmp = yousai_right_raw.subsurface(pg.Rect(yousai_right_p,yousai_right_pose_s))
  yousai_right_img = pg.transform.scale(yousai_right_tmp,yousai_right_s) 
  
  yousai_top_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_top_raw = pg.image.load('./yousei.png')
  yousai_top_p = pg.Vector2(96,192) # 前向き・2番目のポーズの位置　
  yousai_top_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_top_tmp = yousai_top_raw.subsurface(pg.Rect(yousai_top_p,yousai_top_pose_s))
  yousai_top_img = pg.transform.scale(yousai_top_tmp,yousai_top_s) 

  yousai_bottom_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_bottom_raw = pg.image.load('./yousei.png')
  yousai_bottom_p = pg.Vector2(24,128) # 前向き・2番目のポーズの位置　
  yousai_bottom_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_bottom_tmp = yousai_bottom_raw.subsurface(pg.Rect(yousai_bottom_p,yousai_bottom_pose_s))
  yousai_bottom_img = pg.transform.scale(yousai_bottom_tmp,yousai_bottom_s) 

  # 弾幕の画像読込み
  random = 0
  danmaku_top = False
  danmaku_bottom = False
  danmaku_left = False
  danmaku_right = False
  speed = 2
  danmaku_start = [pg.Vector2(253,30),pg.Vector2(253,450),pg.Vector2(454,228),pg.Vector2(50,228)]
  knife_start = [pg.Vector2(253,185),pg.Vector2(253,239),pg.Vector2(255,228),pg.Vector2(215,228)]
  danmaku_slow = {}
  danmaku_fast = {}
  danmaku_slow_list = []
  danmaku_fast_list = []

  knife = {}
  knife_list = []

  danmaku_top_slow_p = {}
  danmaku_top_fast_p = {}
  danmaku_top_slow_dis = {}
  danmaku_top_fast_dis = {}
  danmaku_top_slow_dis_list = []
  danmaku_top_fast_dis_list = []

  danmaku_bottom_slow_p = {}
  danmaku_bottom_fast_p = {}
  danmaku_bottom_slow_dis = {}
  danmaku_bottom_fast_dis = {}
  danmaku_bottom_slow_dis_list = []
  danmaku_bottom_fast_dis_list = []

  danmaku_right_slow_p = {}
  danmaku_right_fast_p = {}
  danmaku_right_slow_dis = {}
  danmaku_right_fast_dis = {}
  danmaku_right_slow_dis_list = []
  danmaku_right_fast_dis_list = []

  danmaku_left_slow_p = {}
  danmaku_left_fast_p = {}
  danmaku_left_slow_dis = {}
  danmaku_left_fast_dis = {}
  danmaku_left_slow_dis_list = []
  danmaku_left_fast_dis_list = []

  knife_top_p = {}
  knife_top_dis = {}
  knife_top_dis_list = []

  knife_bottom_p = {}
  knife_bottom_dis = {}
  knife_bottom_dis_list = []


  knife_right_p = {}
  knife_right_dis = {}
  knife_right_dis_list = []

  knife_left_p = {}
  knife_left_dis = {}
  knife_left_dis_list = []
  

  # ゲームループ
  while not exit_flag:

    if setting:
      for i in range(roop):
        danmaku_top_p_name = f"danmaku_top_{i}_p"
        danmaku_top_dis_name = f"danmaku_top_{i}_dis"
        danmaku_top_slow_p[danmaku_top_p_name] = danmaku_start[0]
        danmaku_top_fast_p[danmaku_top_p_name] = danmaku_start[0]
        danmaku_top_slow_dis[danmaku_top_dis_name] = False
        danmaku_top_fast_dis[danmaku_top_dis_name] = False
        danmaku_top_slow_dis_list.append(danmaku_top_dis_name)
        danmaku_top_fast_dis_list.append(danmaku_top_dis_name)

        danmaku_bottom_p_name = f"danmaku_bottom_{i}_p"
        danmaku_bottom_dis_name = f"danmaku_bottom_{i}_dis"
        danmaku_bottom_slow_p[danmaku_bottom_p_name] = danmaku_start[1]
        danmaku_bottom_fast_p[danmaku_bottom_p_name] = danmaku_start[1]
        danmaku_bottom_slow_dis[danmaku_bottom_dis_name] = False
        danmaku_bottom_fast_dis[danmaku_bottom_dis_name] = False
        danmaku_bottom_slow_dis_list.append(danmaku_bottom_dis_name)
        danmaku_bottom_fast_dis_list.append(danmaku_bottom_dis_name)
        
        danmaku_right_p_name = f"danmaku_right_{i}_p"
        danmaku_right_dis_name = f"danmaku_right_{i}_dis"
        danmaku_right_slow_p[danmaku_right_p_name] = danmaku_start[2]
        danmaku_right_fast_p[danmaku_right_p_name] = danmaku_start[2]
        danmaku_right_slow_dis[danmaku_right_dis_name] = False
        danmaku_right_fast_dis[danmaku_right_dis_name] = False
        danmaku_right_slow_dis_list.append(danmaku_right_dis_name)
        danmaku_right_fast_dis_list.append(danmaku_right_dis_name)

        danmaku_left_p_name = f"danmaku_left_{i}_p"
        danmaku_left_dis_name = f"danmaku_left_{i}_dis"
        danmaku_left_slow_p[danmaku_left_p_name] = danmaku_start[3]
        danmaku_left_fast_p[danmaku_left_p_name] = danmaku_start[3]
        danmaku_left_slow_dis[danmaku_left_dis_name] = False
        danmaku_left_fast_dis[danmaku_left_dis_name] = False
        danmaku_left_slow_dis_list.append(danmaku_left_dis_name)
        danmaku_left_fast_dis_list.append(danmaku_left_dis_name)

        knife_top_p_name = f"knife_top_{i}_p"
        knife_top_dis_name = f"knife_top_{i}_dis"
        knife_top_p[knife_top_p_name] = knife_start[0]
        knife_top_dis[knife_top_dis_name] = False
        knife_top_dis_list.append(knife_top_dis_name)

        knife_bottom_p_name = f"knife_bottom_{i}_p"
        knife_bottom_dis_name = f"knife_bottom_{i}_dis"
        knife_bottom_p[knife_bottom_p_name] = knife_start[1]
        knife_bottom_dis[knife_bottom_dis_name] = False
        knife_bottom_dis_list.append(knife_bottom_dis_name)
        
        knife_right_p_name = f"knife_right_{i}_p"
        knife_right_dis_name = f"knife_right_{i}_dis"
        knife_right_p[knife_right_p_name] = knife_start[2]
        knife_right_dis[knife_right_dis_name] = False
        knife_right_dis_list.append(knife_right_dis_name)

        knife_left_p_name = f"knife_left_{i}_p"
        knife_left_dis_name = f"knife_left_{i}_dis"
        knife_left_p[knife_left_p_name] = knife_start[3]
        knife_left_dis[knife_left_dis_name] = False
        knife_left_dis_list.append(knife_left_dis_name)

        danmaku_slow_list.append(f"danmaku_slow_{i}")
        danmaku_fast_list.append(f"danmaku_fast_{i}")
        knife_list.append(f"knife_{i}")
      
      frame  = 0
      cmd_move = 2
      knifeshot = False
      snail = False
      snailcount = 0
      attack = False
      score = 0
      setting = False

    # システムイベントの検出
    for event in pg.event.get():
      if event.type == pg.QUIT: # ウィンドウ[X]の押下
        exit_flag = True
        exit_code = '001'
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_w:
          cmd_move = 0
        elif event.key == pg.K_d:
          cmd_move = 1
        elif event.key == pg.K_s:
          cmd_move = 2
        elif event.key == pg.K_a:
          cmd_move = 3
      if event.type == pg.MOUSEBUTTONDOWN:
        if event.button == 1:
          knifeshot = True
          print("True")
        if event.button == 3:
          print("False")
          if snail:
            snail = False
            while frame % 4 != 0:
              frame += 1
          else:
            snail = True

    score += 50

    # 能力と背景の処理
    if snail:
      screen.fill(pg.Color('#7d7d7d'))
      for x in range(0, disp_w, chip_s): # 縦線
        pg.draw.line(screen,grid_c,(x,0),(x,disp_h))
      for y in range(0, disp_h, chip_s): # 横線
        pg.draw.line(screen,grid_c,(0,y),(disp_w,y))
      screen.blit(font.render(f'Snail Meter {snailcount:05}',True,'WHITE'),(10,100))
      screen.blit(font.render(f'Score {score:09}',True,'WHITE'),(10,40))
      speed = 0.5
      if frame >= 6000:
        speed = 0.75
      snailcount -= 3
      frame += 1
      if snailcount <= 0:
        while frame % 4 != 0:
          frame += 1
        snail = False
    else:
      screen.fill(pg.Color('WHITE'))
      for x in range(0, disp_w, chip_s): # 縦線
        pg.draw.line(screen,grid_c,(x,0),(x,disp_h))
      for y in range(0, disp_h, chip_s): # 横線
        pg.draw.line(screen,grid_c,(0,y),(disp_w,y))
      screen.blit(font.render(f'Snail Meter {snailcount:05}',True,'BLACK'),(10,100))
      screen.blit(font.render(f'Score {score:09}',True,'BLACK'),(10,40))
      speed = 2
      if frame >= 6000:
        speed = 3
      snailcount += 1
      frame += 4

      # 自キャラの画像読込み    
    sakuya_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
    sakuya_d = 2 # 自キャラの向き
    sakuya_img_raw = pg.image.load('./sakuya.png')
    pose_p = pg.Vector2(0,32*cmd_move) # 前向き・2番目のポーズの位置　
    pose_s = pg.Vector2(24,32) # ポーズのサイズ
    tmp = sakuya_img_raw.subsurface(pg.Rect(pose_p,pose_s))
    sakuya_img = pg.transform.scale(tmp,sakuya_s) 


    # 自キャラの描画 dp:描画基準点（imgの左上座標）
    dp_sakuya = pg.Vector2(241,208)
    screen.blit(sakuya_img,dp_sakuya)

    dp_yousai_left = pg.Vector2(20,208)
    screen.blit(yousai_left_img,dp_yousai_left)

    dp_yousai_right = pg.Vector2(462,208)
    screen.blit(yousai_right_img,dp_yousai_right)

    dp_yousai_top = pg.Vector2(241,4)
    screen.blit(yousai_top_img,dp_yousai_top)

    dp_yousai_bottom = pg.Vector2(241,451)
    screen.blit(yousai_bottom_img,dp_yousai_bottom)


    if frame <= 2000:
      if frame % 120 == 0:
        attack = True
    elif frame <= 4000:
      if frame % 80 == 0:
        attack = True
    elif frame <= 8000:
      if frame % 60 == 0:
        attack = True
    else:
      if frame % 40 == 0:
        attack = True

    #弾幕の描画
    if attack:
      random = r.randint(0,100)
      attack = False
      if random <= 25:
        danmaku_top = True
      elif random <= 50:
        danmaku_bottom = True
      elif random <= 75:
        danmaku_left = True
      elif random <= 100:
        danmaku_right = True
    
    if danmaku_top:
      random_top = r.randint(1,2)
      if random_top == 1:
        for i in range(roop):
          if danmaku_top_slow_dis[danmaku_top_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_top_slow_dis[danmaku_top_slow_dis_list[i]] = True 
            danmaku_top = False
            break
      else:
        for i in range(roop):
          if danmaku_top_fast_dis[danmaku_top_fast_dis_list[i]] == False:
              danmaku_fast_list[i] = f"danmaku_fast_{frame}"
              danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
              danmaku_top_fast_dis[danmaku_top_fast_dis_list[i]] = True 
              danmaku_top = False
              break


    if danmaku_bottom:
      random_bottom = r.randint(1,2)
      if random_bottom == 1:
        for i in range(roop):
          if danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[i]] = True 
            danmaku_bottom = False
            break
      else:
        for i in range(roop):
          if danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[i]] == False:
            danmaku_fast_list[i] = f"danmaku_fast_{frame}"
            danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
            danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[i]] = True 
            danmaku_bottom = False
            break

    if danmaku_right:
      random_right = r.randint(1,2)
      if random_right == 1:
        for i in range(roop):
          if danmaku_right_slow_dis[danmaku_right_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_right_slow_dis[danmaku_right_slow_dis_list[i]] = True 
            danmaku_right = False
            break
      else:
        for i in range(roop):
          if danmaku_right_fast_dis[danmaku_right_fast_dis_list[i]] == False:
            danmaku_fast_list[i] = f"danmaku_fast_{frame}"
            danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
            danmaku_right_fast_dis[danmaku_right_fast_dis_list[i]] = True 
            danmaku_right = False
            break
    if danmaku_left:
      random_left = r.randint(1,2)
      if random_left == 1:
        for i in range(roop):
          if danmaku_left_slow_dis[danmaku_left_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_left_slow_dis[danmaku_left_slow_dis_list[i]] = True 
            danmaku_left = False
            break
      else:
        for i in range(roop):
          if danmaku_left_fast_dis[danmaku_left_fast_dis_list[i]] == False:
            danmaku_fast_list[i] = f"danmaku_fast_{frame}"
            danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
            danmaku_left_fast_dis[danmaku_left_fast_dis_list[i]] = True 
            danmaku_left = False
            break

    #自キャラの弾幕の描画
    if knifeshot:
      if cmd_move == 0:
        for i in range(roop):
          if knife_top_dis[knife_top_dis_list[i]] == False:
            knife_list[i] = f"knife_{frame}"
            knife[knife_list[i]] = Danmaku('./knife.png',(24,24))
            knife_top_dis[knife_top_dis_list[i]] = True 
            knifeshot = False
            break
      if cmd_move == 1:
        for i in range(roop):
          if knife_right_dis[knife_right_dis_list[i]] == False:
            knife_list[i] = f"knife_{frame}"
            knife[knife_list[i]] = Danmaku('./knife.png',(24,24))
            knife_right_dis[knife_right_dis_list[i]] = True 
            knifeshot = False
            break
      if cmd_move == 2:
        for i in range(roop):
          if knife_bottom_dis[knife_bottom_dis_list[i]] == False:
            knife_list[i] = f"knife_{frame}"
            knife[knife_list[i]] = Danmaku('./knife.png',(24,24))
            knife_bottom_dis[knife_bottom_dis_list[i]] = True 
            knifeshot = False
            break
      if cmd_move == 3:
        for i in range(roop):
          if knife_left_dis[knife_left_dis_list[i]] == False:
            knife_list[i] = f"knife_{frame}"
            knife[knife_list[i]] = Danmaku('./knife.png',(24,24))
            knife_left_dis[knife_left_dis_list[i]] = True 
            knifeshot = False
            break
    
    #弾幕の移動

    for i in range(roop):
      if danmaku_top_slow_dis[danmaku_top_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(0),danmaku_top_slow_p[f"danmaku_top_{i}_p"])
        danmaku_top_slow_p[f"danmaku_top_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(2,speed,danmaku_top_slow_p[f"danmaku_top_{i}_p"])
      if danmaku_top_fast_dis[danmaku_top_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(0),danmaku_top_fast_p[f"danmaku_top_{i}_p"])
        danmaku_top_fast_p[f"danmaku_top_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(2,speed*2,danmaku_top_fast_p[f"danmaku_top_{i}_p"])

      if danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(2),danmaku_bottom_slow_p[f"danmaku_bottom_{i}_p"])
        danmaku_bottom_slow_p[f"danmaku_bottom_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(0,speed,danmaku_bottom_slow_p[f"danmaku_bottom_{i}_p"])
      if danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(2),danmaku_bottom_fast_p[f"danmaku_bottom_{i}_p"])
        danmaku_bottom_fast_p[f"danmaku_bottom_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(0,speed*2,danmaku_bottom_fast_p[f"danmaku_bottom_{i}_p"])

      if danmaku_right_slow_dis[danmaku_right_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(1),danmaku_right_slow_p[f"danmaku_right_{i}_p"])
        danmaku_right_slow_p[f"danmaku_right_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(3,speed,danmaku_right_slow_p[f"danmaku_right_{i}_p"])
      if danmaku_right_fast_dis[danmaku_right_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(1),danmaku_right_fast_p[f"danmaku_right_{i}_p"])
        danmaku_right_fast_p[f"danmaku_right_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(3,speed*2,danmaku_right_fast_p[f"danmaku_right_{i}_p"])

      if danmaku_left_slow_dis[danmaku_left_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(3),danmaku_left_slow_p[f"danmaku_left_{i}_p"])
        danmaku_left_slow_p[f"danmaku_left_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(1,speed,danmaku_left_slow_p[f"danmaku_left_{i}_p"])
      if danmaku_left_fast_dis[danmaku_left_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(3),danmaku_left_fast_p[f"danmaku_left_{i}_p"])
        danmaku_left_fast_p[f"danmaku_left_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(1,speed*2,danmaku_left_fast_p[f"danmaku_left_{i}_p"])

      for i in range(roop):
        if knife_top_dis[knife_top_dis_list[i]]:
          screen.blit(knife[knife_list[i]].display(0),knife_top_p[f"knife_top_{i}_p"])
          knife_top_p[f"knife_top_{i}_p"] = knife[knife_list[i]].shot(0,speed,knife_top_p[f"knife_top_{i}_p"])
        
        if knife_right_dis[knife_right_dis_list[i]]:
          screen.blit(knife[knife_list[i]].display(3),knife_right_p[f"knife_right_{i}_p"])
          knife_right_p[f"knife_right_{i}_p"] =  knife[knife_list[i]].shot(1,speed,knife_right_p[f"knife_right_{i}_p"])

        if knife_bottom_dis[knife_bottom_dis_list[i]]:
          screen.blit(knife[knife_list[i]].display(2),knife_bottom_p[f"knife_bottom_{i}_p"])
          knife_bottom_p[f"knife_bottom_{i}_p"] =  knife[knife_list[i]].shot(2,speed,knife_bottom_p[f"knife_bottom_{i}_p"])

        if knife_left_dis[knife_left_dis_list[i]]:
          screen.blit(knife[knife_list[i]].display(1),knife_left_p[f"knife_left_{i}_p"])
          knife_left_p[f"knife_left_{i}_p"] =  knife[knife_list[i]].shot(3,speed,knife_left_p[f"knife_left_{i}_p"])

        for j in range(roop):
            if knife_top_p[f"knife_top_{i}_p"].distance_to(danmaku_top_slow_p[f"danmaku_top_{j}_p"]) < speed*1.5: 
              danmaku_top_slow_dis[danmaku_top_slow_dis_list[j]] = False
              danmaku_top_slow_p[f"danmaku_top_{j}_p"] = danmaku_start[0]
              knife_top_dis[knife_top_dis_list[i]] = False
              if knife_top_p[f"knife_top_{i}_p"] == knife_start[0]:
                exit_code = '002'
              knife_top_p[f"knife_top_{i}_p"] = knife_start[0]
              score += 4000

            if knife_top_p[f"knife_top_{i}_p"].distance_to(danmaku_top_fast_p[f"danmaku_top_{j}_p"]) < speed*1.5:
              danmaku_top_fast_dis[danmaku_top_fast_dis_list[j]] = False
              danmaku_top_fast_p[f"danmaku_top_{j}_p"] = danmaku_start[0]
              knife_top_dis[knife_top_dis_list[i]] = False
              if knife_top_p[f"knife_top_{i}_p"] == knife_start[0]:
                exit_code = '002'
              knife_top_p[f"knife_top_{i}_p"] = knife_start[0]
              score += 8000
            
            if knife_right_p[f"knife_right_{i}_p"].distance_to(danmaku_right_slow_p[f"danmaku_right_{j}_p"]) < speed*1.5: 
              danmaku_right_slow_dis[danmaku_right_slow_dis_list[j]] = False
              danmaku_right_slow_p[f"danmaku_right_{j}_p"] = danmaku_start[2]
              knife_right_dis[knife_right_dis_list[i]] = False
              if knife_right_p[f"knife_right_{i}_p"] == knife_start[2]:
                exit_code = '002'
              knife_right_p[f"knife_right_{i}_p"] = knife_start[2]

            if knife_right_p[f"knife_right_{i}_p"].distance_to(danmaku_right_fast_p[f"danmaku_right_{j}_p"]) < speed*1.5:
              danmaku_right_fast_dis[danmaku_right_fast_dis_list[j]] = False
              danmaku_right_fast_p[f"danmaku_right_{j}_p"] = danmaku_start[2]
              knife_right_dis[knife_right_dis_list[i]] = False
              if knife_right_p[f"knife_right_{i}_p"] == knife_start[2]:
                exit_code = '002'
              knife_right_p[f"knife_right_{i}_p"] = knife_start[2]
            
            if knife_bottom_p[f"knife_bottom_{i}_p"].distance_to(danmaku_bottom_slow_p[f"danmaku_bottom_{j}_p"]) < speed*1.5: 
              danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[j]] = False
              danmaku_bottom_slow_p[f"danmaku_bottom_{j}_p"] = danmaku_start[1]
              knife_bottom_dis[knife_bottom_dis_list[i]] = False
              if knife_bottom_p[f"knife_bottom_{i}_p"] == knife_start[1]:
                exit_code = '002'
              knife_bottom_p[f"knife_bottom_{i}_p"] = knife_start[1]

            if knife_bottom_p[f"knife_bottom_{i}_p"].distance_to(danmaku_bottom_fast_p[f"danmaku_bottom_{j}_p"]) < speed*1.5:
              danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[j]] = False
              danmaku_bottom_fast_p[f"danmaku_bottom_{j}_p"] = danmaku_start[1]
              knife_bottom_dis[knife_bottom_dis_list[i]] = False
              if knife_bottom_p[f"knife_bottom_{i}_p"] == knife_start[1]:
                exit_code = '002'
              knife_bottom_p[f"knife_bottom_{i}_p"] = knife_start[1]

            if knife_left_p[f"knife_left_{i}_p"].distance_to(danmaku_left_slow_p[f"danmaku_left_{j}_p"]) < speed*1.5: 
              danmaku_left_slow_dis[danmaku_left_slow_dis_list[j]] = False
              danmaku_left_slow_p[f"danmaku_left_{j}_p"] = danmaku_start[3]
              knife_left_dis[knife_left_dis_list[i]] = False
              if knife_left_p[f"knife_left_{i}_p"] == knife_start[3]:
                exit_code = '002'
              knife_left_p[f"knife_left_{i}_p"] = knife_start[3]

            if knife_left_p[f"knife_left_{i}_p"].distance_to(danmaku_left_fast_p[f"danmaku_left_{j}_p"]) < speed*1.5:
              danmaku_left_fast_dis[danmaku_left_fast_dis_list[j]] = False
              danmaku_left_fast_p[f"danmaku_left_{j}_p"] = danmaku_start[3]
              knife_left_dis[knife_left_dis_list[i]] = False
              if knife_left_p[f"knife_left_{i}_p"] == knife_start[3]:
                exit_code = '002'
              knife_left_p[f"knife_left_{i}_p"] = knife_start[3]

      screen.blit(font.render("True",exit_flag,'BLACK'),(10,10))
    

    while exit_code == '002':
      screen.fill(pg.Color('WHITE'))
      screen.blit(font_finish.render(f"Score {score}",True,'BLACK'),(170,200))
      screen.blit(font_key.render("Retry      SPACEkey",True,'BLACK'),(160,270))
      pg.display.update()
      for event in pg.event.get():
        if event.type == pg.QUIT:
          exit_flag = True
          exit_code = '001'
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_SPACE:
            exit_flag = False
            exit_code = '000'
            setting = True
    
    
    # 画面の更新と同期
    pg.display.update()
    clock.tick(30)

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')