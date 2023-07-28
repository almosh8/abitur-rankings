import parse


# roles_info = {role: places}
# candidate_rankings = [{candidate_id: {candidate_points, {priority: role}}]
def calculate_passing_candidates(roles_info, candidate_rankings):
    result_tables = {}
    candidate_counted = {}

    candidate_rankings = dict(sorted(candidate_rankings.items(), key=lambda item: item[1][0], reverse=True))

    for candidate_id in candidate_rankings:

        if candidate_id in candidate_counted:
            continue
        candidate_counted[candidate_id] = True

        candidate_info = candidate_rankings[candidate_id]
        selected_roles = dict(sorted(candidate_info[1].items(), key=lambda item: item[1]))
        if candidate_id == '158-507-439 89':
            print(candidate_id)

        for prior in selected_roles:
            role = selected_roles[prior]
            if roles_info[role] > 0:
                roles_info[role] -= 1
                if not role in result_tables:
                    result_tables[role] = []
                result_tables[role].append([candidate_id, candidate_info[0]])
                break

    return result_tables

