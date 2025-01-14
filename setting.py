import pygame as pg

def setting():
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
  yousai_left_d = 2 # 自キャラの向き
  yousai_left_raw = pg.image.load('./yousei.png')
  yousai_left_p = pg.Vector2(24,32) # 前向き・2番目のポーズの位置　
  yousai_left_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_left_tmp = yousai_left_raw.subsurface(pg.Rect(yousai_left_p,yousai_left_pose_s))
  yousai_left_img = pg.transform.scale(yousai_left_tmp,yousai_left_s) 

  yousai_right_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_right_d = 2 # 自キャラの向き
  yousai_right_raw = pg.image.load('./yousei.png')
  yousai_right_p = pg.Vector2(96,96) # 前向き・2番目のポーズの位置　
  yousai_right_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_right_tmp = yousai_right_raw.subsurface(pg.Rect(yousai_right_p,yousai_right_pose_s))
  yousai_right_img = pg.transform.scale(yousai_right_tmp,yousai_right_s) 
  
  yousai_top_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_top_d = 2 # 自キャラの向き
  yousai_top_raw = pg.image.load('./yousei.png')
  yousai_top_p = pg.Vector2(96,192) # 前向き・2番目のポーズの位置　
  yousai_top_pose_s = pg.Vector2(24,32) # ポーズのサイズ
  yousai_top_tmp = yousai_top_raw.subsurface(pg.Rect(yousai_top_p,yousai_top_pose_s))
  yousai_top_img = pg.transform.scale(yousai_top_tmp,yousai_top_s) 

  yousai_bottom_s = pg.Vector2(48,64) # 画面に出力する自キャラサイズ 48x64
  yousai_bottom_d = 2 # 自キャラの向き
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
  danmaku_top_slow_p = {}
  danmaku_top_fast_p = {}
  danmaku_top_slow_dis = {}
  danmaku_top_fast_dis = {}
  danmaku_bottom_slow_dis = {}
  danmaku_bottom_fast_dis = {}

  for i in range(4):
    danmaku_top_p_name = f"danmaku_top_{i}_p"
    danmaku_top_dis_name = f"danmaku_top_{i}_dis"
    danmaku_bottom_dis_name = f"danmaku_top_{i}_dis"

    danmaku_top_slow_p[danmaku_top_p_name] = pg.Vector2(60,228)
    danmaku_top_fast_p[danmaku_top_p_name] = pg.Vector2(60,228)
    danmaku_top_slow_dis[danmaku_top_dis_name] = False
    danmaku_top_fast_dis[danmaku_top_dis_name] = False
    danmaku_bottom_slow_dis[danmaku_bottom_dis_name] = False
    danmaku_bottom_fast_dis[danmaku_bottom_dis_name] = False
