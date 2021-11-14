import itertools

operators = ["+", "-", "*", "/"]


def main(nums):
    num_permutations = (list(itertools.permutations(nums, 4)))
    operator_permutationss = (list(itertools.permutations(
        [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], 3)))
    operator_permutationss = list(set(operator_permutationss))

    for i in range(len(num_permutations)):
        permutation = list(num_permutations[i])
        for j in range(len(operator_permutationss)):
            answer = 0.0
            for k in range(len(num_permutations[i])-1):
                if k == 0:
                    if operator_permutationss[j][k] == 0:
                        answer = float(permutation[k]) + \
                            float(permutation[k+1])
                    elif operator_permutationss[j][k] == 1:
                        answer = float(permutation[k]) - \
                            float(permutation[k+1])
                    elif operator_permutationss[j][k] == 2:
                        answer = float(permutation[k]) * \
                            float(permutation[k+1])
                    elif operator_permutationss[j][k] == 3:
                        if float(permutation[k+1]) == 0:
                            continue
                        else:
                            answer = float(permutation[k]) / \
                                float(permutation[k+1])
                else:
                    if operator_permutationss[j][k] == 0:
                        answer = answer + float(permutation[k+1])
                    elif operator_permutationss[j][k] == 1:
                        answer = answer - float(permutation[k+1])
                    elif operator_permutationss[j][k] == 2:
                        answer = answer * float(permutation[k+1])
                    elif operator_permutationss[j][k] == 3:
                        if permutation[k+1] == 0:
                            continue
                        else:
                            answer = answer / float(permutation[k+1])
            if answer == 10.0:
                print(num_permutations[i][0], operators[operator_permutationss[j][0]],
                      num_permutations[i][1], operators[operator_permutationss[j][1]],
                      num_permutations[i][2], operators[operator_permutationss[j][2]],
                      num_permutations[i][3], " = ", answer)

# def main(nums):
#     num_permutations = (list(itertools.permutations(nums, 4)))
#     calc_permutationss = (list(itertools.permutations(
#         ["+", "+", "+", "-", "-", "-", "*", "*", "*", "/", "/", "/"], 3)))
#     calc_permutationss = list(set(calc_permutationss))

#     for i in range(len(num_permutations)):
#         permutation = list(num_permutations[i])
#         for j in range(len(calc_permutationss)):
#             formula = []
#             for k in range(len(num_permutations[i])-1):
#                 if calc_permutationss[j][k] not in "*/":
#                     if k == 0:
#                         formula += "(" + \
#                             str(permutation[k]) + calc_permutationss[j][k] + \
#                             str(permutation[k+1]) + ")"
#                     else:
#                         formula.append(
#                             calc_permutationss[j][k] + str(permutation[k+1]) + ")")
#                         formula.insert(0, '(')
#                 else:
#                     if k == 0:
#                         formula += str(permutation[k]) + \
#                             calc_permutationss[j][k] + str(permutation[k+1])
#                     else:
#                         formula.append(
#                             calc_permutationss[j][k] + str(permutation[k+1]))
#             ret = eval("".join(map(str, formula)))
#             if ret == 10.0:
#                 print("".join(map(str, formula)), "=", ret)


if __name__ == '__main__':
    main([1, 3, 3, 7])
    main([0, 3, 5, 8])
    input_string_list = input()
    input_list = [int(i) for i in input_string_list]
    main(list(input_list))
