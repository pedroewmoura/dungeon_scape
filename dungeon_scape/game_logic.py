import math

class Entity:
    def __init__(self, x, y, grid_size, offset_x, offset_y, prefix):
        self.grid_size = grid_size
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.prefix = prefix
        
        self.grid_x = x
        self.grid_y = y
        self.pos = [x * grid_size + offset_x, y * grid_size + offset_y]
        self.target_pos = [self.pos[0], self.pos[1]]
        
        self.frame = 1
        self.anim_timer = 0
        self.state = "idle"  # idle ou walk
        self.speed = 5

    def get_sprite(self):
        return f"{self.prefix}_{self.state}_{int(self.frame)}"

    def update_animation(self, dt):
        self.anim_timer += dt
        if self.anim_timer > 0.15:
            self.frame = (self.frame % 4) + 1
            self.anim_timer = 0

    def move_smoothly(self):
        moving = False
        for i in range(2):
            if abs(self.pos[i] - self.target_pos[i]) > self.speed:
                self.pos[i] += self.speed if self.target_pos[i] > self.pos[i] else -self.speed
                moving = True
            else:
                self.pos[i] = self.target_pos[i]
        
        self.state = "walk" if moving else "idle"

class Hero(Entity):
    def __init__(self, x, y, grid_size, offset_x, offset_y):
        super().__init__(x, y, grid_size, offset_x, offset_y, "hero")
        self.health = 7  # AJUSTADO PARA 7 VIDAS

    @property
    def grid_pos(self):
        return (self.grid_x, self.grid_y)

    def move(self, dx, dy):
        if self.pos == self.target_pos:
            new_x = self.grid_x + dx
            new_y = self.grid_y + dy
            if 0 <= new_x < 15 and 0 <= new_y < 11:
                self.grid_x = new_x
                self.grid_y = new_y
                self.target_pos = [new_x * self.grid_size + self.offset_x,
                                   new_y * self.grid_size + self.offset_y]

    def update(self, dt):
        self.move_smoothly()
        self.update_animation(dt)

    def collide_with(self, other):
        dist = math.sqrt((self.pos[0] - other.pos[0])**2 + (self.pos[1] - other.pos[1])**2)
        return dist < self.grid_size * 0.8

class Enemy(Entity):
    def __init__(self, x, y, patrol_points, grid_size, offset_x, offset_y):
        super().__init__(x, y, grid_size, offset_x, offset_y, "enemy")
        self.patrol_points = patrol_points
        self.current_patrol_idx = 0
        self.speed = 2

    def update(self, dt):
        if self.pos == self.target_pos:
            self.current_patrol_idx = (self.current_patrol_idx + 1) % len(self.patrol_points)
            tx, ty = self.patrol_points[self.current_patrol_idx]
            self.target_pos = [tx * self.grid_size + self.offset_x,
                               ty * self.grid_size + self.offset_y]
        self.move_smoothly()
        self.update_animation(dt)