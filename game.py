import window as wind
import player

class Game:
    def __init__(self) -> None:
        self.window = wind.Window("600x600", "PONG GAME")
        self.canvas = self.window.getCanvas()
        
        # Create player 1
        self.player1 = player.Player(30, 300, 45, 350, 'white', 0, 3)
        self.canvas_player1 = self.canvas.create_rectangle(self.player1.get_initial_x(), self.player1.get_initial_y(),
                                     self.player1.get_final_x(), self.player1.get_final_y(),
                                     fill=self.player1.get_color())
        
        # Create player 2
        self.player2 = player.Player(555, 300, 570, 350, 'white', 0, 3)
        self.canvas_player2 = self.canvas.create_rectangle(self.player2.get_initial_x(), self.player2.get_initial_y(),
                                     self.player2.get_final_x(), self.player2.get_final_y(),
                                     fill=self.player2.get_color())
        # Create Ball        
        initial_y_ball = (self.player1.get_final_y() - self.player1.get_initial_y()) // 2 + self.player1.get_initial_y()
        self.ball = player.Ball(300, initial_y_ball, 310, initial_y_ball + 10, 'red', -4, 3)
        self.canvas_ball = self.canvas.create_rectangle(self.ball.get_initial_x(), initial_y_ball,
                                     self.ball.get_final_x(), self.ball.get_final_y(),
                                     fill=self.ball.get_color())
        self.movement()
        
    def update_player_coords(self, player: player.Player, coords: list):
        player.set_initial_x(coords[0])
        player.set_initial_y(coords[1])
        player.set_final_x(coords[2])
        player.set_final_y(coords[3])
    
    def movement(self):
        #Move ball
        self.canvas.move(self.canvas_ball, self.ball.get_speed_x(), self.ball.get_speed_y())
        # Get coordinates of the ball -> [x1, y1, x2, y2]
        ball_pos = self.canvas.coords(self.canvas_ball)
        # Get coordinates of the players -> [x1, y1, x2, y2]
        player1_pos = self.canvas.coords(self.canvas_player1)
        player2_pos = self.canvas.coords(self.canvas_player2)
        #Update players Coords
        self.update_player_coords(self.player1, player1_pos)
        self.update_player_coords(self.player2, player2_pos)
        self.update_player_coords(self.ball, ball_pos)
        
        # Ball limits
        if ball_pos[2] >= 600 or ball_pos[0] <= 0:
            self.ball.set_speed_x(self.ball.get_speed_x() * -1)
            
        if ball_pos[3] >= 600 or ball_pos[1] <= 0:
            self.ball.set_speed_y(self.ball.get_speed_y() * -1) 
            
        # Ball hitting any player
        if ball_pos[0] <= player1_pos[2] and player1_pos[1] <= ball_pos[1] <= player1_pos[3]:
            self.ball.set_speed_x(self.ball.get_speed_x() * -1)
        
        if ball_pos[2] >= player2_pos[0] and player2_pos[1] <= ball_pos[1] <= player2_pos[3]:
            self.ball.set_speed_x(self.ball.get_speed_x() * -1)
            
        #Player1 movement
        player_middle = (self.player1.get_final_y() - self.player1.get_initial_y()) // 2
        if player1_pos[1] + player_middle > ball_pos[1]:
            if player1_pos[1] >= 0:
                self.player1.set_speed_y(self.player1.get_speed_y() - 3)
                self.canvas.move(self.canvas_player1, 0, self.player1.get_speed_y())
        
        if player1_pos[1] + player_middle < ball_pos[1]:
            if player1_pos[3] <= 600:
                self.player1.set_speed_y(self.player1.get_speed_y() + 3)
                self.canvas.move(self.canvas_player1, 0, self.player1.get_speed_y())
        #Player2 movement
        if player2_pos[1] + player_middle > ball_pos[1]:
            if player2_pos[1] >= 0:
                self.player2.set_speed_y(self.player2.get_speed_y() - 3)
                self.canvas.move(self.canvas_player2, 0, self.player2.get_speed_y())
        
        if player2_pos[1] + player_middle < ball_pos[1]:
            if player2_pos[3] <= 600:
                self.player2.set_speed_y(self.player2.get_speed_y() + 3)
                self.canvas.move(self.canvas_player2, 0, self.player2.get_speed_y())
        self.canvas.after(40, self.movement)

    def play_game(self):
        self.window.start_execution()