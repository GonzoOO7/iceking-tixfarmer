import iceking_tixfarmer
import bank_to_king
import get_gold
from utils import timeout

timeout(3)

while True:
    bank_to_king.main()
    iceking_tixfarmer.main()
    get_gold.main()