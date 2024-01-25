order = [17, 17, 12, 9, 14, 8, 5, 1, 19, 17, 16, 15, 5, 9, 18, 9, 4, 5, 4, 9, 12, 15, 5, 9, 14, 10, 
6, 13, 1, 7, 12, 16, 12, 13, 19, 10, 16, 13, 16, 1, 19, 10, 9, 7, 19, 7, 4, 17, 9, 2]

ram_frames = []
limit_frames = 26

swap_cnt = 0

def exists(arr: [], el: int) -> bool:
    for i in arr:
        if i == el:
            return True
    return False


def find_farthest_el(arr: [], idx_from: int) -> int:
    farthest_pos = -1
    fathest_el = -1
    for i in arr:
        idx_from_cp = idx_from
        while idx_from_cp < len(order):
            if order[idx_from_cp] == i:
                if farthest_pos < idx_from_cp:
                    farthest_pos = idx_from_cp
                    farthest_el = i
                break
            idx_from_cp += 1
        if idx_from_cp == len(order):
            farthest_pos = idx_from_cp
            farthest_el = i
            break
    if farthest_el == -1:
        farthest_el = arr[0]
    return farthest_el
        


def print_state(i: int, arr: [], el_queued: [], el_in: [] = [], el_out: [] = []):
    i += 1
    print(f"{i})\t {el_queued} \t--->\t {arr}, \tin: {el_in}, out: {el_out}")


for i in range(len(order)):
    if order[i] in ram_frames:
        print_state(i, ram_frames, [order[i]])
        continue
    if len(ram_frames) < limit_frames:
        ram_frames.append(order[i])
        print_state(i, ram_frames, [order[i]], el_in=[order[i]])
        continue
    else:
        to_remove = find_farthest_el(ram_frames, i)
        ram_frames.remove(to_remove)
        ram_frames.append(order[i])
        swap_cnt += 1
        print_state(i, ram_frames, [order[i]], [order[i]], [to_remove])

print("Количество замен:", swap_cnt)

print("page fault %", swap_cnt / len(order))