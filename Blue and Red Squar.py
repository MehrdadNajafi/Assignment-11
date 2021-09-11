import arcade

arcade.Window(600,600,'Blue and Red Square')
arcade.set_background_color(arcade.color.WHITE)
red_circle = arcade.color.RED
blue_circle = arcade.color.BLUE
center_x=600 // 3
center_y=600 // 3
r = 8
arcade.start_render()
count=0

for i in range(10):
    for j in range(10):
        if i%2==0:
            if j%2==0:
                arcade.draw_circle_filled(center_x+count, center_y, r, red_circle)
            else:
                arcade.draw_circle_filled(center_x+count, center_y, r, blue_circle)
        else:
            if j%2==0:
                arcade.draw_circle_filled(center_x+count, center_y, r, blue_circle)
            else:
                arcade.draw_circle_filled(center_x+count, center_y, r, red_circle)
        count+=20
    count=0
    center_y+=20

arcade.finish_render()
arcade.run()
