def on_up_pressed():
    global direction
    direction = 0
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f f 2 f e f . . 
                        . . f f f 2 f e e 2 2 f f f . . 
                        . . f e 2 f f e e 2 f e e f . . 
                        . f f e f f e e e f e e e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . . e f f f f f f f f 4 e . . 
                        . . . 4 f 2 2 2 2 2 e d d 4 . . 
                        . . . e f f f f f f e e 4 . . . 
                        . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . f f f f f 2 2 f f f f f . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e 2 f 2 f f 2 f 2 e f . . 
                        . . f f f 2 2 e e 2 2 f f f . . 
                        . f f e f 2 f e e f 2 f e f f . 
                        . f e e f f e e e e f e e e f . 
                        . . f e e e e e e e e e e f . . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f e e e e f f . . . . 
                        . . . f e e e f f e e e f . . . 
                        . . . f f f f 2 2 f f f f . . . 
                        . . f f e 2 e 2 2 e 2 e f f . . 
                        . . f e f 2 f f f 2 f 2 e f . . 
                        . . f f f 2 2 e e f 2 f f f . . 
                        . . f e e f 2 e e f f 2 e f . . 
                        . f f e e e f e e e f f e f f . 
                        . f f e e e e e e e e e e f f . 
                        . . . f e e e e e e e e f . . . 
                        . . e 4 f f f f f f f f e . . . 
                        . . 4 d d e 2 2 2 2 2 f 4 . . . 
                        . . . 4 e e f f f f f f e . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    attack(direction)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global direction
    direction = 3
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d e e e e e f . . . 
                        . . . f e 4 e d d 4 f . . . . . 
                        . . . f 2 2 e d d e f . . . . . 
                        . . f f 5 5 f e e f f f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """),
            img("""
                . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e e f f . . . . 
                        . . . f 2 2 2 e d d 4 . . . . . 
                        . . . f 2 2 2 e d d e . . . . . 
                        . . . f 5 5 4 f e e f . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . . . . f f f . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f . . . . . . 
                        . . . f 2 f e e e e f f . . . . 
                        . . f 2 2 2 f e e e e f f . . . 
                        . . f e e e e f f e e e f . . . 
                        . f e 2 2 2 2 e e f f f f . . . 
                        . f 2 e f f f f 2 2 2 e f . . . 
                        . f f f e e e f f f f f f f . . 
                        . f e e 4 4 f b e 4 4 e f f . . 
                        . . f e d d f 1 4 d 4 e e f . . 
                        . . . f d d d d 4 e e e f . . . 
                        . . . f e 4 4 4 e d d 4 . . . . 
                        . . . f 2 2 2 2 e d d e . . . . 
                        . . f f 5 5 4 4 f e e f . . . . 
                        . . f f f f f f f f f f . . . . 
                        . . . f f f . . . f f . . . . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def attack(num: number):
    global attacking
    attacking = True
    if num == 0:
        animation.run_image_animation(mySprite, assets.animation("""
            boyAnim
        """), 100, True)
    elif num == 1:
        animation.run_image_animation(mySprite, assets.animation("""
            myAnim0
        """), 100, True)
    elif num == 2:
        animation.run_image_animation(mySprite, assets.animation("""
            attack2
        """), 100, True)
    elif num == 3:
        animation.run_image_animation(mySprite,
            assets.animation("""
                attackAnim
            """),
            100,
            True)
    else:
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
        mySprite.set_image(img("""
            ........................
                        .....ffff...............
                        ...fff22fff.............
                        ..fff2222fff............
                        .fffeeeeeefff...........
                        .ffe222222eef...........
                        .fe2ffffff2ef...........
                        .ffffeeeeffff...........
                        ffefbf44fbfeff..........
                        fee41fddf14eef..........
                        .ffffdddddeef...........
                        fddddf444eef............
                        fbbbbf2222f4e...........
                        fbbbbf2222fd4...........
                        .fccf45544f44...........
                        ..ffffffff..............
                        ....ff..ff..............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
        """))

def on_right_pressed():
    global direction
    direction = 1
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e e e d d d f . . . 
                        . . . . . f 4 d d e 4 e f . . . 
                        . . . . . f e d d e 2 2 f . . . 
                        . . . . f f f e e f 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """),
            img("""
                . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . f f e e 4 4 4 e f . . . 
                        . . . . . 4 d d e 2 2 2 f . . . 
                        . . . . . e d d e 2 2 2 f . . . 
                        . . . . . f e e f 4 5 5 f . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . . . . f f f . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f f f . . . . 
                        . . . . f f e e e e f 2 f . . . 
                        . . . f f e e e e f 2 2 2 f . . 
                        . . . f e e e f f e e e e f . . 
                        . . . f f f f e e 2 2 2 2 e f . 
                        . . . f e 2 2 2 f f f f e 2 f . 
                        . . f f f f f f f e e e f f f . 
                        . . f f e 4 4 e b f 4 4 e e f . 
                        . . f e e 4 d 4 1 f d d e f . . 
                        . . . f e e e 4 d d d d f . . . 
                        . . . . 4 d d e 4 4 4 e f . . . 
                        . . . . e d d e 2 2 2 2 f . . . 
                        . . . . f e e f 4 4 5 5 f f . . 
                        . . . . f f f f f f f f f f . . 
                        . . . . . f f . . . f f f . . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_a_released():
    global attacking
    attack(4)
    attacking = False
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_down_pressed():
    global direction
    direction = 2
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . .
                . . . . . . f f f f . . . . . .
                . . . . f f f 2 2 f f f . . . .
                . . . f f f 2 2 2 2 f f f . . .
                . . f f f e e e e e e f f f . .
                . . f f e 2 2 2 2 2 2 e e f . .
                . f f e 2 f f f f f f 2 e f f .
                . f f f f f e e e e f f f f f .
                . . f e f b f 4 4 f b f e f . .
                . . f e 4 1 f d d f 1 4 e f . .
                . . . f e 4 d d d d 4 e f e . .
                . . f e f 2 2 2 2 e d d 4 e . .
                . . e 4 f 2 2 2 2 e d d e . . .
                . . . . f 4 4 5 5 f e e . . . .
                . . . . f f f f f f f . . . . .
                . . . . f f f . . . . . . . . .
            """),
            img("""
                . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f f e 2 2 2 2 2 2 e e f . . 
                        . . f e 2 f f f f f f 2 e f . . 
                        . . f f f f e e e e f f f f . . 
                        . f f e f b f 4 4 f b f e f f . 
                        . f e e 4 1 f d d f 1 4 e e f . 
                        . . f e e d d d d d d e e f . . 
                        . . . f e e 4 4 4 4 e e f . . . 
                        . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                        . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                        . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                        . . . . . f f f f f f . . . . . 
                        . . . . . f f . . f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . f f f f . . . . . . 
                        . . . . f f f 2 2 f f f . . . . 
                        . . . f f f 2 2 2 2 f f f . . . 
                        . . f f f e e e e e e f f f . . 
                        . . f e e 2 2 2 2 2 2 e f f . . 
                        . f f e 2 f f f f f f 2 e f f . 
                        . f f f f f e e e e f f f f f . 
                        . . f e f b f 4 4 f b f e f . . 
                        . . f e 4 1 f d d f 1 4 e f . . 
                        . . e f e 4 d d d d 4 e f . . . 
                        . . e 4 d d e 2 2 2 2 f e f . . 
                        . . . e d d e 2 2 2 2 f 4 e . . 
                        . . . . e e f 5 5 4 4 f . . . . 
                        . . . . . f f f f f f f . . . . 
                        . . . . . . . . . f f f . . . .
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

direction = 0
attacking = False
mySprite: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . 1 1 1 1 . . . . . . 
            . . . . 1 1 3 8 8 3 1 1 . . . . 
            . . . 1 3 8 8 8 8 8 8 3 1 . . . 
            . . 1 3 8 8 8 e 4 8 8 8 3 1 . . 
            . . 1 8 8 4 8 4 e 8 4 8 8 1 . . 
            . . 1 8 8 8 8 8 8 8 8 8 8 1 . . 
            . . 1 3 3 3 3 3 3 3 3 3 3 1 . . 
            . 1 1 c 1 1 c c c c 1 1 c 1 1 . 
            . 1 5 c a 1 c c c c a 1 c 5 1 . 
            . . 1 5 c c c 5 5 c c c 5 1 . . 
            . . . 1 5 c c c c c c 5 1 . . . 
            . . 1 1 1 5 5 5 5 5 5 1 1 1 . . 
            . . 1 c 1 4 4 4 4 4 4 1 c 1 . . 
            . . 1 1 1 4 4 4 4 4 4 1 1 1 . . 
            . . . . . 1 1 1 1 1 1 . . . . . 
            . . . . . 1 1 . . 1 1 . . . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(mySprite)
attacking = False
direction = 2
controller.move_sprite(mySprite, 50, 50)
mySprite.set_stay_in_screen(True)
tiles.set_tilemap(tilemap("""
    level1
"""))
monster = sprites.create(assets.tile("""
    myTile
"""), SpriteKind.enemy)
tiles.place_on_random_tile(monster, assets.tile("""
    myTile0
"""))
animation.run_image_animation(monster, assets.animation("""
    myAnim
"""), 100, True)

def on_on_update():
    if mySprite.overlaps_with(monster) and attacking:
        monster.say("OUUCH!!!!", 500)
        monster.x = mySprite.x - 100
        monster.set_bounce_on_wall(True)
        monster.set_stay_in_screen(True)
game.on_update(on_on_update)
