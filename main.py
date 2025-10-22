@namespace
class SpriteKind:
    Building = SpriteKind.create()
    Props = SpriteKind.create()

def on_b_pressed():
    houseRed.set_image(assets.image("""
        houseRed
        """))
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile(sprite, location):
    sprites.destroy_all_sprites_of_kind(SpriteKind.Props)
    tiles.set_current_tilemap(tilemap("""
        level0
        """))
    setLevel1Props()
    tiles.place_on_tile(sprite,
        tiles.get_tiles_by_type(assets.tile("""
            tileHouseRed
            """))[0].get_neighboring_location(CollisionDirection.BOTTOM))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tileDoor1
        """),
    on_overlap_tile)

def on_a_pressed():
    houseRed.set_image(assets.image("""
        houseRed0
        """))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def setHouseRedProps():
    global prop
    prop = createProp(assets.image("""
            furnitureRug
            """),
        5,
        5,
        False,
        False)
    prop = createProp(assets.image("""
            furnitureTable2
            """),
        8,
        5,
        False,
        False)
    prop = createProp(assets.image("""
        couchSide1
        """), 12, 8, False, True)
    prop = createProp(assets.image("""
        bed2
        """), 4, 8, False, True)
def setHero():
    global hero
    hero = sprites.create(assets.image("""
            princessFront0
            """),
        SpriteKind.player)
    controller.move_sprite(hero)
    scene.camera_follow_sprite(hero)
    hero.z = 100
def createProp(propImage: Image, propCol: number, propRow: number, flipV: bool, flipH: bool):
    global prop
    if flipV:
        propImage.flip_y()
    elif flipH:
        propImage.flip_x()
    prop = sprites.create(propImage, SpriteKind.Props)
    tiles.place_on_tile(prop, tiles.get_tile_location(propCol, propRow))
    prop.x += (prop.width - 16) / 2
    prop.y += (prop.height - 16) / 2
    return prop

def on_overlap_tile2(sprite2, location2):
    sprites.destroy_all_sprites_of_kind(SpriteKind.Building)
    tiles.set_current_tilemap(tilemap("""
        levelRedHouse
        """))
    setHouseRedProps()
    tiles.place_on_tile(sprite2,
        tiles.get_tiles_by_type(assets.tile("""
            tileDoor1
            """))[0].get_neighboring_location(CollisionDirection.TOP))
    hero.z = 100
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tileHouseRed
        """),
    on_overlap_tile2)

def setLevel1Props():
    global houseRed, houseBlue
    houseRed = sprites.create(assets.image("""
        houseRed
        """), SpriteKind.Building)
    tiles.place_on_random_tile(houseRed, assets.tile("""
        tileHouseRed
        """))
    houseRed.y += -16
    houseBlue = sprites.create(assets.image("""
        houseBlue
        """), SpriteKind.Building)
    tiles.place_on_random_tile(houseBlue, assets.tile("""
        tileHouseBlue
        """))
    houseBlue.y += -16
heroDirection = ""
houseBlue: Sprite = None
hero: Sprite = None
prop: Sprite = None
houseRed: Sprite = None
tiles.set_current_tilemap(tilemap("""
    levelRedHouse
    """))
setHero()
setHouseRedProps()

def on_forever():
    global heroDirection
    if controller.up.is_pressed():
        if heroDirection != "up":
            animation.run_image_animation(hero,
                assets.animation("""
                    princessWalkBack
                    """),
                100,
                True)
        heroDirection = "up"
    elif controller.down.is_pressed():
        if heroDirection != "down":
            animation.run_image_animation(hero,
                assets.animation("""
                    princessWalkFront
                    """),
                100,
                True)
        heroDirection = "down"
    elif controller.right.is_pressed():
        if heroDirection != "right":
            animation.run_image_animation(hero,
                assets.animation("""
                    princessWalkRight
                    """),
                100,
                True)
        heroDirection = "right"
    elif controller.left.is_pressed():
        if heroDirection != "left":
            animation.run_image_animation(hero,
                assets.animation("""
                    princessWalkLeft
                    """),
                100,
                True)
        heroDirection = "left"
    else:
        animation.stop_animation(animation.AnimationTypes.ALL, hero)
        if heroDirection == "up":
            hero.set_image(assets.image("""
                princessBack0
                """))
        elif heroDirection == "down":
            hero.set_image(assets.image("""
                princessFront0
                """))
        elif heroDirection == "right":
            hero.set_image(assets.image("""
                princessRight0
                """))
        elif heroDirection == "left":
            hero.set_image(assets.image("""
                princessLeft0
                """))
        heroDirection = ""
forever(on_forever)
