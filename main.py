import pygame as pg
import random as r

class Danmaku:

  def __init__(self,img,size):
    self.img_raw = pg.image.load(img)
    self.size = pg.Vector2(size)

  def display(self):
    return pg.transform.scale(self.img_raw,self.size)

  def direction(self,dir):
    return pg.transform.rotate(self.img_raw, 90*dir)

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

  # 初期化処理
  chip_s = 48 # マップチップの基本サイズ
  map_s  = pg.Vector2(11,11) # マップの横・縦の配置数 

  pg.init() 
  pg.display.set_caption('ぼくのかんがえたさいきょうのげーむ II')
  disp_w = int(chip_s*map_s.x)
  disp_h = int(chip_s*map_s.y)
  screen = pg.display.set_mode((disp_w,disp_h))
  clock  = pg.time.Clock()
  font   = pg.font.Font(None,15)
  frame  = 0
  cmd_move = 2
  exit_flag = False
  exit_code = '000'

  # グリッド設定
  grid_c = '#bbbbbb'
  
  for event in pg.event.get():
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_w:
          cmd_move = 0
        elif event.key == pg.K_a:
          cmd_move = 1
        elif event.key == pg.K_s:
          cmd_move = 2
        elif event.key == pg.K_d:
          cmd_move = 3

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
  danmaku_slow = {}
  danmaku_fast = {}
  danmaku_slow_list = []
  danmaku_fast_list = []

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

  for i in range(4):
    danmaku_top_p_name = f"danmaku_top_{i}_p"
    danmaku_top_dis_name = f"danmaku_top_{i}_dis"
    danmaku_top_slow_p[danmaku_top_p_name] = pg.Vector2(60,228)
    danmaku_top_fast_p[danmaku_top_p_name] = pg.Vector2(60,228)
    danmaku_top_slow_dis[danmaku_top_dis_name] = False
    danmaku_top_fast_dis[danmaku_top_dis_name] = False
    danmaku_top_slow_dis_list.append(danmaku_top_dis_name)
    danmaku_top_fast_dis_list.append(danmaku_top_dis_name)

    danmaku_bottom_p_name = f"danmaku_bottom_{i}_p"
    danmaku_bottom_dis_name = f"danmaku_bottom_{i}_dis"
    danmaku_bottom_slow_p[danmaku_bottom_p_name] = pg.Vector2(253,420)
    danmaku_bottom_fast_p[danmaku_bottom_p_name] = pg.Vector2(253,420)
    danmaku_bottom_slow_dis[danmaku_bottom_dis_name] = False
    danmaku_bottom_fast_dis[danmaku_bottom_dis_name] = False
    danmaku_bottom_slow_dis_list.append(danmaku_bottom_dis_name)
    danmaku_bottom_fast_dis_list.append(danmaku_bottom_dis_name)
    
    danmaku_right_p_name = f"danmaku_right_{i}_p"
    danmaku_right_dis_name = f"danmaku_right_{i}_dis"
    danmaku_right_slow_p[danmaku_right_p_name] = pg.Vector2(443,228)
    danmaku_right_fast_p[danmaku_right_p_name] = pg.Vector2(443,228)
    danmaku_right_slow_dis[danmaku_right_dis_name] = False
    danmaku_right_fast_dis[danmaku_right_dis_name] = False
    danmaku_right_slow_dis_list.append(danmaku_right_dis_name)
    danmaku_right_fast_dis_list.append(danmaku_right_dis_name)

    danmaku_slow_list.append(f"danmaku_slow_{i}")
    danmaku_fast_list.append(f"danmaku_fast_{i}")

  # ゲームループ
  while not exit_flag:

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

    # 背景描画
    screen.fill(pg.Color('WHITE'))

    # グリッド
    for x in range(0, disp_w, chip_s): # 縦線
      pg.draw.line(screen,grid_c,(x,0),(x,disp_h))
    for y in range(0, disp_h, chip_s): # 横線
      pg.draw.line(screen,grid_c,(0,y),(disp_w,y))

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

    dp_yousai_top = pg.Vector2(241,3)
    screen.blit(yousai_top_img,dp_yousai_top)

    dp_yousai_bottom = pg.Vector2(241,451)
    screen.blit(yousai_bottom_img,dp_yousai_bottom)
    # フレームカウンタの描画
    frame += 1
    frm_str = f'{frame:05}'
    cmd_move_str = f'{cmd_move:02}'
    screen.blit(font.render(frm_str,True,'BLACK'),(10,10))
    screen.blit(font.render(cmd_move_str,True,'BLACK'),(10,30))

    #弾幕の描画
    if frame%30 == 0:
      random = r.randint(0,100)
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
        for i in range(4):
          if danmaku_top_slow_dis[danmaku_top_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_top_slow_dis[danmaku_top_slow_dis_list[i]] = True 
            danmaku_top = False
            break
      else:
        for i in range(4):
          if danmaku_top_fast_dis[danmaku_top_fast_dis_list[i]] == False:
              danmaku_fast_list[i] = f"danmaku_fast_{frame}"
              danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
              danmaku_top_fast_dis[danmaku_top_fast_dis_list[i]] = True 
              danmaku_top = False
              break


    if danmaku_bottom:
      random_bottom = r.randint(1,2)
      if random_bottom == 1:
        for i in range(4):
          if danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[i]] = True 
            danmaku_bottom = False
            break
      else:
        for i in range(4):
          if danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[i]] == False:
            danmaku_fast_list[i] = f"danmaku_fast_{frame}"
            danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
            danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[i]] = True 
            danmaku_bottom = False
            break

    if danmaku_right:
      random_right = r.randint(1,2)
      if random_right == 1:
        for i in range(4):
          if danmaku_right_slow_dis[danmaku_right_slow_dis_list[i]] == False:
            danmaku_slow_list[i] = f"danmaku_slow_{frame}"
            danmaku_slow[danmaku_slow_list[i]] = Danmaku('./danmaku_yellow.png',(24,24))
            danmaku_right_slow_dis[danmaku_right_slow_dis_list[i]] = True 
            danmaku_right = False
            break
      else:
        for i in range(4):
          if danmaku_right_fast_dis[danmaku_right_fast_dis_list[i]] == False:
            danmaku_fast_list[i] = f"danmaku_fast_{frame}"
            danmaku_fast[danmaku_fast_list[i]] = Danmaku('./danmaku_red.png',(24,24))
            danmaku_right_fast_dis[danmaku_right_fast_dis_list[i]] = True 
            danmaku_right = False
            break

    for i in range(4):
      if danmaku_top_slow_dis[danmaku_top_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(),danmaku_top_slow_p[f"danmaku_top_{i}_p"])
        danmaku_top_slow_p[f"danmaku_top_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(1,speed,danmaku_top_slow_p[f"danmaku_top_{i}_p"])
      if danmaku_top_fast_dis[danmaku_top_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(),danmaku_top_fast_p[f"danmaku_top_{i}_p"])
        danmaku_top_fast_p[f"danmaku_top_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(1,speed*2,danmaku_top_fast_p[f"danmaku_top_{i}_p"])

      if danmaku_bottom_slow_dis[danmaku_bottom_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(),danmaku_bottom_slow_p[f"danmaku_bottom_{i}_p"])
        danmaku_bottom_slow_p[f"danmaku_bottom_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(0,speed,danmaku_bottom_slow_p[f"danmaku_bottom_{i}_p"])
      if danmaku_bottom_fast_dis[danmaku_bottom_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(),danmaku_bottom_fast_p[f"danmaku_bottom_{i}_p"])
        danmaku_bottom_fast_p[f"danmaku_bottom_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(0,speed*2,danmaku_bottom_fast_p[f"danmaku_bottom_{i}_p"])

      if danmaku_right_slow_dis[danmaku_right_slow_dis_list[i]]:
        screen.blit(danmaku_slow[danmaku_slow_list[i]].display(),danmaku_right_slow_p[f"danmaku_right_{i}_p"])
        danmaku_right_slow_p[f"danmaku_right_{i}_p"] = danmaku_slow[danmaku_slow_list[i]].shot(3,speed,danmaku_right_slow_p[f"danmaku_right_{i}_p"])
      if danmaku_right_fast_dis[danmaku_right_fast_dis_list[i]]:
        screen.blit(danmaku_fast[danmaku_fast_list[i]].display(),danmaku_right_fast_p[f"danmaku_right_{i}_p"])
        danmaku_right_fast_p[f"danmaku_right_{i}_p"] = danmaku_fast[danmaku_fast_list[i]].shot(3,speed*2,danmaku_right_fast_p[f"danmaku_right_{i}_p"])

      
    random_str = f'{random:03}'
    screen.blit(font.render(random_str,True,'BLACK'),(10,50))
    if danmaku_top:
      screen.blit(font.render("True",True,'BLACK'),(10,70))
    if danmaku_bottom:
      screen.blit(font.render("True",True,'BLACK'),(10,90))
    
    
    # 画面の更新と同期
    pg.display.update()
    clock.tick(30)

  # ゲームループ [ここまで]
  pg.quit()
  return exit_code

if __name__ == "__main__":
  code = main()
  print(f'プログラムを「コード{code}」で終了しました。')