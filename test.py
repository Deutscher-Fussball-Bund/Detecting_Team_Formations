import os
import random

from avg_formation import get_avg_formations
from hausdorff_metric import calculate_formation

print('')
player_positions, shirtnumbers = get_avg_formations(os.path.dirname(__file__) + '/../Data_STS/DFL_04_02_positions_raw_DFL-COM-000001_DFL-MAT-X03BWS.xml', 50000, 101000, 'DFL-CLU-000N99')
calculate_formation(player_positions)
print('')
player_positions, shirtnumbers = get_avg_formations(os.path.dirname(__file__) + '/../Data_STS/ersteHalbzeit.xml', 30000, 50000, 'DFL-CLU-000N99')
calculate_formation(player_positions)
print('')