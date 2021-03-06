# Board used for start-up drawing of the board
# note - this is using Square list method (see https://en.wikipedia.org/wiki/Board_representation_(computer_chess))
# TODO - rename this from fen to just settings?






linear_dirs = [-10, -1, 10, 1]
diagonal_dirs = [-11, -9, 9, 11]
knight_moves = [-21, -19, -12, -8, 8, 12, 19, 21]  # Up-up-left, up-up-right ......

opposite_dir_dict = {-10: 10,
                     10: -10,
                     -1: 1,
                     1: -1,
                     -11: 9,
                     9: -11,
                     -9: 11,
                     11: -9}


diagonals = [9, 11]
up = 10
board_square_count = 120  # 12x10
valid_pieces = 'pNBRQK'
valid_colors = 'wb'

start_board = {0: 'FF',   1: 'FF',   2: 'FF',   3: 'FF',   4: 'FF',   5: 'FF',   6: 'FF',   7: 'FF',   8: 'FF',   9: 'FF',   # [  0,   1,   2,   3,   4,   5,   6,   7,   8,   9]
              10: 'FF',  11: 'FF',  12: 'FF',  13: 'FF',  14: 'FF',  15: 'FF',  16: 'FF',  17: 'FF',  18: 'FF',  19: 'FF',   # [ 10,  11,  12,  13,  14,  15,  16,  17,  18,  19]
              20: 'FF',  21: 'bR',  22: 'bN',  23: 'bB',  24: 'bQ',  25: 'bK',  26: 'bB',  27: 'bN',  28: 'bR',  29: 'FF',   # [ 20,  21,  22,  23,  24,  25,  26,  27,  28,  29]
              30: 'FF',  31: 'bp',  32: 'bp',  33: 'bp',  34: 'bp',  35: 'bp',  36: 'bp',  37: 'bp',  38: 'bp',  39: 'FF',   # [ 30,  31,  32,  33,  34,  35,  36,  37,  38,  39]
              40: 'FF',  41: '--',  42: '--',  43: '--',  44: '--',  45: '--',  46: '--',  47: '--',  48: '--',  49: 'FF',   # [ 40,  41,  42,  43,  44,  45,  46,  47,  48,  49]
              50: 'FF',  51: '--',  52: '--',  53: '--',  54: '--',  55: '--',  56: '--',  57: '--',  58: '--',  59: 'FF',   # [ 50,  51,  52,  53,  54,  55,  56,  57,  58,  59]
              60: 'FF',  61: '--',  62: '--',  63: '--',  64: '--',  65: '--',  66: '--',  67: '--',  68: '--',  69: 'FF',   # [ 60,  61,  62,  63,  64,  65,  66,  67,  68,  69]
              70: 'FF',  71: '--',  72: '--',  73: '--',  74: '--',  75: '--',  76: '--',  77: '--',  78: '--',  79: 'FF',   # [ 70,  71,  72,  73,  74,  75,  76,  77,  78,  79]
              80: 'FF',  81: 'wp',  82: 'wp',  83: 'wp',  84: 'wp',  85: 'wp',  86: 'wp',  87: 'wp',  88: 'wp',  89: 'FF',   # [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89]
              90: 'FF',  91: 'wR',  92: 'wN',  93: 'wB',  94: 'wQ',  95: 'wK',  96: 'wB',  97: 'wN',  98: 'wR',  99: 'FF',   # [ 90,  91,  92,  93,  94,  95,  96,  97,  98,  99]
             100: 'FF', 101: 'FF', 102: 'FF', 103: 'FF', 104: 'FF', 105: 'FF', 106: 'FF', 107: 'FF', 108: 'FF', 109: 'FF',   # [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
             110: 'FF', 111: 'FF', 112: 'FF', 113: 'FF', 114: 'FF', 115: 'FF', 116: 'FF', 117: 'FF', 118: 'FF', 119: 'FF'}   # [110, 111, 112, 113, 114, 115, 116, 117, 118, 119]

# Pawn specific info
# This feels out of place lol, but more robust kinda
black_pawn_start = []
white_pawn_start = []
black_pawn_end = []
white_pawn_end = []

black_pawn_en_passant_cords = []
white_pawn_en_passant_cords = []

for square_index, piece_code in start_board.items():
    if piece_code == 'bp':
        black_pawn_start.append(square_index)
        black_pawn_en_passant_cords.append(square_index+10)
        white_pawn_end.append(square_index-10)
    if piece_code == 'wp':
        white_pawn_start.append(square_index)
        white_pawn_en_passant_cords.append(square_index-10)
        black_pawn_end.append(square_index+10)




# note - all other squares are "off the board" - this is more efficient when checking for moves vs 8x8
real_board_squares = [21, 22, 23, 24, 25, 26, 27, 28,
                      31, 32, 33, 34, 35, 36, 37, 38,
                      41, 42, 43, 44, 45, 46, 47, 48,
                      51, 52, 53, 54, 55, 56, 57, 58,
                      61, 62, 63, 64, 65, 66, 67, 68,
                      71, 72, 73, 74, 75, 76, 77, 78,
                      81, 82, 83, 84, 85, 86, 87, 88,
                      91, 92, 93, 94, 95, 96, 97, 98]

# note - added this to make it easier for me to track square id to algebraic notation
algebraic_to_square_id = {'a8': 21, 'b8': 22, 'c8': 23, 'd8': 24, 'e8': 25, 'f8': 26, 'g8': 27, 'h8': 28,
                          'a7': 31, 'b7': 32, 'c7': 33, 'd7': 34, 'e7': 35, 'f7': 36, 'g7': 37, 'h7': 38,
                          'a6': 41, 'b6': 42, 'c6': 43, 'd6': 44, 'e6': 45, 'f6': 46, 'g6': 47, 'h6': 48,
                          'a5': 51, 'b5': 52, 'c5': 53, 'd5': 54, 'e5': 55, 'f5': 56, 'g5': 57, 'h5': 58,
                          'a4': 61, 'b4': 62, 'c4': 63, 'd4': 64, 'e4': 65, 'f4': 66, 'g4': 67, 'h4': 68,
                          'a3': 71, 'b3': 72, 'c3': 73, 'd3': 74, 'e3': 75, 'f3': 76, 'g3': 77, 'h3': 78,
                          'a2': 81, 'b2': 82, 'c2': 83, 'd2': 84, 'e2': 85, 'f2': 86, 'g2': 87, 'h2': 88,
                          'a1': 91, 'b1': 92, 'c1': 93, 'd1': 94, 'e1': 95, 'f1': 96, 'g1': 97, 'h1': 98}


square_id_to_algebraic = {v: k for k, v in algebraic_to_square_id.items()}

# FEN representation to board pieces
fen_to_piece = {'p': 'bp',
                'n': 'bN',
                'b': 'bB',
                'r': 'bR',
                'q': 'bQ',
                'k': 'bK',
                'P': 'wp',
                'N': 'wN',
                'B': 'wB',
                'R': 'wR',
                'Q': 'wQ',
                'K': 'wK'}



king_mid = [0,   0,   0,   0,   0,   0,   0,   0,   0, 0,
            0,   0,   0,   0,   0,   0,   0,   0,   0, 0,
            0, -30, -40, -40, -50, -50, -40, -40, -30, 0,
            0, -30, -40, -40, -50, -50, -40, -40, -30, 0,
            0, -30, -40, -40, -50, -50, -40, -40, -30, 0,
            0, -30, -40, -40, -50, -50, -40, -40, -30, 0,
            0, -20, -30, -30, -40, -40, -30, -30, -20, 0,
            0, -10, -20, -20, -20, -20, -20, -20, -10, 0,
            0,  20,  20,   0,   0,   0,   0,  20,  20, 0,
            0,  0,  20,   40,   0,   0,   0,  40,  20, 0,
            0,   0,   0,   0,   0,   0,   0,   0,   0, 0,
            0,   0,   0,   0,   0,   0,   0,   0,   0, 0]

queen_mid = [0,   0,   0,   0,  0,  0,   0,   0,   0, 0,
             0,   0,   0,   0,  0,  0,   0,   0,   0, 0,
             0, -20, -10, -10, -5, -5, -10, -10, -20, 0,
             0, -10,   0,   0,  0,  0,   0,   0, -10, 0,
             0, -10,   0,   5,  5,  5,   5,   0, -10, 0,
             0,  -5,   0,   5,  5,  5,   5,   0,  -5, 0,
             0,  -5,   0,   5,  5,  5,   5,   0,  -5, 0,
             0, -10,   5,   5,  5,  5,   5,   0, -10, 0,
             0, -10,   0,   5,  0,  0,   0,   0, -10, 0,
             0, -20, -10, -10,  0,  0, -10, -10, -20, 0,
             0,   0,   0,   0,  0,  0,   0,   0,   0, 0,
             0,   0,   0,   0,  0,  0,   0,   0,   0, 0]

rook_mid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 5, 15, 15, 15, 15, 15, 15, 5, 0,
            0, -5, 0, 0, 0, 0, 0, 0, -5, 0,
            0, -5, 0, 0, 0, 0, 0, 0, -5, 0,
            0, -5, 0, 0, 0, 0, 0, 0, -5, 0,
            0, -5, 0, 0, 0, 0, 0, 0, -5, 0,
            0, -5, 0, 0, 0, 0, 0, 0, -5, 0,
            0, 0, 0, 10, 10, 10, 10, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

bishop_mid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, -20, -10, -10, -10, -10, -10, -10, -20, 0,
              0, -10, 0, 0, 0, 0, 0, 0, -10, 0,
              0, -10, 0, 5, 10, 10, 5, 0, -10, 0,
              0, -10, 5, 5, 10, 10, 5, 5, -10, 0,
              0, -10, 0, 10, 10, 10, 10, 0, -10, 0,
              0, -10, 10, 10, 10, 10, 10, 10, -10, 0,
              0, -10, 10, 0, 10, 10, 0, 10, -10, 0,
              0, -20, -10, -50, -10, -10, -50, -10, -20, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

knight_mid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, -30, -30, -10, -10, -10, -10, -30, -30, 0,
              0, -20, -20, 0, 0, 0, 0, -20, -20, 0,
              0, -10, 0, 10, 15, 15, 10, 0, -10, 0,
              0, -10, 5, 15, 20, 20, 15, 5, -10, 0,
              0, -10, 0, 15, 20, 20, 15, 0, -10, 0,
              0, -10, 5, 10, 15, 15, 10, 5, -10, 0,
              0, -20, -20, 0, 5, 5, 0, -20, -20, 0,
              0, -30, -30, -10, -10, -10, -10, -30, -30, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

pawn_mid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 50, 50, 50, 50, 50, 50, 50, 50, 0,
            0, 20, 20, 20, 30, 30, 20, 20, 20, 0,
            0, 10, 10, 10, 25, 25, 10, 10, 10, 0,
            0, 0, 0, 0, 20, 20, 0, 0, 0, 0,
            0, 5, -5, -10, 0, 0, -10, -5, 5, 0,
            0, 5, 10, 10, -20, -20, 10, 10, 5, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


piece_value_mid_game = {'K': king_mid,
                        'Q': queen_mid,
                        'R': rook_mid,
                        'B': bishop_mid,
                        'N': knight_mid,
                        'p': pawn_mid}

# MVV-LVA move ordering  https://www.chessprogramming.org/MVV-LVA
mvv_lva_values = {'K': 20000,
                  'Q': 900,
                  'R': 490,
                  'B': 320,
                  'N': 290,
                  'p': 100,
                  '-': 0}