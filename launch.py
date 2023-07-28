import codecs
import json

from rankings.parse import parse
from rankings.un import calculate_passing_candidates

roles_info, candidate_rankings = parse()
result = calculate_passing_candidates(roles_info, candidate_rankings)


file = codecs.open("result.txt", "w", "utf-8")
file.write(json.dumps(result, ensure_ascii=False))
file.close()