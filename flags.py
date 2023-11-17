from config import PASSWORD

part_size = len(PASSWORD) // 7

FLAG1 = PASSWORD[:part_size]
FLAG2 = PASSWORD[part_size:part_size * 2]
FLAG3 = PASSWORD[part_size * 2:part_size * 3]
FLAG4 = PASSWORD[part_size * 3:part_size * 4]
FLAG5 = PASSWORD[part_size * 4:part_size * 5]
FLAG6 = PASSWORD[part_size * 5:part_size * 6]
FLAG7 = PASSWORD[part_size * 6:]
