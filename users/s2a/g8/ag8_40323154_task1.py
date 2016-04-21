# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag8_40323154 = Blueprint('ag8_40323154', __name__, url_prefix='/ag8_40323154', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag8_40323154.route('/task1')
def task1():
    outstring = '''

from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -400, 500, 500) 

# 決定要不要畫座標軸線
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(170)
    basic2 = cmbr.dup()
    basic2.rotate(160)
    basic2.translate(3.65, 20)
    
    basic3 = cmbr.dup()
    basic3.rotate(90)
    basic3.translate(11, 39)
    
    basic4 = cmbr.dup()
    basic4.rotate(20)
    basic4.translate(31, 39)
    
    basic5 = cmbr.dup()
    basic5.rotate(15)
    basic5.translate(38, 20)
    
    basic6 = cmbr.dup()
    basic6.rotate(180)
    basic6.translate(50*math.cos(30*deg), -13*math.sin(30*deg)-13)
    
    basic7 = cmbr.dup()
    basic7.rotate(90)
    basic7.translate(20*math.cos(30*deg), -20*math.sin(30*deg)-20)
    
    basic8 = cmbr.dup()
    basic8.rotate(90)
    basic8.translate(0,0)
    
    basic9 = cmbr.dup()
    basic9.rotate(91.5)
    basic9.translate(23.5,0)

    cmbr.appendPath(basic3)

    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 0, 0, 0, 0, "green", True, 4)




from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-325
, -400, 500, 500) 

# 決定要不要畫座標軸線

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 =  cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(120)
    basic1.translate(21, 20)
    
    basic2 = cmbr.dup()
    basic2.rotate(90)
    basic2.translate(0, -20)
    
    basic3 = basic2.dup()
    basic3.rotate(90)
    basic3.translate(-20, 0)
    
    basic4 = cmbr.dup()
    basic4.rotate(120)
    basic4.translate(24*math.cos(30*deg), -13.25*math.sin(30*deg)-13.25)
    
    basic5 = cmbr.dup()
    basic5.translate(2.20*20*math.cos(30*deg), 10)
    
    basic6 = basic3.dup()
    basic6.rotate(0)
    basic6.translate(0, 20)
    
    basic7 = basic6.dup()
    basic7.rotate(90)
    basic7.translate(40,20)
    
    basic8 = basic7.dup()
    basic8.rotate(-30)
    basic8.translate(11,2.5)
    
    basic9 = cmbr.dup()
    basic9.rotate(0)
    basic9.translate(0,60)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(0,60)
    
    basic11 = basic10.dup()
    basic11.rotate(-30)
    basic11.translate(-10,8)
    
    basic12 = cmbr.dup()
    basic12.rotate(2.5)
    basic12.translate(37.5,50)
    
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)

    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 0, 0, 0, 0, "green", True, 4)



from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-400, -415, 500, 500) 

# 決定要不要畫座標軸線

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(180)
    basic2 = cmbr.dup()
    basic2.rotate(30)
    basic2.translate(0, -20)
    
    basic3 = basic2.dup()
    basic3.rotate(120)
    basic3.translate(-17.5,10)
    
    basic4 = cmbr.dup()
    basic4.rotate(70)
    basic4.translate(11.5*math.cos(30*deg), -25*math.sin(30*deg)-25)
    
    basic5 = cmbr.dup()
    basic5.rotate(90)
    basic5.translate(1.7*20*math.cos(30*deg), -44.5)
    
    basic6 = basic3.dup()
    basic6.rotate(-30)
    basic6.translate(0,20)
    
    basic7 = cmbr.dup()
    basic7.rotate(90)
    basic7.translate(27.5,47.5)
    
    cmbr.appendPath(basic5)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y,  0.85, rot)

O(0, 0, 0, 0, 0, "green", True, 4)

from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(180)
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, -20)
    
    basic3 = basic1.dup()
    basic3.rotate(180)
    basic3.translate(0,40)
    
    basic4 = basic3.dup()
    basic4.rotate(-90)
    basic4.translate(-20,40)
    
    basic5 = basic2.dup()
    basic5.rotate(90)
    basic5.translate(-20,-40)
    
    basic6 = basic5.dup()
    basic6.rotate(30)
    basic6.translate(0,-5)
    
    basic7 = basic4.dup()
    basic7.rotate(-30)
    basic7.translate(0,5)
    
    basic8 = basic7.dup()
    basic8.rotate(-50)
    basic8.translate(-6,19.5)
    
    basic9 = basic6.dup()
    basic9.rotate(50)
    basic9.translate(-6,-19.5)
    
    basic10 = basic9.dup()
    basic10.rotate(10)
    basic10.translate(-1,12.5)
    
    cmbr.appendPath(basic10)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 0, 0, 0, 0, "green", True, 4)

from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-325, -250, 500, 500) 

# 決定要不要畫座標軸線

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(180)
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, -20)
    
    basic3 = basic1.dup()
    basic3.rotate(180)
    basic3.translate(0,40)
    
    basic4 = basic3.dup()
    basic4.rotate(-90)
    basic4.translate(-20,40)
    
    basic5 = basic2.dup()
    basic5.rotate(90)
    basic5.translate(-20,-40)
    
    basic6 = basic5.dup()
    basic6.rotate(0)
    basic6.translate(20,0)
    
    basic7 = basic4.dup()
    basic7.rotate(0)
    basic7.translate(20,0)
    
    basic8 = basic7.dup()
    basic8.rotate(0)
    basic8.translate(20,0)
    
    basic9 = basic6.dup()
    basic9.rotate(0)
    basic9.translate(20,0)
    
    basic10 = basic1.dup()
    basic10.rotate(-90)
    basic10.translate(0,0)
    
    cmbr.appendPath(basic10)

    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1, rot)

O(0, 0, 0, 0, 0, "green", True, 4)

from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-500, -250, 600, 500) 

# 決定要不要畫座標軸線

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth  })

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(180)
    basic2 = cmbr.dup()
    basic2.rotate(0)
    basic2.translate(0, -20)
    
    basic3 = basic1.dup()
    basic3.rotate(180)
    basic3.translate(0,40)
    
    basic4 = basic3.dup()
    basic4.rotate(-90)
    basic4.translate(-20,40)
    
    basic7 = basic4.dup()
    basic7.rotate(0)
    basic7.translate(20,0)
    
    basic8 = basic7.dup()
    basic8.rotate(0)
    basic8.translate(20,0)
    
    basic10 = basic1.dup()
    basic10.rotate(-90)
    basic10.translate(0,0)
    
    cmbr.appendPath(basic10)

    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 1.25, rot)

O(0, 0, 0, 0, 0, "green", True, 4)
'''
    return outstring
    

    
    
